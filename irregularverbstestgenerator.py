#!/usr/bin/python
# -*- coding: utf-8 -*-

"""\
Entry point of irregularverbstestgenerator tool.
TODO
"""

__author__ = "Alexandre Chassany"
__copyright__ = "Copyright 2013, Alexandre Chassany"
__license__ = "GPL"
__version__ = "0.0.1"
__maintainer__ = "Alexandre Chassany"
__email__ = "alexandre.chassany@gmail.com"
__status__ = "Prototype"

import sys
import random
import os
from sets import Set
from PySide.QtGui import QMainWindow, QApplication, QStandardItemModel, \
    QStandardItem, QItemSelectionModel, QMessageBox, QTextCursor,  \
    QTextTableFormat, QFileDialog, QDesktopServices
from PySide.QtCore import Qt
from ui_irregularverbstestgenerator import Ui_IrregularVerbsTestGenerator
import xlrd
import xlwt 
from elementtree.SimpleXMLWriter import XMLWriter
from StringIO import StringIO

class Verb:
    def __init__(self, base_verbal, preterit, past_participle, translation):
        self.base_verbal = base_verbal
        self.preterit = preterit
        self.past_participle = past_participle
        self.translation = translation

    def array(self):
        return [self.base_verbal, self.preterit, self.past_participle, self.translation]

class Level:
    def __init__(self, verbs_list):
        self.verbs_dict = {}
        for verb in verbs_list:
            self.verbs_dict[verb.base_verbal] = verb
        self.verbs_list = verbs_list

class CustomRandom:
    def __init__(self):
        random.seed()
        self.last_generated_number = Set()

    def next(self):
        res = random.randint(0,3)
        while(res in self.last_generated_number):
            res = random.randint(0,3)
        self.last_generated_number.add(res)
        if len(self.last_generated_number) == 4:
            self.last_generated_number = Set()
        return res

class Test:
    def __init__(self):
        self.array = []
        self.solutions = []

    def __str__(self):
        _str = ""
        for entry in self.array:
            _str += "{0}\n".format(entry)
        _str += "\nSolutions: "
        for value in self.solutions:
            _str += "{0} ".format(value)

        return _str

def _generate_test(verbs, nb_lines, include_solutions):
    random.shuffle(verbs)
    custom_random = CustomRandom()
    test = Test()
    for i in range(nb_lines):
        verb = verbs[i].array()
        index = custom_random.next()
        test.array.append((index, verb[index]))
        if include_solutions:
            test.solutions.extend([verb[i] for i in range(len(verb)) if i != index])
    random.shuffle(test.solutions)
    return test


def _add_row(row, w):
    w.start(u"tr")
    index = row[0]
    verb = row[1]
    for i in range(4):
        if index == i:
            w.element(u"td", verb)
        else:
            w.element(u"td", u"")
    w.end(u"tr")

def _test_to_html(test):
    iodevice = StringIO()
    w = XMLWriter(iodevice, "utf-8")
    w.start(u"html")
    w.start(u"body")
    w.start(u"table", border="1")
    w.start(u"tr")
    w.element(u"th", u"Base verbale")
    w.element(u"th", u"Preterit")
    w.element(u"th", u"Participe passé")
    w.element(u"th", u"Traduction")
    w.element(u"th", u"Points")
    w.end(u"tr")
    for entry in test.array:
        _add_row(entry, w)
    w.end(u"table")
    w.end(u"body")
    w.end(u"html")

    html_str = iodevice.getvalue()
    #f = open("test.html", "w")
    #f.write(html_str)
    #f.close()
    iodevice.close()
    return html_str

def _get_cell_format_information(workbook, sheet, row_index):
    format_index = sheet.cell_xf_index(row_index,0)
    format = workbook.xf_list[format_index]
    font = workbook.font_list[format.font_index]
    return format, font

def _r_font_to_w_font(r_font):
    w_font = xlwt.Font()
    w_font.height = r_font.height
    w_font.bold = r_font.weight == 700
    w_font.italic = r_font.italic
    w_font.colour_index = r_font.colour_index
    w_font.escapement = r_font.escapement
    w_font.family = r_font.family
    w_font.name = r_font.name
    w_font.outline = r_font.outline
    w_font.shadow = r_font.shadow
    w_font.struck_out = r_font.struck_out
    w_font.underlined = r_font.underline_type

    return w_font

def _r_alignment_to_w_alignment(r_alignment):
    w_alignment = xlwt.Alignment()
    w_alignment.horz = r_alignment.hor_align
    w_alignment.vert = r_alignment.vert_align
    w_alignment.dire = r_alignment.text_direction
    w_alignment.rota = r_alignment.rotation
    w_alignment.wrap = r_alignment.text_wrapped
    w_alignment.shri = r_alignment.shrink_to_fit
    w_alignment.inde = r_alignment.indent_level
    
    return w_alignment

def _r_borders_to_w_borders(r_borders):
    w_borders = xlwt.Borders()
    w_borders.left = r_borders.left_line_style
    w_borders.left_colour = r_borders.left_colour_index
    w_borders.right = r_borders.right_line_style
    w_borders.right_colour = r_borders.right_colour_index
    w_borders.top = r_borders.top_line_style
    w_borders.top_colour = r_borders.top_colour_index
    w_borders.bottom = r_borders.bottom_line_style
    w_borders.bottom_colour = r_borders.bottom_colour_index

    return w_borders

def _r_format_to_w_format(r_format, r_font):
    w_style = xlwt.XFStyle()
    w_style.font = _r_font_to_w_font(r_font)
    w_style.alignment = _r_alignment_to_w_alignment(r_format.alignment)
    w_style.borders = _r_borders_to_w_borders(r_format.border)
    return w_style

def _get_string_width(font, string):
    height = (font.height*1.0/1440.0)/0.05*96*0.8
    return int(round(len(string)*height))

def _export_test_to_xls_file(test, filepath):

    # Open format workbook
    f_workbook = xlrd.open_workbook('format.xls', formatting_info=True)
    f_sheet = f_workbook.sheet_by_index(0)

    # Open destination workbook
    wb = xlwt.Workbook(encoding='utf-8')
    sheet = wb.add_sheet(u"Test")

    # Write header
    title_r_format, title_r_font = _get_cell_format_information(f_workbook, f_sheet, 0)
    title_w_style = _r_format_to_w_format(title_r_format, title_r_font)
    content_r_format, content_r_font = _get_cell_format_information(f_workbook, f_sheet, 1)
    content_w_style = _r_format_to_w_format(content_r_format, content_r_font)
    solution_r_format, solution_r_font = _get_cell_format_information(f_workbook, f_sheet, 2)
    solution_w_style = _r_format_to_w_format(solution_r_format, solution_r_font)
    max_cell_height = max(_get_string_width(title_w_style.font, 'w'), 
                     _get_string_width(content_w_style.font, 'w'))

    max_cell_width = len(u"Participe passé") * max_cell_height
    sheet.write(0, 0, u"Base verbale", title_w_style)
    sheet.write(0, 1, u"Preterit", title_w_style)
    sheet.write(0, 2, u"Participe passé", title_w_style)
    sheet.write(0, 3, u"Traduction", title_w_style)
    sheet.write(0, 4, u"Points", title_w_style)
    sheet.row(0).height = max_cell_height

    # Write test content
    for i in range(len(test.array)):
        for j in range(5):
            if j == test.array[i][0]:
                sheet.write(i+1, test.array[i][0], test.array[i][1], content_w_style)
                max_cell_width = max(max_cell_width, len(test.array[i][1]))
            else:
                sheet.write(i+1, j, '', content_w_style)
            sheet.row(i+1).height = max_cell_height
    # Resize columns
    for i in range(5):
        sheet.col(i).width = max_cell_width
    
    # Write solutions
    solution_lines = []
    max_line_width = max_cell_width * 5
    for solution in test.solutions:
        width = _get_string_width(solution_w_style.font, " / "+solution)
        if len(solution_lines) == 0 or (_get_string_width(solution_w_style.font, solution_lines[-1])+width) > max_line_width:
            solution_lines.append(solution)
        else:
            solution_lines[-1] += " / "+solution

    current_row = len(test.array)+2
    for line in solution_lines:
        sheet.write_merge(current_row, current_row, 0, 4, line, solution_w_style)
        current_row+=1

    wb.save(filepath)

class MainWindow(QMainWindow, Ui_IrregularVerbsTestGenerator):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.test = Test()

        # Load verbs informations
        workbook = xlrd.open_workbook('irv.xls')
        self.levels_list = []
        self.levels_dict = {}
        for sheet in workbook.sheets():
            verbs = []
            for i in range(sheet.nrows):
                verb = Verb(sheet.row(i)[0].value, sheet.row(i)[1].value,
                            sheet.row(i)[2].value, sheet.row(i)[3].value)
                verbs.append(verb)
            self.levels_list.append(sheet.name)
            self.levels_dict[sheet.name] = Level(verbs)

        self.mClassList.currentIndexChanged.connect(self._on_level_selected_changed)
        for level in self.levels_list:
            self.mClassList.addItem(level, level)
        self.mGenerate.clicked.connect(self._on_generate)
        self.mActionSave.triggered.connect(self._on_export)
        
    def _on_level_selected_changed(self, index):
        level_name = self.mClassList.itemData(index)
        level = self.levels_dict[level_name]
        model = QStandardItemModel()
        for verb in level.verbs_list:
            item = QStandardItem(verb.base_verbal)
            item.setData(verb.base_verbal)
            model.appendRow(item)

        self.mVerbsList.setModel(model)

    def _on_generate(self):
        index_list = self.mVerbsList.selectionModel().selectedRows()
        nb_lines = self.mNbLines.value()
        if nb_lines > len(index_list):
            QMessageBox.warning(self, self.tr("IrregularVerbsTestGenerator"),
                                self.tr("You haven't selected enought verbs to generate a test with {0} lines !".format(nb_lines)))
            return
        level_name = self.mClassList.itemData(self.mClassList.currentIndex())
        level = self.levels_dict[level_name]
        verbs = []
        for index in index_list:
            verbs.append(level.verbs_dict[index.data()])
        include_solutions = self.mIncludeSolutions.isChecked()
        self.test = _generate_test(verbs, nb_lines, include_solutions)

        document = self.mTestPreview.document()
        document.clear()
        html = _test_to_html(self.test)
        document.setHtml(html)

    def _on_export(self):
        if len(self.test.array) == 0:
            QMessageBox.warning(self, self.tr("IrregularVerbsTestGenerator"),
                                self.tr("You need to generate a test first !"))
            return

        export_file, export_format = QFileDialog.getSaveFileName(
            self, 
            self.tr("Save test"),
            QDesktopServices.storageLocation(QDesktopServices.DesktopLocation),
            self.tr("Xls file (*.xls)"))
        
        if not export_file:
            return

        export_file = "{0}.xls".format(os.path.splitext(export_file)[0])
        _export_test_to_xls_file(self.test, export_file)
        
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    frame = MainWindow()
    frame.show()    
    app.exec_()


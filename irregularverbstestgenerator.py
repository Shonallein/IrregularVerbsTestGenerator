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
from sets import Set
from PySide.QtGui import QMainWindow, QApplication, QStandardItemModel, \
    QStandardItem, QItemSelectionModel, QMessageBox
from ui_irregularverbstestgenerator import Ui_IrregularVerbsTestGenerator
from xlrd import open_workbook
from xlrd.book import Book
from xlrd.sheet import Sheet

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
            test.solutions.append([verb[i] for i in range(len(verb)) if i != index])
    return test
        

class MainWindow(QMainWindow, Ui_IrregularVerbsTestGenerator):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        # Load verbs informations
        workbook = open_workbook('irv.xls')
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
        level_name = self.mClassList.itemData(self.mClassList.currentIndex())
        level = self.levels_dict[level_name]
        verbs = []
        for index in index_list:
            verbs.append(level.verbs_dict[index.data()])
        include_solutions = self.mIncludeSolutions.isChecked()
        test = _generate_test(verbs, nb_lines, include_solutions)
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    frame = MainWindow()
    frame.show()    
    app.exec_()


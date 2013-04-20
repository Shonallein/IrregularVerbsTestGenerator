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
from PySide.QtGui import QMainWindow, QApplication
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

class MainWindow(QMainWindow, Ui_IrregularVerbsTestGenerator):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        # Load verbs informations
        workbook = open_workbook('irv.xls')
        verbs_sheets = []
        for sheet in workbook.sheets():
            verbs = []
            for i in range(sheet.nrows):
                verb = Verb(sheet.row(i)[0].value, sheet.row(i)[1].value,
                            sheet.row(i)[2].value, sheet.row(i)[3].value)
                verbs.append((verb.base_verbal, verb))
            verbs_sheets.append([sheet.name, verbs])
        self.verb_dict = dict(verbs_sheets)

        for key in self.verb_dict.keys():
            self.mClassList.addItem(key, key)
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    frame = MainWindow()
    frame.show()    
    app.exec_()


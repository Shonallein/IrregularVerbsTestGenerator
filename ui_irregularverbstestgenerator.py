# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'irregularverbstestgenerator.ui'
#
# Created: Fri Apr 19 19:56:39 2013
#      by: pyside-uic 0.2.13 running on PySide 1.1.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_IrregularVerbsTestGenerator(object):
    def setupUi(self, IrregularVerbsTestGenerator):
        IrregularVerbsTestGenerator.setObjectName("IrregularVerbsTestGenerator")
        IrregularVerbsTestGenerator.resize(834, 441)
        self.centralWidget = QtGui.QWidget(IrregularVerbsTestGenerator)
        self.centralWidget.setObjectName("centralWidget")
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.centralWidget)
        self.horizontalLayout_3.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.mTestPreview = QtGui.QTextBrowser(self.centralWidget)
        self.mTestPreview.setObjectName("mTestPreview")
        self.horizontalLayout_3.addWidget(self.mTestPreview)
        IrregularVerbsTestGenerator.setCentralWidget(self.centralWidget)
        self.menuBar = QtGui.QMenuBar(IrregularVerbsTestGenerator)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 834, 21))
        self.menuBar.setObjectName("menuBar")
        self.menuFile = QtGui.QMenu(self.menuBar)
        self.menuFile.setObjectName("menuFile")
        IrregularVerbsTestGenerator.setMenuBar(self.menuBar)
        self.dockWidget = QtGui.QDockWidget(IrregularVerbsTestGenerator)
        self.dockWidget.setFeatures(QtGui.QDockWidget.NoDockWidgetFeatures)
        self.dockWidget.setObjectName("dockWidget")
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.verticalLayout = QtGui.QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtGui.QLabel(self.dockWidgetContents)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.mClassList = QtGui.QComboBox(self.dockWidgetContents)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mClassList.sizePolicy().hasHeightForWidth())
        self.mClassList.setSizePolicy(sizePolicy)
        self.mClassList.setObjectName("mClassList")
        self.horizontalLayout.addWidget(self.mClassList)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtGui.QLabel(self.dockWidgetContents)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.mNbLines = QtGui.QSpinBox(self.dockWidgetContents)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mNbLines.sizePolicy().hasHeightForWidth())
        self.mNbLines.setSizePolicy(sizePolicy)
        self.mNbLines.setMinimum(1)
        self.mNbLines.setProperty("value", 10)
        self.mNbLines.setObjectName("mNbLines")
        self.horizontalLayout_2.addWidget(self.mNbLines)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.mVerbsList = QtGui.QListView(self.dockWidgetContents)
        self.mVerbsList.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.mVerbsList.setAlternatingRowColors(True)
        self.mVerbsList.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.mVerbsList.setObjectName("mVerbsList")
        self.verticalLayout.addWidget(self.mVerbsList)
        self.mIncludeSolutions = QtGui.QCheckBox(self.dockWidgetContents)
        self.mIncludeSolutions.setObjectName("mIncludeSolutions")
        self.verticalLayout.addWidget(self.mIncludeSolutions)
        self.mGenerate = QtGui.QPushButton(self.dockWidgetContents)
        self.mGenerate.setObjectName("mGenerate")
        self.verticalLayout.addWidget(self.mGenerate)
        self.dockWidget.setWidget(self.dockWidgetContents)
        IrregularVerbsTestGenerator.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockWidget)
        self.actionTodo = QtGui.QAction(IrregularVerbsTestGenerator)
        self.actionTodo.setObjectName("actionTodo")
        self.menuFile.addAction(self.actionTodo)
        self.menuBar.addAction(self.menuFile.menuAction())

        self.retranslateUi(IrregularVerbsTestGenerator)
        QtCore.QMetaObject.connectSlotsByName(IrregularVerbsTestGenerator)

    def retranslateUi(self, IrregularVerbsTestGenerator):
        IrregularVerbsTestGenerator.setWindowTitle(QtGui.QApplication.translate("IrregularVerbsTestGenerator", "IrregularVerbsTestGenerator", None, QtGui.QApplication.UnicodeUTF8))
        self.mTestPreview.setHtml(QtGui.QApplication.translate("IrregularVerbsTestGenerator", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("IrregularVerbsTestGenerator", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.dockWidget.setWindowTitle(QtGui.QApplication.translate("IrregularVerbsTestGenerator", "Test parameters", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("IrregularVerbsTestGenerator", "Class", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("IrregularVerbsTestGenerator", "Nb lines", None, QtGui.QApplication.UnicodeUTF8))
        self.mIncludeSolutions.setText(QtGui.QApplication.translate("IrregularVerbsTestGenerator", "Include solutions", None, QtGui.QApplication.UnicodeUTF8))
        self.mGenerate.setText(QtGui.QApplication.translate("IrregularVerbsTestGenerator", "Generate", None, QtGui.QApplication.UnicodeUTF8))
        self.actionTodo.setText(QtGui.QApplication.translate("IrregularVerbsTestGenerator", "Todo", None, QtGui.QApplication.UnicodeUTF8))


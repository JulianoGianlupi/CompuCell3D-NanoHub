# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'NewFileWizard.ui'
#
# Created: Wed Mar 02 16:44:32 2011
#      by: PyQt4 UI code generator 4.7.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_NewFileWizard(object):
    def setupUi(self, NewFileWizard):
        NewFileWizard.setObjectName("NewFileWizard")
        NewFileWizard.resize(376, 304)
        self.wizardPage1 = QtGui.QWizardPage()
        self.wizardPage1.setObjectName("wizardPage1")
        self.verticalLayout = QtGui.QVBoxLayout(self.wizardPage1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtGui.QLabel(self.wizardPage1)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 2)
        self.nameLE = QtGui.QLineEdit(self.wizardPage1)
        self.nameLE.setObjectName("nameLE")
        self.gridLayout.addWidget(self.nameLE, 0, 3, 1, 2)
        self.nameBrowsePB = QtGui.QPushButton(self.wizardPage1)
        self.nameBrowsePB.setObjectName("nameBrowsePB")
        self.gridLayout.addWidget(self.nameBrowsePB, 0, 5, 1, 1)
        self.label = QtGui.QLabel(self.wizardPage1)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 2)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 2, 3, 1)
        self.fileTypeCB = QtGui.QComboBox(self.wizardPage1)
        self.fileTypeCB.setObjectName("fileTypeCB")
        self.fileTypeCB.addItem("")
        self.fileTypeCB.addItem("")
        self.fileTypeCB.addItem("")
        self.fileTypeCB.addItem("")
        self.fileTypeCB.addItem("")
        self.gridLayout.addWidget(self.fileTypeCB, 1, 3, 2, 2)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 1, 5, 1, 1)
        self.label_4 = QtGui.QLabel(self.wizardPage1)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 0, 2, 2)
        self.locationBrowsePB = QtGui.QPushButton(self.wizardPage1)
        self.locationBrowsePB.setObjectName("locationBrowsePB")
        self.gridLayout.addWidget(self.locationBrowsePB, 2, 5, 2, 1)
        self.locationLE = QtGui.QLineEdit(self.wizardPage1)
        self.locationLE.setObjectName("locationLE")
        self.gridLayout.addWidget(self.locationLE, 3, 3, 1, 2)
        self.label_3 = QtGui.QLabel(self.wizardPage1)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 4, 0, 1, 3)
        self.projectDirLE = QtGui.QLineEdit(self.wizardPage1)
        self.projectDirLE.setReadOnly(False)
        self.projectDirLE.setObjectName("projectDirLE")
        self.gridLayout.addWidget(self.projectDirLE, 4, 3, 1, 2)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 4, 5, 1, 1)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 5, 3, 2, 2)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 5, 5, 3, 1)
        self.customTypeLE = QtGui.QLineEdit(self.wizardPage1)
        self.customTypeLE.setEnabled(False)
        self.customTypeLE.setObjectName("customTypeLE")
        self.gridLayout.addWidget(self.customTypeLE, 6, 4, 2, 1)
        self.customTypeCHB = QtGui.QCheckBox(self.wizardPage1)
        self.customTypeCHB.setObjectName("customTypeCHB")
        self.gridLayout.addWidget(self.customTypeCHB, 7, 0, 1, 3)
        self.verticalLayout.addLayout(self.gridLayout)
        spacerItem6 = QtGui.QSpacerItem(20, 71, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem6)
        NewFileWizard.addPage(self.wizardPage1)

        self.retranslateUi(NewFileWizard)
        QtCore.QObject.connect(self.customTypeCHB, QtCore.SIGNAL("toggled(bool)"), self.customTypeLE.setEnabled)
        QtCore.QObject.connect(self.customTypeCHB, QtCore.SIGNAL("toggled(bool)"), self.fileTypeCB.setDisabled)
        QtCore.QMetaObject.connectSlotsByName(NewFileWizard)
        NewFileWizard.setTabOrder(self.nameLE, self.nameBrowsePB)
        NewFileWizard.setTabOrder(self.nameBrowsePB, self.locationLE)
        NewFileWizard.setTabOrder(self.locationLE, self.locationBrowsePB)
        NewFileWizard.setTabOrder(self.locationBrowsePB, self.fileTypeCB)
        NewFileWizard.setTabOrder(self.fileTypeCB, self.customTypeCHB)
        NewFileWizard.setTabOrder(self.customTypeCHB, self.customTypeLE)
        NewFileWizard.setTabOrder(self.customTypeLE, self.projectDirLE)

    def retranslateUi(self, NewFileWizard):
        NewFileWizard.setWindowTitle(QtGui.QApplication.translate("NewFileWizard", "Add New File (Resource) to CC3D Simulation", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("NewFileWizard", "Name:", None, QtGui.QApplication.UnicodeUTF8))
        self.nameBrowsePB.setText(QtGui.QApplication.translate("NewFileWizard", "Browse...", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("NewFileWizard", "File Type:", None, QtGui.QApplication.UnicodeUTF8))
        self.fileTypeCB.setItemText(0, QtGui.QApplication.translate("NewFileWizard", "Main Python Script", None, QtGui.QApplication.UnicodeUTF8))
        self.fileTypeCB.setItemText(1, QtGui.QApplication.translate("NewFileWizard", "XML Script", None, QtGui.QApplication.UnicodeUTF8))
        self.fileTypeCB.setItemText(2, QtGui.QApplication.translate("NewFileWizard", "Python File", None, QtGui.QApplication.UnicodeUTF8))
        self.fileTypeCB.setItemText(3, QtGui.QApplication.translate("NewFileWizard", "PIF File", None, QtGui.QApplication.UnicodeUTF8))
        self.fileTypeCB.setItemText(4, QtGui.QApplication.translate("NewFileWizard", "Concentration File", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("NewFileWizard", " Location:", None, QtGui.QApplication.UnicodeUTF8))
        self.locationBrowsePB.setText(QtGui.QApplication.translate("NewFileWizard", "Browse...", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("NewFileWizard", "Project Directory", None, QtGui.QApplication.UnicodeUTF8))
        self.customTypeCHB.setText(QtGui.QApplication.translate("NewFileWizard", " Custom File Type ", None, QtGui.QApplication.UnicodeUTF8))


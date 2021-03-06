# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/kovid/work/calibre/src/calibre/gui2/dialogs/tag_list_editor.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_TagListEditor(object):
    def setupUi(self, TagListEditor):
        TagListEditor.setObjectName("TagListEditor")
        TagListEditor.resize(397, 335)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(I("chapters.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        TagListEditor.setWindowIcon(icon)
        self.gridlayout = QtWidgets.QGridLayout(TagListEditor)
        self.gridlayout.setObjectName("gridlayout")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label = QtWidgets.QLabel(TagListEditor)
        self.label.setObjectName("label")
        self.horizontalLayout_11.addWidget(self.label)
        self.search_box = HistoryLineEdit(TagListEditor)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.search_box.sizePolicy().hasHeightForWidth())
        self.search_box.setSizePolicy(sizePolicy)
        self.search_box.setObjectName("search_box")
        self.horizontalLayout_11.addWidget(self.search_box)
        self.search_button = QtWidgets.QPushButton(TagListEditor)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(I("search.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.search_button.setIcon(icon1)
        self.search_button.setObjectName("search_button")
        self.horizontalLayout_11.addWidget(self.search_button)
        self.gridlayout.addLayout(self.horizontalLayout_11, 0, 0, 1, 2)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.delete_button = QtWidgets.QToolButton(TagListEditor)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(I("trash.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.delete_button.setIcon(icon2)
        self.delete_button.setIconSize(QtCore.QSize(32, 32))
        self.delete_button.setObjectName("delete_button")
        self.verticalLayout_2.addWidget(self.delete_button)
        self.rename_button = QtWidgets.QToolButton(TagListEditor)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(I("edit_input.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.rename_button.setIcon(icon3)
        self.rename_button.setIconSize(QtCore.QSize(32, 32))
        self.rename_button.setObjectName("rename_button")
        self.verticalLayout_2.addWidget(self.rename_button)
        self.gridlayout.addLayout(self.verticalLayout_2, 1, 0, 1, 1)
        self.table = QtWidgets.QTableWidget(TagListEditor)
        self.table.setAlternatingRowColors(True)
        self.table.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.table.setObjectName("table")
        self.table.setColumnCount(0)
        self.table.setRowCount(0)
        self.gridlayout.addWidget(self.table, 1, 1, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(TagListEditor)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.gridlayout.addWidget(self.buttonBox, 3, 0, 1, 2)
        self.label.setBuddy(self.search_box)

        self.retranslateUi(TagListEditor)
        self.buttonBox.accepted.connect(TagListEditor.accept)
        self.buttonBox.rejected.connect(TagListEditor.reject)
        QtCore.QMetaObject.connectSlotsByName(TagListEditor)

    def retranslateUi(self, TagListEditor):

        TagListEditor.setWindowTitle(_("Category editor"))
        self.label.setText(_("&Search for:"))
        self.search_box.setToolTip(_("Search for an item in the Tag column"))
        self.search_button.setToolTip(_("Find the first/next matching item"))
        self.search_button.setText(_("&Find"))
        self.delete_button.setToolTip(_("Delete item from database. This will unapply the item from all books and then remove it from the database."))
        self.delete_button.setText(_("..."))
        self.rename_button.setToolTip(_("Rename the item in every book where it is used."))
        self.rename_button.setText(_("..."))
        self.rename_button.setShortcut(_("Ctrl+S"))

from calibre.gui2.widgets import HistoryLineEdit


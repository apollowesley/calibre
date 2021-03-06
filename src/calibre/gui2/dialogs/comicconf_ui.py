# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/kovid/work/calibre/src/calibre/gui2/dialogs/comicconf.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(646, 503)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(I("convert.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.title_label = QtWidgets.QLabel(Dialog)
        self.title_label.setObjectName("title_label")
        self.gridLayout.addWidget(self.title_label, 0, 0, 1, 1)
        self.opt_title = EnLineEdit(Dialog)
        self.opt_title.setObjectName("opt_title")
        self.gridLayout.addWidget(self.opt_title, 0, 1, 1, 1)
        self.author_label = QtWidgets.QLabel(Dialog)
        self.author_label.setObjectName("author_label")
        self.gridLayout.addWidget(self.author_label, 1, 0, 1, 1)
        self.opt_author = EnLineEdit(Dialog)
        self.opt_author.setObjectName("opt_author")
        self.gridLayout.addWidget(self.opt_author, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.opt_colors = QtWidgets.QSpinBox(Dialog)
        self.opt_colors.setMinimum(8)
        self.opt_colors.setMaximum(3200000)
        self.opt_colors.setSingleStep(8)
        self.opt_colors.setObjectName("opt_colors")
        self.gridLayout.addWidget(self.opt_colors, 2, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.opt_profile = QtWidgets.QComboBox(Dialog)
        self.opt_profile.setObjectName("opt_profile")
        self.gridLayout.addWidget(self.opt_profile, 3, 1, 1, 1)
        self.opt_dont_normalize = QtWidgets.QCheckBox(Dialog)
        self.opt_dont_normalize.setObjectName("opt_dont_normalize")
        self.gridLayout.addWidget(self.opt_dont_normalize, 4, 0, 1, 1)
        self.opt_keep_aspect_ratio = QtWidgets.QCheckBox(Dialog)
        self.opt_keep_aspect_ratio.setObjectName("opt_keep_aspect_ratio")
        self.gridLayout.addWidget(self.opt_keep_aspect_ratio, 5, 0, 1, 1)
        self.opt_dont_sharpen = QtWidgets.QCheckBox(Dialog)
        self.opt_dont_sharpen.setObjectName("opt_dont_sharpen")
        self.gridLayout.addWidget(self.opt_dont_sharpen, 6, 0, 1, 1)
        self.opt_landscape = QtWidgets.QCheckBox(Dialog)
        self.opt_landscape.setObjectName("opt_landscape")
        self.gridLayout.addWidget(self.opt_landscape, 9, 0, 1, 1)
        self.opt_no_sort = QtWidgets.QCheckBox(Dialog)
        self.opt_no_sort.setObjectName("opt_no_sort")
        self.gridLayout.addWidget(self.opt_no_sort, 11, 0, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 13, 1, 1, 1)
        self.opt_right2left = QtWidgets.QCheckBox(Dialog)
        self.opt_right2left.setObjectName("opt_right2left")
        self.gridLayout.addWidget(self.opt_right2left, 10, 0, 1, 1)
        self.opt_despeckle = QtWidgets.QCheckBox(Dialog)
        self.opt_despeckle.setObjectName("opt_despeckle")
        self.gridLayout.addWidget(self.opt_despeckle, 12, 0, 1, 1)
        self.opt_wide = QtWidgets.QCheckBox(Dialog)
        self.opt_wide.setObjectName("opt_wide")
        self.gridLayout.addWidget(self.opt_wide, 8, 0, 1, 1)
        self.opt_disable_trim = QtWidgets.QCheckBox(Dialog)
        self.opt_disable_trim.setObjectName("opt_disable_trim")
        self.gridLayout.addWidget(self.opt_disable_trim, 7, 0, 1, 1)
        self.title_label.setBuddy(self.opt_title)
        self.author_label.setBuddy(self.opt_author)
        self.label_3.setBuddy(self.opt_colors)
        self.label_4.setBuddy(self.opt_profile)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):

        Dialog.setWindowTitle(_("Dialog"))
        self.title_label.setText(_("&Title:"))
        self.author_label.setText(_("&Author(s):"))
        self.label_3.setText(_("&Number of colors:"))
        self.label_4.setText(_("&Profile:"))
        self.opt_dont_normalize.setText(_("Disable &normalize"))
        self.opt_keep_aspect_ratio.setText(_("Keep &aspect ratio"))
        self.opt_dont_sharpen.setText(_("Disable &sharpening"))
        self.opt_landscape.setText(_("&Landscape"))
        self.opt_no_sort.setText(_("Don\'t so&rt"))
        self.opt_right2left.setText(_("&Right to left"))
        self.opt_despeckle.setText(_("De&speckle"))
        self.opt_wide.setText(_("&Wide"))
        self.opt_disable_trim.setText(_("Disable &trimming"))

from calibre.gui2.widgets import EnLineEdit


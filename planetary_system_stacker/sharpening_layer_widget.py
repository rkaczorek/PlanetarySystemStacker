# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sharpening_layer_widget.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_sharpening_layer_widget(object):
    def setupUi(self, sharpening_layer_widget):
        sharpening_layer_widget.setObjectName("sharpening_layer_widget")
        sharpening_layer_widget.resize(340, 130)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(sharpening_layer_widget.sizePolicy().hasHeightForWidth())
        sharpening_layer_widget.setSizePolicy(sizePolicy)
        self.verticalLayout = QtWidgets.QVBoxLayout(sharpening_layer_widget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox_layer = QtWidgets.QGroupBox(sharpening_layer_widget)
        self.groupBox_layer.setObjectName("groupBox_layer")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_layer)
        self.gridLayout.setHorizontalSpacing(12)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalSlider_amount = QtWidgets.QSlider(self.groupBox_layer)
        self.horizontalSlider_amount.setMaximum(100)
        self.horizontalSlider_amount.setPageStep(1)
        self.horizontalSlider_amount.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_amount.setObjectName("horizontalSlider_amount")
        self.gridLayout.addWidget(self.horizontalSlider_amount, 1, 1, 1, 1)
        self.lineEdit_amount = QtWidgets.QLineEdit(self.groupBox_layer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_amount.sizePolicy().hasHeightForWidth())
        self.lineEdit_amount.setSizePolicy(sizePolicy)
        self.lineEdit_amount.setMinimumSize(QtCore.QSize(60, 0))
        self.lineEdit_amount.setMaximumSize(QtCore.QSize(60, 16777215))
        self.lineEdit_amount.setObjectName("lineEdit_amount")
        self.gridLayout.addWidget(self.lineEdit_amount, 1, 2, 1, 1)
        self.horizontalSlider_radius = QtWidgets.QSlider(self.groupBox_layer)
        self.horizontalSlider_radius.setMinimum(1)
        self.horizontalSlider_radius.setMaximum(100)
        self.horizontalSlider_radius.setPageStep(1)
        self.horizontalSlider_radius.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_radius.setObjectName("horizontalSlider_radius")
        self.gridLayout.addWidget(self.horizontalSlider_radius, 0, 1, 1, 1)
        self.lineEdit_radius = QtWidgets.QLineEdit(self.groupBox_layer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_radius.sizePolicy().hasHeightForWidth())
        self.lineEdit_radius.setSizePolicy(sizePolicy)
        self.lineEdit_radius.setMinimumSize(QtCore.QSize(60, 0))
        self.lineEdit_radius.setMaximumSize(QtCore.QSize(60, 16777215))
        self.lineEdit_radius.setObjectName("lineEdit_radius")
        self.gridLayout.addWidget(self.lineEdit_radius, 0, 2, 1, 1)
        self.label_amount = QtWidgets.QLabel(self.groupBox_layer)
        self.label_amount.setObjectName("label_amount")
        self.gridLayout.addWidget(self.label_amount, 1, 0, 1, 1)
        self.label_radius = QtWidgets.QLabel(self.groupBox_layer)
        self.label_radius.setObjectName("label_radius")
        self.gridLayout.addWidget(self.label_radius, 0, 0, 1, 1)
        self.pushButton_remove = QtWidgets.QPushButton(self.groupBox_layer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_remove.sizePolicy().hasHeightForWidth())
        self.pushButton_remove.setSizePolicy(sizePolicy)
        self.pushButton_remove.setMinimumSize(QtCore.QSize(60, 0))
        self.pushButton_remove.setMaximumSize(QtCore.QSize(60, 16777215))
        self.pushButton_remove.setObjectName("pushButton_remove")
        self.gridLayout.addWidget(self.pushButton_remove, 2, 2, 1, 1)
        self.checkBox_luminance = QtWidgets.QCheckBox(self.groupBox_layer)
        self.checkBox_luminance.setObjectName("checkBox_luminance")
        self.gridLayout.addWidget(self.checkBox_luminance, 2, 0, 1, 2)
        self.gridLayout.setColumnStretch(1, 1)
        self.gridLayout.setRowStretch(1, 1)
        self.verticalLayout.addWidget(self.groupBox_layer)

        self.retranslateUi(sharpening_layer_widget)
        QtCore.QMetaObject.connectSlotsByName(sharpening_layer_widget)

    def retranslateUi(self, sharpening_layer_widget):
        _translate = QtCore.QCoreApplication.translate
        sharpening_layer_widget.setWindowTitle(_translate("sharpening_layer_widget", "Form"))
        self.groupBox_layer.setTitle(_translate("sharpening_layer_widget", "Layer 1"))
        self.horizontalSlider_amount.setToolTip(_translate("sharpening_layer_widget", "Increase / decrease the effect of this layer"))
        self.lineEdit_amount.setToolTip(_translate("sharpening_layer_widget", "Relative effect of this layer"))
        self.horizontalSlider_radius.setToolTip(_translate("sharpening_layer_widget", "Change the radius of Gauss filter for this layer"))
        self.lineEdit_radius.setToolTip(_translate("sharpening_layer_widget", "Radius of Gauss filter"))
        self.label_amount.setText(_translate("sharpening_layer_widget", "Amount"))
        self.label_radius.setText(_translate("sharpening_layer_widget", "Radius"))
        self.pushButton_remove.setToolTip(_translate("sharpening_layer_widget", "Remove this layer"))
        self.pushButton_remove.setText(_translate("sharpening_layer_widget", "Remove"))
        self.checkBox_luminance.setToolTip(_translate("sharpening_layer_widget", "Apply sharpening only to luminance channel"))
        self.checkBox_luminance.setText(_translate("sharpening_layer_widget", "Luminance channel only"))


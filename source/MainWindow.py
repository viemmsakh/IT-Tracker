# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
	def setupUi(self, MainWindow):
		MainWindow.setObjectName("MainWindow")
		MainWindow.resize(530, 175)
		MainWindow.setMinimumSize(QtCore.QSize(530, 175))
		MainWindow.setMaximumSize(QtCore.QSize(530, 175))
		font = QtGui.QFont()
		font.setFamily("Courier")
		MainWindow.setFont(font)
		
		
		# Location Dropdown
		self.comboOffice = QtWidgets.QComboBox(MainWindow)
		self.comboOffice.setGeometry(QtCore.QRect(170, 10, 350, 27))
		self.comboOffice.setObjectName("comboOffice")
		
		# Locator Table
		self.tableLocator = QtWidgets.QTableWidget(MainWindow)
		self.tableLocator.setGeometry(QtCore.QRect(10, 50, 510, 114))
		self.tableLocator.setObjectName("tableLocator")
		self.tableLocator.setColumnCount(3)
		self.tableLocator.setRowCount(3)
		
		# Table Column Width
		self.tableLocator.setColumnWidth(0,90)
		self.tableLocator.setColumnWidth(1,313)
		self.tableLocator.setColumnWidth(2,90)
		
		# Table Font Settings
		font = QtGui.QFont()
		font.setFamily("Courier")
		font.setPointSize(8)
		
		item = QtWidgets.QTableWidgetItem()
		item.setFont(font)
		self.tableLocator.setVerticalHeaderItem(0, item)
		
		item = QtWidgets.QTableWidgetItem()
		item.setFont(font)
		self.tableLocator.setVerticalHeaderItem(1, item)
		
		item = QtWidgets.QTableWidgetItem()
		item.setFont(font)
		self.tableLocator.setVerticalHeaderItem(2, item)
		
		item = QtWidgets.QTableWidgetItem()
		item.setFont(font)
		self.tableLocator.setHorizontalHeaderItem(0, item)
		
		item = QtWidgets.QTableWidgetItem()
		item.setFont(font)
		self.tableLocator.setHorizontalHeaderItem(1, item)
		
		item = QtWidgets.QTableWidgetItem()
		item.setFont(font)
		self.tableLocator.setHorizontalHeaderItem(2, item)
		
		
		# Username Textarea
		self.textUsername = QtWidgets.QTextEdit(MainWindow)
		self.textUsername.setGeometry(QtCore.QRect(10, 10, 141, 27))
		font = QtGui.QFont()
		font.setFamily("Courier")
		font.setPointSize(12)
		self.textUsername.setFont(font)
		self.textUsername.setReadOnly(True)
		self.textUsername.setObjectName("textUsername")

		self.retranslateUi(MainWindow)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)

	def retranslateUi(self, MainWindow):
		_translate = QtCore.QCoreApplication.translate
		MainWindow.setWindowTitle(_translate("MainWindow", "IT Locator"))
		item = self.tableLocator.verticalHeaderItem(0)
		item.setText(_translate("MainWindow", "1"))
		item = self.tableLocator.verticalHeaderItem(1)
		item.setText(_translate("MainWindow", "2"))
		item = self.tableLocator.verticalHeaderItem(2)
		item.setText(_translate("MainWindow", "3"))
		item = self.tableLocator.horizontalHeaderItem(0)
		item.setText(_translate("MainWindow", "Username"))
		item = self.tableLocator.horizontalHeaderItem(1)
		item.setText(_translate("MainWindow", "Location"))
		item = self.tableLocator.horizontalHeaderItem(2)
		item.setText(_translate("MainWindow", "Duration"))
		self.textUsername.setHtml(_translate("MainWindow", ""))


if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	MainWindow = QtWidgets.QWidget()
	ui = Ui_MainWindow()
	ui.setupUi(MainWindow)
	MainWindow.show()
	sys.exit(app.exec_())


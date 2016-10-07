# Imports

import datetime, time
import math
import os
import sqlite3

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from MainWindow import Ui_MainWindow

# Use this for browsing database: https://github.com/sqlitebrowser/sqlitebrowser/releases

class MainWindow(Ui_MainWindow):
	def __init__(self, app_MainWindow):
		Ui_MainWindow.__init__(self)
		self.setupUi(app_MainWindow)
		
		# Font
		self.font = QtGui.QFont()
		self.font.setFamily("Courier")
		self.font.setPointSize(8)
		
		# Set Username
		self.username = os.getlogin()
		_translate = QtCore.QCoreApplication.translate
		self.textUsername.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Courier\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\';\">" + self.username + "</span></p></body></html>"))
		
		# Populate table before 1 second
		self.update_db()
		
		# Update DB/form on 1 second timer
		self.timer = QTimer()
		self.timer.timeout.connect(self.update_db)
		self.timer.start(1000)
		
		# Connect dropdown change to update_db
		self.comboOffice.currentIndexChanged.connect(self.update_db)
		
		# Connect quit in menubar to clean_quit
		self.actionCleanQuit.triggered.connect(self.clean_quit)
		
	def clean_quit(self):
		c.execute("""DELETE FROM tracker WHERE username = ?""", (self.username,))
		conn.commit()
		c.close()
		conn.close()
		quit()
	
	def update_db(self):
		ts = time.time()
		# Update Location dropdown
		# This isn't necessary after first load. And most
		# likey new locations will not be added; however,
		# if the sqlite db is updated with more locations,
		# the locations will auto-populate.
		# Also, it would probably be better to just use
		# configparser to store the locations.
		
		c.execute("""SELECT * from locations""")
		locations = c.fetchall()
		for row in locations:
			location = row[0]
			self.comboOffice.addItem(location)
		self.location = self.comboOffice.currentText()
		
		c.execute("""SELECT * from tracker WHERE username = ?""", (self.username,))
		check = c.fetchone()
		if not check or len(check) == 0:
			c.execute("""INSERT INTO tracker VALUES(?,?,?)""", (self.username, self.location, ts))
		else:
			if not self.location == check[1]:
				# Self.Location is different than what is in the db
				c.execute("""UPDATE tracker SET location = ?,  ts = ? WHERE username = ?""", (self.location, ts, self.username))
		conn.commit()

		c.execute("""SELECT * from tracker""")
		ittracker = c.fetchall()
		i = 0
		self.tableLocator.setRowCount(len(ittracker))
		for row in ittracker:
			username = QtWidgets.QTableWidgetItem(str(row[0]))
			username.setFont(self.font)
			self.tableLocator.setItem(i, 0, username)

			location = QtWidgets.QTableWidgetItem(str(row[1]))
			location.setFont(self.font)
			self.tableLocator.setItem(i, 1, location)
			
			ts1 = float(row[2])
			duration = datetime.datetime.fromtimestamp(time.time()) - datetime.datetime.fromtimestamp(ts1)
			diff = duration.seconds
			if diff < 60:
				msg = "%ss" % diff
			else:
				msg = "%sm %ss" % (str(math.floor(diff) / 60).split(".")[0], diff % 60)
			
			item = QtWidgets.QTableWidgetItem(str(msg))
			item.setFont(self.font)
			item.setTextAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignCenter)
			self.tableLocator.setItem(i, 2, item)
			i += 1

		
if __name__ == '__main__':
	conn = sqlite3.connect('ittracker.db')
	c = conn.cursor()
	
	c.execute("""CREATE TABLE IF NOT EXISTS locations(location TEXT, id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT)""")
	c.execute("""SELECT * FROM locations""")
	if len(c.fetchall()) == 0:
		# Create Locations
		locations = [
			{"location": "Computer Information Systems"},
			{"location": "Adult Probation"},
			{"location": "Building & Zoning"},
			{"location": "Circuit Court"},
			{"location": "CIR. CT. Family Division"},
			{"location": "CIR. CT. Friend of the Court"},
			{"location": "CIR. CT. Juvenile Division"},
			{"location": "Clerk"},
			{"location": "Commissioners"},
			{"location": "Corporation Counsel"},
			{"location": "District Court"},
			{"location": "DIST. CT. Magistrate Court"},
			{"location": "DIST. CT. Probation Office"},
			{"location": "DIST. CT. Community Corrections"},
			{"location": "Economic Development Corp."},
			{"location": "Equalization"},
			{"location": "Maintenance"},
			{"location": "Probate Court"},
			{"location": "Prosecuting Attorney"},
			{"location": "Public Guardian"},
			{"location": "Register of Deeds"},
			{"location": "Social Security"},
			{"location": "Tax Mapping / GIS"},
			{"location": "Treasurer"},
			{"location": "Veteran's"},
			{"location": "Sheriff Department"},
			{"location": "SD. Administrative"},
			{"location": "SD. Booking"},
			{"location": "SD. Garage"},
			{"location": "SD. Records"},
			{"location": "SD. Squadroom"},
			{"location": "SD. Substation - West"},
			{"location": "SD. Substation - East"},
		]
		for location in locations:
			c.execute("""INSERT INTO locations (location) VALUES(?)""", (location['location'],))
	c.execute("""CREATE TABLE IF NOT EXISTS tracker(username TEXT NOT NULL, location TEXT NOT NULL, ts TEXT NOT NULL)""")
	conn.commit()
	
	import sys
	app = QtWidgets.QApplication(sys.argv)

	widget_MainWindow = QtWidgets.QMainWindow()
	widget_MainWindow.setWindowFlags(QtCore.Qt.WindowSystemMenuHint | QtCore.Qt.WindowMinimizeButtonHint)
	app_MainWindow = MainWindow(widget_MainWindow)
	
	widget_MainWindow.show()
	
	sys.exit(app.exec_())
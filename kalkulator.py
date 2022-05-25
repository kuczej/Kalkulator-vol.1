#!/usr/bin/env python3

# coding: utf-8
import sys
from PyQt4 import QtCore, QtGui
from projekt import Ui_Form
from math import * # importuję wszystkie funkcje z biblioteki math
def silnia(n):

	"""

	Funkcja oblicza silnię wykorzystując do tego celu pętlę iteracyjną

	"""

	if n == 0:

		return 1

	elif n < 0:

		return None

	wynik = 1

	for i in range(2, n + 1): # generator od 2 do n

		wynik *= i

	return wynik
class MyForm(QtGui.QMainWindow):

	def __init__(self, parent=None):

		QtGui.QWidget.__init__(self, parent)

		self.ui = Ui_Form()

		self.ui.setupUi(self)

		self.setWindowTitle("Kalkulator 1.0")

		self.setWindowOpacity(0.8)

		QtCore.QObject.connect(self.ui.Calculate,QtCore.SIGNAL("clicked()"), self.calculate_value)

		QtCore.QObject.connect(self.ui.writeText,QtCore.SIGNAL("returnPressed()"), self.calculate_value)

		

	def calc_text(self, errortext, calcText):

		if calcText == "":

			self.ui.wynik.setPlainText(self.ui.writeText.text() + " = " + errortext)

		else:

			self.ui.wynik.setPlainText(self.ui.writeText.text() + " = " + errortext + "n" + calcText)

		

	def calculate_value(self):

		calcText = self.ui.wynik.toPlainText() # pobieranie tekstu zawartego w kontrolce wynik

		

		try:

			exp = eval(self.ui.writeText.text())

			self.calc_text(str(exp), calcText)

		except ZeroDivisionError as e:

			self.calc_text('Dzielisz przez zero ({0})'.format(e), calcText)

		except NameError as e:

			self.calc_text('Nieznana zmienna ({0})'.format(e), calcText)

		except TypeError as e:

			self.calc_text('Błąd typu danych lub deklaracji zmiennej ({0})'.format(e), calcText)

		except:

			self.calc_text('Błąd składni',calcText)

		

		self.ui.writeText.setText("") # ustawianie tekstu w kontrolce writeText

		self.ui.writeText.setFocus(True) # przypisanie fokusa kontrolce writeText

if __name__ == "__main__":

	app = QtGui.QApplication(sys.argv)

	myapp = MyForm()

	myapp.show()

	sys.exit(app.exec_())

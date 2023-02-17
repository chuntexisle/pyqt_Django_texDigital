import sys
import requests
import json
#import urllib2

from PyQt5.QtWidgets import (
    QApplication, QDialog, QMainWindow, QMessageBox
)
from PyQt5.uic import loadUi

from ui_form import Ui_Form

class Window(QMainWindow, Ui_Form):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.jdata  = self.get_data()
        self.jdata2 = self.get_data2()

        self.pushButton.clicked.connect(self.set_data)

    def set_data(self):
        try:
            url = str("http://127.0.0.1:8000/lots/all/20110")
            self.jdata['feet']=float(self.lineEdit_29.text())
            print('feet value is ', self.jdata['feet'])
            print(self.jdata)
            r = requests.post(url=url, json=self.jdata)
            print('r is ', r)
            
            url2 = str("http://127.0.0.1:8000/processing/all/9200")
            print('update the form to database')
        except Exception as ex:
            print('Error: ' + str(ex))


    def get_data(self):
        django_data = {}
        try:
            url = str("http://127.0.0.1:8000/lots/all/20110")
            response = requests.get(url=url)
            django_data = response.json()
            
            print(django_data)
            
            self.lineEdit_11.setText(str(django_data['lot_number']))
            self.lineEdit_17.setText(str(django_data['qty_uv_coated']))
            self.lineEdit_24.setText(str(django_data['qty_nouv_coating']))
            self.lineEdit_29.setText(str(django_data['feet']))
            self.lineEdit_35.setText(str(django_data['tons']))
        except Exception as ex:
            print('Error: ' + str(ex))
        return django_data

    def get_data2(self):
        django_data2={}
        try:
            url2 = str("http://127.0.0.1:8000/processing/all/9200")
            response2 = requests.get(url=url2)
            django_data2 = response2.json()
            print(django_data2)

            self.textEdit.setText(str(django_data2['date']))
            self.lineEdit.setText(str(django_data2['tds_transaction_id']))
            self.comboBox.setCurrentText(str(django_data2['customer']))

            self.comboBox_2.setCurrentText(str(django_data2['gt_pipo_po']))
            self.comboBox_3.setCurrentText(str(django_data2['processing_order']))
            self.comboBox_4.setCurrentText(str(django_data2['wonumber']))

            self.lineEdit_4.setText(str(django_data2['od']))
            self.lineEdit_5.setText(str(django_data2['wall']))
            self.lineEdit_6.setText(str(django_data2['weight_per_ft']))
            self.lineEdit_7.setText(str(django_data2['grade']))
            
            self.lineEdit_8.setText(str(django_data2['design']))
            self.lineEdit_9.setText(str(django_data2['manufacturer']))
            self.lineEdit_10.setText(str(django_data2['avg_length']))

            self.lineEdit_37.setText(str(django_data2['totalqty_uv_coated']))
            self.lineEdit_38.setText(str(django_data2['totalqty_nouv_coating']))
            self.lineEdit_39.setText(str(django_data2['totalfeet']))
            self.lineEdit_36.setText(str(django_data2['totaltons']))


        except Exception as ex:
            print('Error: ' + str(ex))
        return django_data2

    def about(self):
        QMessageBox.about(
            self,
            "About Sample Editor",
            "<p>A sample text editor app built with:</p>"
            "<p>- PyQt</p>"
            "<p>- Qt Designer</p>"
            "<p>- Python</p>",
        )

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    #win.label.setText("Hello")
    win.show()
    #win.get_data()
    sys.exit(app.exec())

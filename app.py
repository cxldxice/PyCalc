import sys
import time
import threading
import win32gui
import subprocess

import keyboard
import PySide6
from PySide6.QtCore import QFile
from PySide6.QtWidgets import QApplication, QDialog

from ui import Ui_Dialog


def clear():
    ui.label.setText("")

def add(sym):
    text = ui.label.text()

    ui.label.setText(f"{text}{sym}".replace("ERROR", ""))

def equal():
    text = ui.label.text().replace("×", "*").replace("÷", "/")

    try:
        ui.label.setText(str(eval(text)))
    except:
        ui.label.setText("ERROR")

def copy2clip(txt):
    cmd='echo '+txt.strip()+'|clip'
    return subprocess.check_call(cmd, shell=True)

def copy_bar():
    text = ui.label.text()

    copy2clip(text)


def key_thread():
    def hook(event):
        if "PyCalc" in win32gui.GetWindowText(win32gui.GetForegroundWindow()):
            if event.event_type == "down":
                if event.name in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "+", "-", "%", "."]:
                    add(event.name)

                elif event.name == "=":
                    equal()

                elif event.name == "c":
                    clear()

                elif event.name in ["/", "*"]:
                    add(event.name.replace("*", "×").replace("/", "÷"))


    keyboard.hook(hook)
    keyboard.wait()
    

if __name__ == "__main__":
    app = QApplication(sys.argv)

    #init dialog window
    window = QDialog()
    ui = Ui_Dialog()
    ui.setupUi(window)
    window.show()

    #button onclick
    ui.pushButton.clicked.connect(lambda: add(1))
    ui.pushButton_2.clicked.connect(lambda: add(2))
    ui.pushButton_3.clicked.connect(lambda: add(3))
    ui.pushButton_4.clicked.connect(lambda: add("+"))
    ui.pushButton_5.clicked.connect(lambda: add(4))
    ui.pushButton_6.clicked.connect(lambda: add(5))
    ui.pushButton_7.clicked.connect(lambda: add(6))
    ui.pushButton_8.clicked.connect(lambda: add("-"))
    ui.pushButton_9.clicked.connect(lambda: add(7))
    ui.pushButton_10.clicked.connect(lambda: add(8))
    ui.pushButton_11.clicked.connect(lambda: add(9))
    ui.pushButton_12.clicked.connect(lambda: add("×"))
    ui.pushButton_14.clicked.connect(lambda: add(0))
    ui.pushButton_15.clicked.connect(lambda: add("%"))
    ui.pushButton_16.clicked.connect(lambda: add("÷"))
    ui.pushButton_18.clicked.connect(equal)
    ui.pushButton_20.clicked.connect(clear)
    ui.pushButton_21.clicked.connect(lambda: add("."))

    #keyboard thread
    th = threading.Thread(target=key_thread)
    th.setDaemon(True)
    th.start()

    
    sys.exit(app.exec())
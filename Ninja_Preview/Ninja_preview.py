# -*- coding: utf-8 -*-
import sys
import os
from base64 import b64decode
from PyQt5.QtCore import QCoreApplication, QSettings, QResource
from PyQt5.QtGui import QGuiApplication, QIcon
from PyQt5.QtQml import QQmlApplicationEngine
from Ninja_Preview.preview import Preview
from Ninja_Preview._ninjapreview_resource import rcc


def dummy_run():
    pass

def cleanUp():
    if os.path.exists('_ninjapreview_resource.rcc'):
        os.remove('_ninjapreview_resource.rcc')

dec = b64decode(rcc)

with open('_ninjapreview_resource.rcc', 'wb') as rcc_f:
    rcc_f.write(dec)

QResource.registerResource("_ninjapreview_resource.rcc")

qApp = QGuiApplication(sys.argv)

QCoreApplication.setOrganizationName("Deuteronomy Works")
QCoreApplication.setApplicationName("Ninja-Preview")
settings = QSettings()

qApp.setWindowIcon(QIcon(":icons/logo.png"))
qApp.aboutToQuit.connect(cleanUp)

engine = QQmlApplicationEngine()

preview = Preview()

engine.load("qrc:///UI/main.qml")
engine.rootObjects()[0].setProperty('preview', preview)
engine.quit.connect(qApp.quit)

sys.exit(qApp.exec_())

__version__ = '0.0.1-dev'

import os, sys

from PySide2.QtCore import QObject, QUrl
from PySide2.QtQml import qmlRegisterType
from PySide2.QtWidgets import QApplication, QWidget
from PySide2.QtQuick import QQuickView, QQuickPaintedItem
from PySide2.QtGui import QIcon



def main():
  app = QApplication([])
  app.setApplicationName("PySnapShot")

  # setup the QML UI
  view = QQuickView()
  view.setResizeMode(QQuickView.SizeRootObjectToView)
  context = view.rootContext()
  filepath = os.path.dirname(os.path.realpath(__file__))
  view.setSource(QUrl.fromLocalFile(os.path.join(filepath,"data", "main.qml")))
  view.resize(640, 480)
  view.show()
  app.exec_()


if __name__ == "__main__":
  main()

    



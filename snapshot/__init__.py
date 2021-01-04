__version__ = '0.0.1-dev'


import os, sys

from PySide2.QtCore import QObject, QUrl
from PySide2.QtQml import qmlRegisterType, QQmlApplicationEngine
from PySide2.QtWidgets import QApplication, QWidget
from PySide2.QtQuick import QQuickView, QQuickPaintedItem
from PySide2.QtGui import QIcon



from model import PhotoModel
from view_item import PhotoViewItem

def main():
  sys.argv += ["--style", "material"]
  app = QApplication(sys.argv)
  app.setApplicationName("PySnapShot")

  photo_model = PhotoModel(os.path.join("test_data"))

  # setup the QML 
  engine = QQmlApplicationEngine()
  context = engine.rootContext()
  #view = QQuickView()
  #view.setResizeMode(QQuickView.SizeRootObjectToView)
  #context = view.rootContext()
  context.setContextProperty("photoModel", photo_model)
  filepath = os.path.dirname(os.path.realpath(__file__))
  #view.setSource(QUrl.fromLocalFile(os.path.join(filepath,"data", "main.qml")))
  #view.resize(640, 480)
  #view.show()
  engine.load(QUrl.fromLocalFile(os.path.join(filepath,"data", "MainWindow.qml")))
  app.exec_()


if __name__ == "__main__":
  main()

    



import QtQuick 2.12

Text 
{
  text: "Hello Wolrd" + photoModel.currentFileName
  y: 30
  anchors.centerIn: parent
  font.pointSize: 24; font.bold: true
}
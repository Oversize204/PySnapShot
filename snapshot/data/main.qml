import QtQuick 2.0

Rectangle {
    id: page
    width: 320; height: 480
    color: "red"

    Text {
        id: helloText
        text: "Test 1 2 3"
        y: 30
        anchors.horizontalCenter: page.horizontalCenter
        font.pointSize: 24; font.bold: true
    }
}
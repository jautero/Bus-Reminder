import QtQuick 1.1
import com.meego 1.0
import com.nokia.extras 1.1

Page {
    id: mainPage
    tools: commonTools
     {
        id: label
        anchors.centerIn: parent
        text: qsTr("Hello world!")
        visible: false
    }
}

InfoBanner {
	id: businfo
	text: "Next buses are 18:05/12 18:17/247A 18:30/36B"
}

from PyQt5.QtWidgets import QGridLayout , QWidget, QLabel
from PyQt5.QtCore import Qt, QPoint, QLineF
from PyQt5.QtGui import QPainter, QColor, QCursor, QTransform
import math
import settings
import plugin

class UI(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowFlags(Qt.FramelessWindowHint | Qt.Tool|       Qt.WindowStaysOnTopHint)  
        self.setAttribute(Qt.WA_TranslucentBackground) 

        self.setGeometry(100, 100, round(300 * settings._UI_RADIUS), round(300 * settings._UI_RADIUS))
        self.radius = min(self.width(),self. height()) / 2
        self.setWindowTitle('Round Transparent Window')
        self.segments = []
        for i in range(settings._PLUGIN_ARRAY_SIZE):
            angle = i * 360 / settings._PLUGIN_ARRAY_SIZE
            segment_center =  QPoint(int(settings._UI_RADIUS * 30 * math.cos(angle * math.pi / 180)),
                                                        int(settings._UI_RADIUS * 30 * math.sin(angle * math.pi / 180)))
            self.segments.append(segment_center)

        center = QPoint(round(self.width() /2)  ,round(self.height()/2 ) )
        self.labels = []
        for i, plug in enumerate(plugin.plugins):
            
            if(plug == None):
                continue
            angle = i * 360 / settings._PLUGIN_ARRAY_SIZE
            rotOffset =  QPoint(int(settings._UI_RADIUS * 117 * math.cos(angle * math.pi / 180)),
                                                        int(settings._UI_RADIUS * 117 * math.sin(angle * math.pi / 180)))

            
            label = QLabel( plug.contextElementName,self)
            label.setGeometry(0,0,110,70)
            label.setWordWrap(True)
            label.move(center+rotOffset -  QPoint(int(label.width()/2),int(label.height()/2)))
            label.color = QColor(255,255,255)
            label.setAlignment(Qt.AlignHCenter| Qt.AlignVCenter)
            label.setStyleSheet("""
QWidget {
font-family: sans-serif;
font-size: 18px;
line-height: 1.5;
color: #fff;
}

QLabel, QLineEdit, QPushButton, QTextEdit, QListWidgetItem, QTreeWidgetItem {
}

QLabel {
.drop-shadow;
}

QLabel:first-of-type, QLabel:only-child {
font-weight: bold;
}

QPushButton, QLabel.QPushButton, QLink {
text-decoration: none;
color: #007bff;
.drop-shadow;
}

QPushButton:hover, QLabel.QPushButton:hover, QLink:hover {
text-shadow: 0 1px 5px rgba(0, 0, 0, 0.2);
}
""")
            self.labels.append(label)
    def paintEvent(self, event):


        painter = QPainter(self)
        
        painter.setRenderHint(QPainter.Antialiasing)

        _BG_COLOR = settings._BG_COLOR
        painter.setBrush(QColor(_BG_COLOR[0], _BG_COLOR[1], _BG_COLOR[2], _BG_COLOR[3]))  



        radius = min(self.width(), self.height()) / 2
        painter.drawEllipse(self.rect().center(), radius, radius)
        painter.drawEllipse(self.rect().center(), 100, 100)

    def showEvent(self, event):
        cursor_pos = QCursor.pos()
        self.setGeometry(
            int(cursor_pos.x() - self.width() / 2),
            int(cursor_pos.y() - self.height() / 2),
            self.width(),
            self.height()
        )

        self.center = QPoint(round(self.x()+self.width()/2 ),round(self.y() + self.height()/2 ))


    def hideEvent(self, event):
        mouse_pos = QCursor.pos()



        closest_segment_index = 0
        closest_distance = float('inf')
        for i, segment in enumerate(self.segments):
            
            distance =  math.dist([mouse_pos.x(),mouse_pos.y()],[ segment.x() + self.center.x(), segment.y()+self.center.y()])
            
            if distance < closest_distance:
                closest_segment_index = i
                closest_distance = distance
        if(math.dist([mouse_pos.x(),mouse_pos.y()],[ self.center.x(), self.center.y()]) > 100 ):
            plugin.ExecutePlugin(closest_segment_index)
import sys
import math
from PyQt5.QtCore import Qt, QTimer, QTime, QPoint
from PyQt5.QtGui import QPainter, QPen, QColor
from PyQt5.QtWidgets import QApplication, QWidget

class TransparentClock(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt Transparent Clock")
        self.resize(600, 600)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update)
        self.timer.start(1000)

        self.drag_position = None

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        center = QPoint(self.width() // 2, self.height() // 2)
        radius = min(self.width(), self.height()) // 2 - 10

        # 畫錶面
        painter.setPen(Qt.NoPen)
        painter.setBrush(QColor(0, 0, 0, 180))  # 半透明黑色
        painter.drawEllipse(center, radius, radius)

        # 畫刻度
        painter.setPen(QPen(Qt.white, 2))
        for i in range(12):
            angle = math.radians(i * 30)
            x1 = center.x() + radius * 0.85 * math.cos(angle)
            y1 = center.y() + radius * 0.85 * math.sin(angle)
            x2 = center.x() + radius * 0.95 * math.cos(angle)
            y2 = center.y() + radius * 0.95 * math.sin(angle)
            painter.drawLine(QPoint(int(x1), int(y1)), QPoint(int(x2), int(y2)))

        # 畫指針
        time = QTime.currentTime()
        self.draw_hand(painter, center, time.hour() % 12 * 30 + time.minute() * 0.5, radius * 0.5, 6, Qt.white)
        self.draw_hand(painter, center, time.minute() * 6, radius * 0.7, 4, Qt.cyan)
        self.draw_hand(painter, center, time.second() * 6, radius * 0.9, 2, Qt.red)

        # 畫中心點
        painter.setBrush(Qt.white)
        painter.drawEllipse(center, 5, 5)

    def draw_hand(self, painter, center, angle_deg, length, width, color):
        angle_rad = math.radians(angle_deg - 90)
        x = center.x() + length * math.cos(angle_rad)
        y = center.y() + length * math.sin(angle_rad)
        painter.setPen(QPen(color, width))
        painter.drawLine(center, QPoint(int(x), int(y)))

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drag_position = event.globalPos() - self.frameGeometry().topLeft()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton and self.drag_position:
            self.move(event.globalPos() - self.drag_position)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    clock = TransparentClock()
    clock.show()
    sys.exit(app.exec_())
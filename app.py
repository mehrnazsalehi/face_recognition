import sys
from PyQt5.QtWidgets import QLabel, QPushButton, QFileDialog
from PyQt5.QtWidgets import *
from PyQt5 import uic
from utils.detector import Detector
from utils.video import Video


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        uic.loadUi("face-recognition.ui", self)

        # Define our widgets

        self.label_title = self.findChild(QLabel, "label_title")
        self.label = self.findChild(QLabel, "label")
        self.openButton = self.findChild(QPushButton, "openButton")

        self.openButton.clicked.connect(self.open_files)

        self.show()

    def open_files(self):
        video = QFileDialog.getOpenFileName(self, "Open File", "C:\\Users\pc-5\\PycharmProjects\\face-recognition\\files", "Video Files (*.avi  *.mp4)")
        video_address = video[0]
        detector = Detector("files/face.xml")

        for frame in Video(video_address):
            frame.draw_rectangle(detector.get_coordinates(frame.gray_scale()))
            frame.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())
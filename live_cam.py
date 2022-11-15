from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout
from PyQt5.QtGui import QPixmap
#import sys
import cv2
from PyQt5.QtCore import pyqtSignal, pyqtSlot, Qt, QThread
import numpy as np


class VideoThread(QThread):
    change_pixmap_signal = pyqtSignal(np.ndarray)

    def __init__(self):
        super().__init__()
        self._run_flag = True

    def run(self):
        # capture from web cam
        cap = cv2.VideoCapture(0)
        cascPath = "haarcascade_frontalface_default.xml"
        # Create the haar cascade
        faceCascade = cv2.CascadeClassifier(cascPath)

        while self._run_flag:
            # Capture frame-by-frame
            ret, frame = cap.read()
            # Our operations on the frame come here
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            # Detect faces in the image
            faces = faceCascade.detectMultiScale(
                gray,
                scaleFactor=1.1,
                minNeighbors=5,
                minSize=(30, 30)
                #flags = cv2.CV_HAAR_SCALE_IMAGE
            )
            print("Found {0} faces!".format(len(faces)))
            # Draw a rectangle around the faces
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            if ret:
                self.change_pixmap_signal.emit(frame)

        # shut down capture system
        cap.release()

    def stop(self):
        """Sets run flag to False and waits for thread to finish"""
        self._run_flag = False
        self.wait()


class live_cam(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        #self.setWindowFlag(QtCore.Qt.WindowCloseButtonHint, False)
        #self.setWindowFlag(QtCore.Qt.WindowMinimizeButtonHint, False)
        #self.setWindowFlag(QtCore.Qt.WindowMaximizeButtonHint, False)
        self.setWindowTitle("Qt live label demo")
        self.disply_width = 640
        self.display_height = 480
        # create the label that holds the image
        self.image_label = QLabel(self)
        self.image_label.resize(self.disply_width, self.display_height)
        # create a text label
        self.btn_cerrar_cam = QPushButton('Cerrar Cámara')

        # create a vertical box layout and add the two labels
        vbox = QVBoxLayout()
        vbox.addWidget(self.image_label)
        vbox.addWidget(self.btn_cerrar_cam)
        
        # set the vbox layout as the widgets layout
        self.setLayout(vbox)

        # create the video capture thread
        self.thread = VideoThread()
        # connect its signal to the update_image slot
        self.thread.change_pixmap_signal.connect(self.update_image)
        # start the thread
        self.thread.start()

        self.btn_cerrar_cam.clicked.connect(self.close_cam)

    def closeEvent(self, event):
        self.thread.stop()
        event.accept()

    def close_cam(self):
        self.close()



    @pyqtSlot(np.ndarray)
    def update_image(self, cv_img):
        """Updates the image_label with a new opencv image"""
        qt_img = self.convert_cv_qt(cv_img)
        self.image_label.setPixmap(qt_img)
    
    def convert_cv_qt(self, cv_img):
        """Convert from an opencv image to QPixmap"""
        rgb_image = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_image.shape
        bytes_per_line = ch * w
        convert_to_Qt_format = QtGui.QImage(rgb_image.data, w, h, bytes_per_line, QtGui.QImage.Format_RGB888)
        p = convert_to_Qt_format.scaled(self.disply_width, self.display_height, Qt.KeepAspectRatio)
        return QPixmap.fromImage(p)
    
#if __name__=="__main__":
#    app = QApplication(sys.argv)
#    a = App()
#    a.show()
#    sys.exit(app.exec_())

from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout
from PyQt5.QtGui import QPixmap
# import sys
import face_recognition
import cv2
import os
from PyQt5.QtCore import pyqtSignal, pyqtSlot, Qt, QThread
import numpy as np


class VideoThread(QThread):
    change_pixmap_signal = pyqtSignal(np.ndarray)

    def __init__(self):
        super().__init__()
        self._run_flag = True

    def run(self):
        # Codificar los rostros extraidos
        imageFacesPath = "images/faces"
        facesEncodings = []
        facesNames = []
        for file_name in os.listdir(imageFacesPath):
            image = cv2.imread(imageFacesPath + "/" + file_name)
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            f_coding = face_recognition.face_encodings(
                image,
                known_face_locations=[(0, 150, 150, 0)]
            )[0]
            facesEncodings.append(f_coding)
            facesNames.append(file_name.split(".")[0])
        # LEYENDO VIDEO
        # cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        # cap = cv2.VideoCapture(0, cv2.CAP_V4L2)
        cap = cv2.VideoCapture(0)
        
        # Detector facial
        faceClassif = cv2.CascadeClassifier(
            cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
        )

        while self._run_flag:
            ret, frame = cap.read()
            if ret is False:
                break
            frame = cv2.flip(frame, 1)
            orig = frame.copy()
            faces = faceClassif.detectMultiScale(
                frame,
                scaleFactor=1.1,
                minNeighbors=10,
                minSize=(30, 30)
            )

            for (x, y, w, h) in faces:
                face = orig[y:y + h, x:x + w]
                face = cv2.cvtColor(face, cv2.COLOR_BGR2RGB)
                actual_face_encoding = face_recognition.face_encodings(face, known_face_locations=[(0, w, h, 0)])[0]
                result = face_recognition.compare_faces(facesEncodings, actual_face_encoding)
                # print(result)
                if True in result:
                    index = result.index(True)
                    name = facesNames[index].split('_')[0]
                    color = (125, 220, 0)
                    cv2.rectangle(frame, (x, y + h), (x + w, y + h + 30), color, -1)
                    cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
                    cv2.putText(frame, name, (x, y + h + 25), 2, 1, (255, 255, 255), 2, cv2.LINE_AA)
                # else:
                    # name = "Desconocido"
                    # color = (30, 30, 255)
                # cv2.rectangle(frame, (x, y + h), (x + w, y + h + 30), color, -1)
                # cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
                # cv2.putText(frame, name, (x, y + h + 25), 2, 1, (255, 255, 255), 2, cv2.LINE_AA)

            if ret:
                self.change_pixmap_signal.emit(frame)

        # shut down capture system
        cap.release()

    def stop(self):
        """Sets run flag to False and waits for thread to finish"""
        self._run_flag = False
        self.wait()


class LiveCam(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        # self.setWindowFlag(QtCore.Qt.WindowCloseButtonHint, False)
        # self.setWindowFlag(QtCore.Qt.WindowMinimizeButtonHint, False)
        # self.setWindowFlag(QtCore.Qt.WindowMaximizeButtonHint, False)
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

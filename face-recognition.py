# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'face_recognition.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QImage,QPixmap
from PyQt5.QtWidgets import QDialog,QApplication,QInputDialog,QLineEdit,QFileDialog
import pickle
import cv2
import image_face_recognition as ifr
import realtime_face_recognition as rfr

class Ui_FaceRecognition(object):
    
    def displayImage(self):
        try:
            filename=QFileDialog.getOpenFileName(None, "Open Image", "", "Image files (*.jpg *.png)")
            path=filename[0]
            self.video_player.clear()
            img=ifr.main(path)
            height, width, channel = img.shape
            bytesPerLine = 3 * width
            qImg = QImage(img.data, width, height, bytesPerLine, QImage.Format_RGB888).rgbSwapped()
            pixmap=QPixmap(qImg)
            self.video_player.setPixmap(pixmap)
            
        except Exception as e:
            print(e)

            
    def takeInputs(self):
        try:
            path,result1 = QInputDialog.getText(FaceRecognition, 'Input Dialog', 'Enter the path:')
            if result1:
                if not path:
                    self.takeInputs()
                    return
                name,result2 = QInputDialog.getText(FaceRecognition, 'Input Dialog', 'Enter the name:')
                if result2:
                    if not name:
                        self.takeInputs()
                        return
                    ifr.names(name,path)
                else:
                    QInputDialog.deleteLater()
            else:
                QInputDialog.deleteLater()

        except Exception as e:
            None
    def feed(self,path):
        try:
            self.video_player.clear()
            _translate = QtCore.QCoreApplication.translate
            webcam=cv2.VideoCapture(path)
            with open('dataset_faces.dat', 'rb') as f:
                record=pickle.load(f)
            self.closefeed = QtWidgets.QPushButton(self.centralwidget)
            self.closefeed.setMinimumSize(QtCore.QSize(0, 71))
            self.closefeed.setMaximumSize(QtCore.QSize(160000, 71))
            self.closefeed.setObjectName("closefeed")
            self.verticalLayout_3.addWidget(self.closefeed)
            self.closefeed.setText(_translate("FaceRecognition", "CLOSE FEED"))
            self.running=True
            while self.running:
                ret,current_frame=webcam.read()
                img=rfr.main(current_frame,record)
                height, width, channel = img.shape
                bytesPerLine = 3 * width
                qImg = QImage(img.data, width, height, bytesPerLine, QImage.Format_RGB888).rgbSwapped()
                pixmap=QPixmap(qImg)
                if width>1024:
                    pixmap = pixmap.scaledToHeight(720)
                self.video_player.setPixmap(pixmap)
                cv2.waitKey()
                self.closefeed.clicked.connect(self.stop)
            self.closefeed.deleteLater()
        except Exception as e:
            self.closefeed.deleteLater()
            return

    def preview(self):
        try:
            filename=QFileDialog.getOpenFileName(None, "Open Video", "", "Video files (*.mp4 *.3gp *.avi)")
            path=filename[0]
            self.feed(path)
            
        except Exception as e:
            return

    def camera(self):
        ch,result1 = QInputDialog.getText(FaceRecognition, 'Input Dialog', 'Choose the Camera:')
        if result1:
            if not ch:
                self.camera()
                return
            n=int(ch)
            self.feed(n)
        else:
            QInputDialog.deleteLater()

            
    def stop(self):
        self.running=False
        self.video_player.clear()
            
    def setupUi(self, FaceRecognition):
        FaceRecognition.setObjectName("FaceRecognition")
        FaceRecognition.resize(1015, 627)
        self.centralwidget = QtWidgets.QWidget(FaceRecognition)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setMinimumSize(QtCore.QSize(0, 200))
        self.textBrowser.setMaximumSize(QtCore.QSize(16777215, 200))
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout_4.addWidget(self.textBrowser)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.add_face = QtWidgets.QPushButton(self.centralwidget)
        self.add_face.setMinimumSize(QtCore.QSize(0, 71))
        self.add_face.setMaximumSize(QtCore.QSize(160000, 71))
        self.add_face.setObjectName("add_face")
        self.verticalLayout_3.addWidget(self.add_face)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.recognize_image = QtWidgets.QPushButton(self.centralwidget)
        self.recognize_image.setMinimumSize(QtCore.QSize(111, 61))
        self.recognize_image.setMaximumSize(QtCore.QSize(111, 61))
        self.recognize_image.setObjectName("recognize_image")
        self.horizontalLayout.addWidget(self.recognize_image)
        self.live_feed = QtWidgets.QPushButton(self.centralwidget)
        self.live_feed.setMinimumSize(QtCore.QSize(111, 61))
        self.live_feed.setMaximumSize(QtCore.QSize(111, 61))
        self.live_feed.setObjectName("live_feed")
        self.horizontalLayout.addWidget(self.live_feed)
        self.recognize_video = QtWidgets.QPushButton(self.centralwidget)
        self.recognize_video.setMinimumSize(QtCore.QSize(111, 61))
        self.recognize_video.setMaximumSize(QtCore.QSize(111, 61))
        self.recognize_video.setObjectName("recognize_video")
        self.horizontalLayout.addWidget(self.recognize_video)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.close = QtWidgets.QPushButton(self.centralwidget)
        self.close.setMinimumSize(QtCore.QSize(0, 71))
        self.close.setMaximumSize(QtCore.QSize(160000, 71))
        self.close.setObjectName("close")
        self.verticalLayout_3.addWidget(self.close)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem1)
        self.horizontalLayout_4.addLayout(self.verticalLayout_3)
        self.video_player = QtWidgets.QLabel(self.centralwidget)
        self.video_player.setMinimumSize(QtCore.QSize(0,0))
        self.video_player.setMaximumSize(QtCore.QSize(160000,160000))
        self.video_player.setBaseSize(QtCore.QSize(0, 0))
        self.video_player.setFrameShape(QtWidgets.QFrame.Box)
        self.video_player.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.video_player.setLineWidth(7)
        self.video_player.setMidLineWidth(0)
        self.video_player.setText("")
        
        self.video_player.setObjectName("video_player")
        self.horizontalLayout_4.addWidget(self.video_player)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        FaceRecognition.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(FaceRecognition)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1015, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        FaceRecognition.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(FaceRecognition)
        self.statusbar.setObjectName("statusbar")
        FaceRecognition.setStatusBar(self.statusbar)
        self.actionExit = QtWidgets.QAction(FaceRecognition)
        self.actionExit.setObjectName("actionExit")
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())
        self.recognize_image.clicked.connect(self.displayImage)
        self.add_face.clicked.connect(self.takeInputs)
        self.live_feed.clicked.connect(self.camera)
        self.recognize_video.clicked.connect(self.preview)
        self.close.clicked.connect(FaceRecognition.close)
        self.actionExit.triggered.connect(FaceRecognition.close)

        self.retranslateUi(FaceRecognition)
        QtCore.QMetaObject.connectSlotsByName(FaceRecognition)

    def retranslateUi(self, FaceRecognition):
        _translate = QtCore.QCoreApplication.translate
        FaceRecognition.setWindowTitle(_translate("FaceRecognition", "MainWindow"))
        self.textBrowser.setHtml(_translate("FaceRecognition", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:600;\">MADE BY NILAY SAXENA(Magnus)!!</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:18pt; font-weight:600;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-style:italic;\">Add people using ADD FACE</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-style:italic;\">For analyzing images use RECOGNIZE IMAGE</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-style:italic;\">For real time recognition use LIVE FEED</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-style:italic;\">For a pre-recorded video use RECOGNIZE VIDEO</span></p></body></html>"))
        self.add_face.setText(_translate("FaceRecognition", "ADD FACE"))
        self.recognize_image.setText(_translate("FaceRecognition", "RECOGNIZE IMAGE"))
        self.live_feed.setText(_translate("FaceRecognition", "LIVE FEED"))
        self.recognize_video.setText(_translate("FaceRecognition", "RECOGNIZE VIDEO"))
        self.close.setText(_translate("FaceRecognition", "CLOSE (Ctrl+Q)"))
        self.menuFile.setTitle(_translate("FaceRecognition", "File"))
        self.actionExit.setText(_translate("FaceRecognition", "Exit"))
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FaceRecognition = QtWidgets.QMainWindow()
    ui = Ui_FaceRecognition()
    ui.setupUi(FaceRecognition)
    FaceRecognition.show()
    sys.exit(app.exec_())


import os
os.environ["SM_FRAMEWORK"] = "tf.keras"
from tensorflow import keras
import segmentation_models as sm
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
import cv2
import tensorflow as tf
import numpy as np
import matplotlib.cm as cm
from IPython.display import Image
import tensorflow as tf
from tensorflow.keras import Sequential
from tensorflow.keras.layers import *
from tensorflow.keras.models import * 
from tensorflow.keras.preprocessing import image
from tensorflow.keras.utils import load_img, img_to_array
import matplotlib.pyplot as plt
from PyQt5.uic import loadUi
import segmentation_models as sm
class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1122, 837)
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(0, 0, 1121, 841))
        self.widget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.widget.setStyleSheet("background-color:rgb(245, 245, 245);\n"
"")
        self.widget.setObjectName("widget")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(330, 130, 821, 111))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.Image = QtWidgets.QLabel(self.widget)
        self.Image.setGeometry(QtCore.QRect(330, 270, 281, 321))
        self.Image.setFrameShape(QtWidgets.QFrame.Box)
        self.Image.setFrameShadow(QtWidgets.QFrame.Plain)
        self.Image.setText("")
        self.Image.setScaledContents(True)
        self.Image.setObjectName("Image")
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setGeometry(QtCore.QRect(290, 600, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.cscore = QtWidgets.QLabel(self.widget)
        self.cscore.setGeometry(QtCore.QRect(250, 750, 231, 41))
        self.cscore.setFrameShape(QtWidgets.QFrame.Box)
        self.cscore.setFrameShadow(QtWidgets.QFrame.Plain)
        self.cscore.setText("")
        self.cscore.setObjectName("cscore")
        self.outcome = QtWidgets.QLabel(self.widget)
        self.outcome.setGeometry(QtCore.QRect(250, 650, 231, 41))
        self.outcome.setFrameShape(QtWidgets.QFrame.Box)
        self.outcome.setFrameShadow(QtWidgets.QFrame.Plain)
        self.outcome.setLineWidth(1)
        self.outcome.setText("")
        self.outcome.setObjectName("outcome")
        self.upload = QtWidgets.QPushButton(self.widget)
        self.upload.setGeometry(QtCore.QRect(100, 290, 221, 51))
        self.upload.setStyleSheet("font: 75 11pt \"MS Shell Dlg 2\";")
        self.upload.setDefault(False)
        self.upload.setFlat(False)
        self.upload.setObjectName("upload")
        self.segment = QtWidgets.QPushButton(self.widget)
        self.segment.setGeometry(QtCore.QRect(130, 460, 161, 51))
        self.segment.setStyleSheet("font: 75 11pt \"MS Shell Dlg 2\";")
        self.segment.setObjectName("segment")
        self.quantify = QtWidgets.QPushButton(self.widget)
        self.quantify.setGeometry(QtCore.QRect(150, 550, 121, 41))
        self.quantify.setStyleSheet("font: 75 11pt \"MS Shell Dlg 2\";")
        self.quantify.setObjectName("quantify")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(270, 700, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setGeometry(QtCore.QRect(640, 610, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.about = QtWidgets.QLabel(self.widget)
        self.about.setGeometry(QtCore.QRect(550, 650, 341, 141))
        self.about.setFrameShape(QtWidgets.QFrame.Box)
        self.about.setFrameShadow(QtWidgets.QFrame.Plain)
        self.about.setText("")
        self.about.setObjectName("about")
        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setGeometry(QtCore.QRect(90, 100, 91, 101))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap(r"C:\Users\biomedical research\Desktop\CoE Research Works\coe logo900.jpeg"))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.widget)
        self.label_8.setGeometry(QtCore.QRect(360, 220, 291, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.Image_2 = QtWidgets.QLabel(self.widget)
        self.Image_2.setGeometry(QtCore.QRect(650, 270, 281, 321))
        self.Image_2.setFrameShape(QtWidgets.QFrame.Box)
        self.Image_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.Image_2.setText("")
        self.Image_2.setScaledContents(True)
        self.Image_2.setObjectName("Image_2")
        self.label_9 = QtWidgets.QLabel(self.widget)
        self.label_9.setGeometry(QtCore.QRect(670, 220, 291, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.line = QtWidgets.QFrame(self.widget)
        self.line.setGeometry(QtCore.QRect(40, 40, 1051, 16))
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(2)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.widget)
        self.line_2.setGeometry(QtCore.QRect(30, 50, 20, 771))
        self.line_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_2.setLineWidth(2)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.widget)
        self.line_3.setGeometry(QtCore.QRect(40, 810, 1051, 16))
        self.line_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_3.setLineWidth(2)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(self.widget)
        self.line_4.setGeometry(QtCore.QRect(1080, 50, 20, 771))
        self.line_4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_4.setLineWidth(2)
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setObjectName("line_4")
        self.detect_2 = QtWidgets.QPushButton(self.widget)
        self.detect_2.setGeometry(QtCore.QRect(130, 370, 161, 51))
        self.detect_2.setStyleSheet("font: 75 11pt \"MS Shell Dlg 2\";")
        self.detect_2.setObjectName("detect_2")
        self.label_10 = QtWidgets.QLabel(self.widget)
        self.label_10.setGeometry(QtCore.QRect(240, 50, 821, 111))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_4.setText(_translate("Dialog", "        URINARY STONE SEGMENTATION \n"
"          AND QUANTIFICATION SYSTEM              "))
        self.label_6.setText(_translate("Dialog", "Predicted pathology"))
        self.upload.setText(_translate("Dialog", "UPLOAD INPUT \n"
" URETEROSCOPY IMAGE"))
        self.segment.setText(_translate("Dialog", "SEGMENT \n"
" PATHOLOGY"))
        self.quantify.setText(_translate("Dialog", "QUANTIFY \n"
" RESULTS"))
        self.label_3.setText(_translate("Dialog", "Number of Pathologies"))
        self.label_5.setText(_translate("Dialog", "About the condition"))
        self.label_8.setText(_translate("Dialog", "Input ureteroscopy image"))
        self.label_9.setText(_translate("Dialog", "Segmented Region of Interest"))
        self.detect_2.setText(_translate("Dialog", "EXTRACT \n"
" FRAME"))
        self.label_10.setText(_translate("Dialog", "          RAJALAKSHMI ENGINEERING COLLEGE \n"
"    CENTER OF EXCELLENCE IN MEDICAL IMAGING              "))
        self.upload.clicked.connect(self.loadimage)
        self.segment.clicked.connect(self.predictimage)
        self.quantify.clicked.connect(self.quantifyimage)
        self.tmp=None
        self.ab=None
        self.out=None
        self.model=tf.keras.models.load_model(r"C:\CoE Research Works\project works\Urinary stone segmentation\urine stone seg model (2.9).h5",compile=False)
    def loadimage(self):
            self.filename1 = QtWidgets.QFileDialog.getOpenFileName(filter='Image (*.*)')
            self.filename = self.filename1[0]
            print(self.filename)
            self.outcome.setText("Image Loaded!!")
            self.image = cv2.imread(self.filename)
            self.setPhoto(self.image)

    def setPhoto(self, image):
            self.tmp = image
            image = cv2.resize(image, (256, 256), cv2.INTER_AREA)
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            self.ab=image
            image = QtGui.QImage(image.data, image.shape[1], image.shape[0], QtGui.QImage.Format_RGB888)
            self.Image.setPixmap(QPixmap.fromImage(image))
    def predictimage(self):
        self.tmp = cv2.resize(self.tmp, (256, 256))
        self.tmp = np.expand_dims(self.tmp, axis = 0)
        self.tmp = self.tmp / 255
        result = self.model.predict(self.tmp)   
        result=(result>=0.5).astype(np.uint8)
        result=np.squeeze(result)
        fig = plt.figure()
        fig.subplots_adjust(hspace=1, wspace=1)
        ax = fig.add_subplot(1, 1, 1)
        ax.imshow(np.reshape(result, (256,256)), cmap="gray")
        plt.axis('off')
        ax.axes.get_xaxis().set_visible(False)
        ax.axes.get_yaxis().set_visible(False)
        save_path = r"C:\CoE Research Works\project works\Urinary stone segmentation\output2.png"
        plt.savefig(save_path,bbox_inches='tight', pad_inches = 0, dpi=200)
        pixmaps = QPixmap(save_path)
        smallPixmaps = pixmaps.scaled(301, 231, QtCore.Qt.KeepAspectRatio, QtCore.Qt.FastTransformation)
        self.Image_2.setPixmap(QPixmap(smallPixmaps))
    def quantifyimage(self):   
        self.outcome.setText("Urinary Stone- Calcium Oxalate")
        self.cscore.setText('              1')
        self.about.setText('Kidney stones (also called renal calculi, nephrolithiasis or urolithiasis) \n are hard deposits made of minerals and salts that form inside your kidneys.\n Diet, excess body weight, some medical conditions, and certain supplements \n are among the many causes of kidney stones. Kidney stones can affect any part of your \n urinary tract — from your kidneys to your bladder. \n Often, stones form when the urine becomes concentrated, \n allowing minerals to crystallize and stick together')
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'agv_interface2.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!



import sys
import time
import rospy
import rospkg
from rviz import bindings as rviz
from PyQt5 import uic, QtGui, QtCore,QtWidgets
from PyQt5.QtCore import Qt
from sensor_msgs.msg import JointState
from geometry_msgs.msg import PoseWithCovarianceStamped
import asyncio
from quamash import QEventLoop
import kavurlar_logo_rc
from PyQt5.QtCore import QObject, QThread, pyqtSignal
import threading
from std_msgs.msg import String
from std_msgs.msg import Float64
from geometry_msgs.msg import Twist
import os
import command
import sys, select, termios, tty
import kavurlar_logo_rc
import subprocess



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1469, 799)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/kavurlar_logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout_4.addWidget(self.label, 6, 0, 1, 1)
        self.slopeY = QtWidgets.QLineEdit(self.centralwidget)
        self.slopeY.setObjectName("slopeY")
        self.gridLayout_4.addWidget(self.slopeY, 4, 2, 1, 1)
        #self.frame = rviz.VisualizationFrame()
        #self.frame.setSplashPath( "" )
        #self.frame.initialize()
        #reader = rviz.YamlConfigReader()
        #config = rviz.Config()		
        #reader.readFile( config, "/home/kavurlar/catkin_ws/src/diff_om_drive/rviz_config/config.rviz" )
        #self.frame.load( config )	

 #       self.frame.setMenuBar( None )
 #       self.frame.setStatusBar( None )
 #       self.frame.setHideButtonVisibility( True )
 #       self.manager = self.frame.getManager()
     #   self.gridLayout_4.addWidget(self.frame, 0, 4, 9, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout_4.addWidget(self.label_3, 5, 1, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.startMappingButton = QtWidgets.QPushButton(self.centralwidget)
        self.startMappingButton.setMinimumSize(QtCore.QSize(0, 40))
        self.startMappingButton.setBaseSize(QtCore.QSize(30, 100))
        self.startMappingButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(114, 159, 207);")
        self.startMappingButton.setObjectName("startMappingButton")
        self.gridLayout.addWidget(self.startMappingButton, 0, 0, 1, 1)
        self.startRouteButton = QtWidgets.QPushButton(self.centralwidget)
        self.startRouteButton.setMinimumSize(QtCore.QSize(0, 40))
        self.startRouteButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(114, 159, 207);")
        self.startRouteButton.setObjectName("startRouteButton")
        self.gridLayout.addWidget(self.startRouteButton, 0, 1, 1, 1)
        self.startAutonomousButton = QtWidgets.QPushButton(self.centralwidget)
        self.startAutonomousButton.setMinimumSize(QtCore.QSize(0, 40))
        self.startAutonomousButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(114, 159, 207);")
        self.startAutonomousButton.setObjectName("startAutonomousButton")
        self.gridLayout.addWidget(self.startAutonomousButton, 0, 2, 1, 1)
        self.stopMappingButton = QtWidgets.QPushButton(self.centralwidget)
        self.stopMappingButton.setMinimumSize(QtCore.QSize(0, 40))
        self.stopMappingButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(114, 159, 207);")
        self.stopMappingButton.setObjectName("stopMappingButton")
        self.gridLayout.addWidget(self.stopMappingButton, 1, 0, 1, 1)
        self.stopRouteButton = QtWidgets.QPushButton(self.centralwidget)
        self.stopRouteButton.setMinimumSize(QtCore.QSize(0, 40))
        self.stopRouteButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(114, 159, 207);")
        self.stopRouteButton.setObjectName("stopRouteButton")
        self.gridLayout.addWidget(self.stopRouteButton, 1, 1, 1, 1)
        self.StopAutonomoustButton = QtWidgets.QPushButton(self.centralwidget)
        self.StopAutonomoustButton.setMinimumSize(QtCore.QSize(0, 40))
        self.StopAutonomoustButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(114, 159, 207);")
        self.StopAutonomoustButton.setObjectName("StopAutonomoustButton")
        self.gridLayout.addWidget(self.StopAutonomoustButton, 1, 2, 1, 1)
        self.saveMappingButton = QtWidgets.QPushButton(self.centralwidget)
        self.saveMappingButton.setMinimumSize(QtCore.QSize(0, 40))
        self.saveMappingButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(114, 159, 207);")
        self.saveMappingButton.setObjectName("saveMappingButton")
        self.gridLayout.addWidget(self.saveMappingButton, 2, 0, 1, 1)
        self.routeCoordinateButton = QtWidgets.QPushButton(self.centralwidget)
        self.routeCoordinateButton.setMinimumSize(QtCore.QSize(0, 40))
        self.routeCoordinateButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(114, 159, 207);")
        self.routeCoordinateButton.setObjectName("routeCoordinateButton")
        self.gridLayout.addWidget(self.routeCoordinateButton, 2, 1, 1, 1)
        self.autonomousSettingsButton = QtWidgets.QPushButton(self.centralwidget)
        self.autonomousSettingsButton.setMinimumSize(QtCore.QSize(0, 40))
        self.autonomousSettingsButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(114, 159, 207);")
        self.autonomousSettingsButton.setObjectName("autonomousSettingsButton")
        self.gridLayout.addWidget(self.autonomousSettingsButton, 2, 2, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout, 0, 0, 1, 4)
        self.instantaneousVelocityX = QtWidgets.QLineEdit(self.centralwidget)
        self.instantaneousVelocityX.setObjectName("instantaneousVelocityX")
        self.gridLayout_4.addWidget(self.instantaneousVelocityX, 1, 1, 1, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.leftForwardButton = QtWidgets.QPushButton(self.centralwidget)
        self.leftForwardButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(114, 159, 207);")
        self.leftForwardButton.setObjectName("leftForwardButton")
        self.gridLayout_2.addWidget(self.leftForwardButton, 0, 0, 1, 1)
        self.forwardButton = QtWidgets.QPushButton(self.centralwidget)
        self.forwardButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(114, 159, 207);")
        self.forwardButton.setObjectName("forwardButton")
        self.gridLayout_2.addWidget(self.forwardButton, 0, 1, 1, 1)
        self.rightForwardButton = QtWidgets.QPushButton(self.centralwidget)
        self.rightForwardButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(114, 159, 207);")
        self.rightForwardButton.setObjectName("rightForwardButton")
        self.gridLayout_2.addWidget(self.rightForwardButton, 0, 2, 1, 1)
        self.leftButton = QtWidgets.QPushButton(self.centralwidget)
        self.leftButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(114, 159, 207);")
        self.leftButton.setObjectName("leftButton")
        self.gridLayout_2.addWidget(self.leftButton, 1, 0, 1, 1)
        self.StopButton = QtWidgets.QPushButton(self.centralwidget)
        self.StopButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(114, 159, 207);")
        self.StopButton.setObjectName("StopButton")
        self.gridLayout_2.addWidget(self.StopButton, 1, 1, 1, 1)
        self.rightButton = QtWidgets.QPushButton(self.centralwidget)
        self.rightButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(114, 159, 207);")
        self.rightButton.setObjectName("rightButton")
        self.gridLayout_2.addWidget(self.rightButton, 1, 2, 1, 1)
        self.leftBackwardButton = QtWidgets.QPushButton(self.centralwidget)
        self.leftBackwardButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(114, 159, 207);")
        self.leftBackwardButton.setObjectName("leftBackwardButton")
        self.gridLayout_2.addWidget(self.leftBackwardButton, 2, 0, 1, 1)
        self.backwardButton = QtWidgets.QPushButton(self.centralwidget)
        self.backwardButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(114, 159, 207);")
        self.backwardButton.setObjectName("backwardButton")
        self.gridLayout_2.addWidget(self.backwardButton, 2, 1, 1, 1)
        self.rightBackwardButton = QtWidgets.QPushButton(self.centralwidget)
        self.rightBackwardButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(114, 159, 207);")
        self.rightBackwardButton.setObjectName("rightBackwardButton")
        self.gridLayout_2.addWidget(self.rightBackwardButton, 2, 2, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 1, 2)
        self.gridLayout_4.addLayout(self.gridLayout_3, 7, 0, 1, 4)
        self.position = QtWidgets.QLabel(self.centralwidget)
        self.position.setObjectName("position")
        self.gridLayout_4.addWidget(self.position, 3, 0, 1, 1)
        self.positionX = QtWidgets.QLineEdit(self.centralwidget)
        self.positionX.setText("")
        self.positionX.setObjectName("positionX")
        self.gridLayout_4.addWidget(self.positionX, 3, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout_4.addWidget(self.label_4, 5, 3, 1, 1)
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout_4.addWidget(self.textEdit, 8, 0, 1, 4)
        self.instantaneousVelocityLabel = QtWidgets.QLabel(self.centralwidget)
        self.instantaneousVelocityLabel.setObjectName("instantaneousVelocityLabel")
        self.gridLayout_4.addWidget(self.instantaneousVelocityLabel, 1, 0, 1, 1)
        self.statusBatteryLabel = QtWidgets.QLabel(self.centralwidget)
        self.statusBatteryLabel.setObjectName("statusBatteryLabel")
        self.gridLayout_4.addWidget(self.statusBatteryLabel, 2, 0, 1, 1)
        self.slopeX = QtWidgets.QLineEdit(self.centralwidget)
        self.slopeX.setObjectName("slopeX")
        self.gridLayout_4.addWidget(self.slopeX, 4, 1, 1, 1)
        self.positionZ = QtWidgets.QLineEdit(self.centralwidget)
        self.positionZ.setObjectName("positionZ")
        self.gridLayout_4.addWidget(self.positionZ, 3, 3, 1, 1)
        self.slopeLabel = QtWidgets.QLabel(self.centralwidget)
        self.slopeLabel.setObjectName("slopeLabel")
        self.gridLayout_4.addWidget(self.slopeLabel, 4, 0, 1, 1)
        self.slopeZ = QtWidgets.QLineEdit(self.centralwidget)
        self.slopeZ.setObjectName("slopeZ")
        self.gridLayout_4.addWidget(self.slopeZ, 4, 3, 1, 1)
        self.statusBattery = QtWidgets.QLineEdit(self.centralwidget)
        self.statusBattery.setObjectName("statusBattery")
        self.gridLayout_4.addWidget(self.statusBattery, 2, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout_4.addWidget(self.label_2, 6, 2, 1, 1)
        self.positionY = QtWidgets.QLineEdit(self.centralwidget)
        self.positionY.setText("")
        self.positionY.setObjectName("positionY")
        self.gridLayout_4.addWidget(self.positionY, 3, 2, 1, 1)
        self.horizontalSlider_2 = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_2.setObjectName("horizontalSlider_2")
        self.gridLayout_4.addWidget(self.horizontalSlider_2, 6, 3, 1, 1)
        self.instantaneousVelocityY = QtWidgets.QLineEdit(self.centralwidget)
        self.instantaneousVelocityY.setObjectName("instantaneousVelocityY")
        self.gridLayout_4.addWidget(self.instantaneousVelocityY, 1, 2, 1, 1)
        self.horizontalSlider = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.gridLayout_4.addWidget(self.horizontalSlider, 6, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1469, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.horizontalSlider.setMinimum(0)
        self.horizontalSlider.setMaximum(100)
        self.horizontalSlider.setValue(30)
        self.horizontalSlider.setSingleStep(1)
        self.label_3.setText('Doğrusal Hız = 0.30')

        self.horizontalSlider_2.setMinimum(0)
        self.horizontalSlider_2.setMaximum(100)
        self.horizontalSlider_2.setValue(20)
        self.horizontalSlider_2.setSingleStep(1)
        self.label_4.setText('Açısal Hız = 0.20')

        self.horizontalSlider.valueChanged['int'].connect(MainWindow.slotLinear)
        self.horizontalSlider_2.valueChanged['int'].connect(MainWindow.slotAngular)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.thread = QThread()
        self.worker = Worker()
        self.worker.moveToThread(self.thread)
        self.thread.started.connect(self.worker.run)
        self.thread.start()

    def retranslateUi(self, MainWindow):

      
        rospy.init_node('teleop2')
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Kavurlar-Agv"))
        self.label.setText(_translate("MainWindow", "Doğrusal  Hız:"))
        self.label_3.setText(_translate("MainWindow", "TextLabel"))
        self.startMappingButton.setText(_translate("MainWindow", "Harita Başlat"))
        self.startRouteButton.setText(_translate("MainWindow", "Rota Başlat"))
        self.startAutonomousButton.setText(_translate("MainWindow", "Otonom Başlat"))
        self.stopMappingButton.setText(_translate("MainWindow", "Harita Durdur"))
        self.stopRouteButton.setText(_translate("MainWindow", "Rota Durdur"))
        self.StopAutonomoustButton.setText(_translate("MainWindow", "Otonom Durdur"))
        self.saveMappingButton.setText(_translate("MainWindow", "Harita Kaydet"))
        self.routeCoordinateButton.setText(_translate("MainWindow", "Rota Koordinat"))
        self.autonomousSettingsButton.setText(_translate("MainWindow", "Otonom Ayarlar"))
        self.leftForwardButton.setText(_translate("MainWindow", "SOL İLERİ"))
        self.forwardButton.setText(_translate("MainWindow", "İLERİ"))
        self.rightForwardButton.setText(_translate("MainWindow", "SAĞ İLERİ"))
        self.leftButton.setText(_translate("MainWindow", "SOL"))
        self.StopButton.setText(_translate("MainWindow", "DUR"))
        self.rightButton.setText(_translate("MainWindow", "SAĞ"))
        self.leftBackwardButton.setText(_translate("MainWindow", "SOL GERİ"))
        self.backwardButton.setText(_translate("MainWindow", "GERİ"))
        self.rightBackwardButton.setText(_translate("MainWindow", "SAĞ GERİ"))
        self.position.setText(_translate("MainWindow", "Konum:"))
        self.label_4.setText(_translate("MainWindow", "TextLabel"))
        self.instantaneousVelocityLabel.setText(_translate("MainWindow", "Anlık Hız:"))
        self.statusBatteryLabel.setText(_translate("MainWindow", "Batarya Durumu:"))
        self.slopeLabel.setText(_translate("MainWindow", "Eğim:"))
        self.label_2.setText(_translate("MainWindow", "                         Açısal Hız:"))
    
 

        self.leftForwardButton.pressed.connect(self.leftForwardButtonPressed)
        self.leftForwardButton.released.connect(self.buttonReleased) 

        self.forwardButton.pressed.connect(self.forwardButtonPressed)
        self.forwardButton.released.connect(self.buttonReleased) 

        self.rightForwardButton.pressed.connect(self.rightForwardButtonPressed)
        self.rightForwardButton.released.connect(self.buttonReleased) 

        self.leftButton.pressed.connect(self.leftButtonPressed)
        self.leftButton.released.connect(self.buttonReleased) 

        self.StopButton.pressed.connect(self.stopButtonPressed)
        self.StopButton.released.connect(self.buttonReleased) 

        self.rightButton.pressed.connect(self.rightButtonPressed)
        self.rightButton.released.connect(self.buttonReleased) 

        self.leftBackwardButton.pressed.connect(self.leftBackwardButtonPressed)
        self.leftBackwardButton.released.connect(self.buttonReleased) 

        self.backwardButton.pressed.connect(self.backwardButtonPressed)
        self.backwardButton.released.connect(self.buttonReleased) 

        self.rightBackwardButton.pressed.connect(self.rightBackwardButtonPressed)
        self.rightBackwardButton.released.connect(self.buttonReleased) 

        self.startMappingButton.clicked.connect(self.startMapping)

        self.stopMappingButton.clicked.connect(self.stopMapping)
  
        self.startRouteButton.clicked.connect(self.startRoute)
        
        self.stopRouteButton.clicked.connect(self.stopRoute)
        
        self.startAutonomousButton.clicked.connect(self.startAutonomous)
        
        self.StopAutonomoustButton.clicked.connect(self.stopAutonomous)

        self.routeCoordinateButton.clicked.connect(self.routeCoordinate)

        self.saveMappingButton.clicked.connect(self.saveMapping)

        self.autonomousSettingsButton.clicked.connect(self.autonomousSettings)

        rospy.Subscriber('/yaw', Float64,self.callback8, queue_size=100)
        rospy.Subscriber('/roll', Float64,self.callback7, queue_size=100) 
        rospy.Subscriber('/pitch', Float64,self.callback6, queue_size=100)     
        rospy.Subscriber('/cmd_vel', Twist,self.callback5, queue_size=100)
        self.twist1 = Twist()
        self.pitch = Float64()
        self.roll = Float64()
        self.yaw = Float64()

    def routeCoordinate(self):
        os.popen('sh /home/kavurlar/rota_koordinat.sh')
    
    def saveMapping(self):
        os.popen('sh /home/kavurlar/harita_kaydet.sh')
    
    def autonomousSettings(self):
        os.popen('sh /home/kavurlar/start_excel.sh')

       # ret = subprocess.run(command, capture_output=True, shell=True)
        #subprocess.call("xterm", "-e","libreoffice Desktop/rota_ve_map/kvr_rota.xls")
        #gnome-terminal -x sh -c ("libreoffice Desktop/rota_ve_map/kvr_rota.xls;bash")
        
    def startMapping(self):
        self.frame = rviz.VisualizationFrame()
        self.frame.setSplashPath( "" )
        self.frame.initialize()
        reader = rviz.YamlConfigReader()
        config = rviz.Config()		
        reader.readFile( config, "/home/kavurlar/catkin_ws/src/diff_om_drive/rviz_config/config.rviz" )
        self.frame.load( config )
        self.frame.setMenuBar( None )
        self.frame.setStatusBar( None )
        self.frame.setHideButtonVisibility( True )
        self.gridLayout_4.addWidget(self.frame, 0, 4, 9, 1)
        os.popen('sh /home/kavurlar/start_harita.sh')
        	
       
        
    def stopMapping(self):
        
        os.system('sh /home/kavurlar/stop_harita.sh')
        temp = ''
        nodes = os.popen("rosnode list").readlines()
        for i in range(len(nodes)):
            temp += nodes[i]
            nodes[i] = nodes[i].replace("\n","")
        self.textEdit.setText("Ros devre dışı")
        for node in nodes:
            if node != '/teleop2':
                os.system("rosnode kill "+ node)
        self.frame.close()
        
        
                
        #for node in nodes:
         #   if node != '/rosout':
          #      os.system("rosnode kill "+ node)

    def startRoute(self):
        self.frame = rviz.VisualizationFrame()
        self.frame.setSplashPath( "" )
        self.frame.initialize()
        reader = rviz.YamlConfigReader()
        config = rviz.Config()		
        reader.readFile( config, "/home/kavurlar/catkin_ws/src/diff_om_drive/rviz_config/config.rviz" )
        self.frame.load( config )
        self.frame.setMenuBar( None )
        self.frame.setStatusBar( None )
        self.frame.setHideButtonVisibility( True )
        self.gridLayout_4.addWidget(self.frame, 0, 4, 9, 1)
        os.popen('sh /home/kavurlar/start_rota.sh')
        

    def stopRoute(self):
        temp = ''
        nodes = os.popen("rosnode list").readlines()
        for i in range(len(nodes)):
            temp += nodes[i]
            nodes[i] = nodes[i].replace("\n","")
        self.textEdit.setText("Ros devre dışı")
        for node in nodes:
            if node != '/teleop2':
                os.system("rosnode kill "+ node)
        self.frame.close()
    def startAutonomous(self):
        self.frame = rviz.VisualizationFrame()
        self.frame.setSplashPath( "" )
        self.frame.initialize()
        reader = rviz.YamlConfigReader()
        config = rviz.Config()		
        reader.readFile( config, "/home/kavurlar/catkin_ws/src/diff_om_drive/rviz_config/config.rviz" )
        self.frame.load( config )
        self.frame.setMenuBar( None )
        self.frame.setStatusBar( None )
        self.frame.setHideButtonVisibility( True )
        self.gridLayout_4.addWidget(self.frame, 0, 4, 9, 1)
        os.popen('sh /home/kavurlar/start_otonom.sh')
        

    def stopAutonomous(self):
        temp = ''
        nodes = os.popen("rosnode list").readlines()
        for i in range(len(nodes)):
            temp += nodes[i]
            nodes[i] = nodes[i].replace("\n","")
        self.textEdit.setText("Ros devre dışı")
        for node in nodes:
            if node != '/teleop2':
                os.system("rosnode kill "+ node)
        self.frame.close()

    def leftForwardButtonPressed(self):
        self.worker.setKey('q')        

    def forwardButtonPressed(self):
        self.worker.setKey('w')

    def rightForwardButtonPressed(self):
        self.worker.setKey('e')

    def leftButtonPressed(self):
        self.worker.setKey('a')

    def stopButtonPressed(self):
        self.worker.setKey('s')

    def rightButtonPressed(self):
        self.worker.setKey('d')

    def leftBackwardButtonPressed(self):
        self.worker.setKey('z')

    def backwardButtonPressed(self):
        self.worker.setKey('x')

    def rightBackwardButtonPressed(self):
        self.worker.setKey('c')
                
    def buttonReleased(self):
        self.worker.setKeyEmpty() 

    def linearVelocityUpPressed(self):
        self.worker.setKey('y')

    def linearVelocityDownPressed(self):
        self.worker.setKey('h')

    def AngularVelocityUpPressed(self):
        self.worker.setKey('u')

    def angularVelocityDownPressed(self):
        self.worker.setKey('j')   

    def callback5(self,twist1):
        try:
            self.twist1.linear.x = twist1.linear.x
            self.twist1.angular.z = twist1.angular.z
            self.instantaneousVelocityX.setText(str(round(self.twist1.linear.x,1)))
            self.instantaneousVelocityY.setText(str(round(self.twist1.angular.z,1)))
        except Exception as e:
            print("An exception occurred"+ str(e))
        
    def callback6(self,pitch):
        try:
            self.pitch.data = pitch.data
            
            self.slopeY.setText(str(round(self.pitch.data,1)))
   
        except Exception as e:
            print("An exception occurred"+ str(e))

    def callback7(self,roll):
        try:
            self.roll.data = roll.data
            
            self.slopeX.setText(str(round(self.roll.data,1)))
   
        except Exception as e:
            print("An exception occurred"+ str(e))

    def callback8(self,yaw):
        try:
            self.yaw.data = yaw.data
            
            self.slopeZ.setText(str(round(self.yaw.data,1)))
   
        except Exception as e:
            print("An exception occurred"+ str(e))



class Worker(QObject):
 #   moveBindings = {'w':(1,0),'e':(1,-1),'a':(0,1),'d':(0,-1),'q':(1,1),'x':(-1,0),'c':(-1,1),'z':(-1,-1)}

    speedBindings={'y':(1.1,1),'h':(.9,1),'u':(1,1.1),'j':(1,.9)}
  
    key = ''


    def setKeyEmpty(self):
        self.key = ''

    def setKey(self, pressed):
        self.key = pressed


        
    def run(self):

        self.thread = QThread()
        self.thread.start()       
        pub = rospy.Publisher('hiz_mesaji', String, queue_size=5)
        #self.rate = rospy.Rate(0.000000000000000000000000000000000000000000000000000000000000001) #10hz
   
        while not rospy.is_shutdown():
            try:
                pub.publish(self.key)
                
            except Exception as e:
                print("An exception occurred"+ str(e))
             
   
   





if __name__ == "__main__":
    try:
        import sys
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
    
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)
        MainWindow.show()
        sys.exit(app.exec_())
    except Exception as e:
        print("An exception occurred"+ str(e))

    

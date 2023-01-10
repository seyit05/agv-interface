
from PyQt5.QtWidgets import*
from agv4 import Ui_MainWindow
from PyQt5.QtCore import pyqtSlot
import rospy
from std_msgs.msg import Float64

class dersler_7(QMainWindow):
    

    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.horizontalSlider_2.valueChanged['int'].connect(self.slotAngular)

        self.ui.horizontalSlider.valueChanged['int'].connect(self.slotLinear)
        
    #@pyqtSlot(int)
    #def on_horizontalSlider_valueChanged(self, current_index):

     #   self.ui.label_3.setText("değer = " + str(current_index/100))

    def slotAngular(self, angularindex):
        self.angularVelocity = 30
 
        self.angularVelocity = angularindex/100
        self.ui.label_4.setText("Açısal Hız = " + str(self.angularVelocity))
        pub = rospy.Publisher('angularVelocityData', Float64, queue_size=5)
        i = 0
        fruits = [1,2,3]
        for i in fruits:
            pub.publish(self.angularVelocity)
            
            

    def slotLinear(self, linearindex):
        
        self.linearVelocity = 20
        self.linearVelocity = linearindex/100
        self.ui.label_3.setText("Doğrusal Hız = " + str(self.linearVelocity))
        pub = rospy.Publisher('linearVelocityData', Float64, queue_size=5)
        
        i = 0
        fruits = [1,2,3]
        for i in fruits:    
            pub.publish(self.linearVelocity)



uygulama = QApplication([])
pencere = dersler_7()
pencere.show()
uygulama.exec_()
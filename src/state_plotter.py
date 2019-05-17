#!/usr/bin/env python

import rospy
from umnitsa_msgs.msg import Ultrasonic
from pyqtgraph.Qt import QtGui, QtCore
import numpy as np
import pyqtgraph as pg
import pyqtgraph.opengl as gl
from PyQt5 import QtWidgets
import time

class StatePlotter():
	def __init__(self):
		self.app = pg.QtGui.QApplication([])  # initialize QT

		#self.view = pg.GraphicsView()
		#self.view.setBackground('w')
		#pg.setConfigOption('foreground', 'k')
		#screen = QtWidgets.QDesktopWidget().availableGeometry()
		#self.view.setGeometry(screen.width()/2.,0,screen.width()/2.,screen.height())
		self.window = pg.GraphicsWindow()
		#pg.setConfigOption('foreground','k')
		#self.window.setBackground('w')
		self.window.setWindowTitle('Umnitsa State Plotter')
		self.window.show()
		#self.view.setCentralItem(self.window)
		#self.view.show()

		self.time0 = time.time()
		self.time = []
		self.ultra1 = []
		self.ultra2 = []
		self.ultra3 = []
		self.ultra4 = []



		p1 = self.window.addPlot(title="Ultrasonic 1",col=1,row=1)
		p1.setLabel('left', "Distance", units='m')
		p1.setLabel('bottom', "Time", units = 's')
		self.g1 = p1.plot(x=[0,10],y=[-10,10],pen=pg.mkPen('r',width=3,style=QtCore.Qt.DotLine))
		# p2 = self.window.addPlot(title="Ultrasonic 2",col=1,row=0)
		# self.g2 = p2.plot(pen=pg.mkPen('g',width=3,style=QtCore.Qt.DotLine))
		# p3 = self.window.addPlot(title="Ultrasonic 3",col=2,row=0)
		# self.g3 = p3.plot(pen=pg.mkPen('g',width=3,style=QtCore.Qt.DotLine))
		# #p4 = self.window.addPlot(title="Ultrasonic 4",col=3,row=0)
		# #self.g4 = p4.plot(x=[0,10],y=[0,10],pen=pg.mkPen('g',width=3,style=QtCore.Qt.DotLine))

		# self.window = gl.GLViewWidget()  # initialize the view object
		# self.window.setWindowTitle('World Viewer')
		# self.window.setGeometry(0, 0, 1500, 1500)  # args: upper_left_x, upper_right_y, width, height
		#
		# self.window.setBackgroundColor('w')  # set background color to black
		# self.window.show()  # display configured window
		print("that worked")


	def updatePlots(self,message=None):
		#print(message)
		message = np.random.random()
		self.time.append(self.time0-time.time())
		self.ultra1.append(message)
		self.g1.setData(self.time,self.ultra1)
		#self.ultra2.append(message)
		#self.ultra3.append(message)
		#self.ultra4.append(message)
		print("again")



	def subscribe(self):
		# rospy.init_node('State_Plotter', anonymous=False)
		# rospy.Subscriber('ultrasonic',Ultrasonic, self.updatePlots)
		# # spin() simply keeps python from exiting until this node is stopped
		# rospy.spin()
		while(True):
			self.updatePlots()




if __name__ == '__main__':
	try:
		subscriber = StatePlotter()
		subscriber.subscribe()
	except rospy.ROSInterruptException:
		pass

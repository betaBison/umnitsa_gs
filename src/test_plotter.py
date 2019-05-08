#!/usr/bin/env python

import rospy
from umnitsa_msgs.msg import ultrasonic
from pyqtgraph.Qt import QtGui, QtCore
import numpy as np
import pyqtgraph as pg
import pyqtgraph.opengl as gl
from PyQt5 import QtWidgets
import time

class StatePlotter():
	def __init__(self):
		win = pg.GraphicsWindow()
		win.setWindowTitle('pyqtgraph example: Scrolling Plots')
		pg.setConfigOption('foreground','k')
		win.setBackground('w')


		# 1) Simplest approach -- update data in the array such that plot appears to scroll
		#    In these examples, the array size is fixed.
		p1 = win.addPlot()
		p2 = win.addPlot()
		data1 = np.random.normal(size=300)
		curve1 = p1.plot(data1)
		curve2 = p2.plot(data1)
		ptr1 = 0
		def update1():
			global data1, curve1, ptr1
			data1[:-1] = data1[1:]  # shift data in the array one sample left
									# (see also: np.roll)
			data1[-1] = np.random.normal()
			curve1.setData(data1)

			ptr1 += 1
			curve2.setData(data1)
			curve2.setPos(ptr1, 0)



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
		# rospy.Subscriber('ultrasonic',ultrasonic, self.updatePlots)
		# # spin() simply keeps python from exiting until this node is stopped
		# rospy.spin()
		while(True):
			self.updatePlots()




if __name__ == '__main__':
	import sys
	if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
		QtGui.QApplication.instance().exec_()
	# try:
	# 	subscriber = StatePlotter()
	# 	#subscriber.subscribe()
	# except rospy.ROSInterruptException:
	# 	pass

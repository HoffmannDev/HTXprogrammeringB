import wx
import gui
import pickle

class mainFrame(gui.mainFrame):
	def __init__(self, parent):
		gui.mainFrame.__init__(self, parent)
		self.orderWindow = orderWindow(self)

	def openOrder(self, event):
		self.orderWindow.Show()

class orderWindow(gui.orderWindow):
	def __init__(self, parent):
		gui.orderWindow.__init__(self, parent)

	def placeOrder(self, event):
		pass
		


app = wx.App(False)
frame = mainFrame(None)
frame.Show(True)
app.MainLoop() 
import wx
import gui
import pickle

class mainFrame(gui.mainFrame):
	def __init__(self, parent):
		gui.mainFrame.__init__(self, parent)


app = wx.App(False)
frame = mainFrame(None)
frame.Show(True)
app.MainLoop() 
import wx
import gui
import sql

con = None
con = lite.connect('deltagere.db')
cur = con.cursor()

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
		sql = "INSER INTO deltagere (fnavn) VALUES("
		sql += self.fnavn_felt.GetValue() + ")"
		cur.execute(sql)
		cur.commit()
		


app = wx.App(False)
frame = mainFrame(None)
frame.Show(True)
app.MainLoop()
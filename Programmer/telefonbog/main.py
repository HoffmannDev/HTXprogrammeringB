import wx
import gui
import sqlite3 as lite

con = None
con = lite.connect('kontakter.db')
cur = con.cursor()

class mainFrame(gui.mainFrame):
    def __init__(self, parent):
        gui.mainFrame.__init__(self, parent)
        self.listFrame = listFrame(self)
        self.nyKontakt = nyKontakt(self)

    def exit(self, event):
        self.Close()

    def vis_kontakter(self, event):
        self.listFrame.Show()

    def ny_kontakt(self, event):
        self.nyKontakt.Show()

class listFrame(gui.listFrame):
    def __init__(self, parent):
        gui.listFrame.__init__(self, parent)
        sql = "SELECT fNavn, eNavn, tlf, adr, postnr FROM telefonbog"
        cur.execute(sql)
        rows = cur.fetchall()
        for row in rows:
            self.m_listBox1.Append(row[0] + ", " + row[1] + ", " + row[2] + ", " + row[3] + ", " + row[4])

    def luk(self, event):
        self.Hide()

    def opdater(self, event):
        self.m_listBox1.Clear()
        sql = "SELECT fNavn, eNavn, tlf, adr, postnr FROM telefonbog"
        cur.execute(sql)
        rows = cur.fetchall()
        for row in rows:
            self.m_listBox1.Append(row[0] + ", " + row[1] + "," + row[2] + ", " + row[3] + ", " + row[4])

class nyKontakt(gui.nyKontakt):
    def __init__(self, parent):
        gui.nyKontakt.__init__(self, parent)

    def gem_kontakt(self, event):
        sql ="INSERT INTO telefonbog (fNavn,eNavn,tlf,adr,postnr) VALUES ('"
        sql += self.fNavn_felt.GetValue()+"','"
        sql += self.eNavn_felt.GetValue()+"','"
        sql += self.tlf_felt.GetValue()+"','"
        sql += self.adr_felt.GetValue()+"','"
        sql += self.postnr_felt.GetValue()+"')"
        cur.execute(sql)
        self.Hide()

    def anuller(self, event):
        self.Hide()


app = wx.App(False)
frame = mainFrame(None)
frame.Show(True)
app.MainLoop()

import wx
import gui
import sqlite3 as lite
con = None
con = lite.connect('lanparty.db')
cur = con.cursor()

class gui_wx(gui.MainFrame, gui.LogInDialog, gui.BordDialog, gui.DeltagerDialog):
    def __init__(self, parent):
        gui.MainFrame.__init__(self, parent)
        sql ="SELECT id, fnavn, enavn, klasse, bord FROM deltagere"
        cur.execute(sql)
        rows = cur.fetchall()
        for row in rows:
            self.listbox_deltagere.Append(str(row[0])+" "+row[1]+", "+row[2]+", "+row[3] + "," + row[4])

    def afslut( self, event ):
        exit(0)

    def vaelgbord( self, event ):
        dlg = gui.BordDialog(self)
        res = dlg.ShowModal()
        if res == wx.ID_OK:
            valg = dlg.bordvalg.GetSelection()
            if valg == 0:
                print("Du har valgt stort bord")
            else:
                print("Du har valgt lille bord")
        dlg.Destroy()

    def login( self, event ):
        dlg = gui.LogInDialog(self)
        res = dlg.ShowModal()
        if res == wx.ID_OK:
            print(dlg.username.GetValue())
            print(dlg.pword.GetValue())
            self.vaelg_bord.Enable(True)

        if res == wx.ID_CANCEL:
            print("Cancel")

    def vis_deltager( self, event ):
        valg = self.listbox_deltagere.GetStringSelection()
        nr = valg[0]
        print(nr)

    def ny_deltager( self, event ):
        dlg = gui.DeltagerDialog(self)
        res = dlg.ShowModal()
        if res == wx.ID_OK:
            fnvn = dlg.fnavn.GetValue()
            envn = dlg.enavn.GetValue()
            klasse = dlg.klasse.GetValue()
            valg = dlg.bordvalg.GetSelection()
            if valg == 0:
                vlg = 0
            else:
                vlg = 1
            sql ="INSERT INTO deltagere (fnavn, enavn, klasse, bord) VALUES ("
            sql += "'" + fnvn + "'"
            sql += ", '" + envn + "'"
            sql += ", '"+klasse+"'"
            sql += ", '"+str(vlg)+"'"
            sql += ")"
            cur.execute(sql)
            con.commit()

app = wx.App(False)
frame = gui_wx(None)
frame.Show(True)
app.MainLoop()
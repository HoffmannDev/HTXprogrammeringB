# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MainFrame
###########################################################################

class MainFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Lan Program", pos = wx.DefaultPosition, size = wx.Size( 558,342 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		self.m_menubar1 = wx.MenuBar( 0 )
		self.m_menu1 = wx.Menu()
		self.m_menuItem1 = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"Log in", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.Append( self.m_menuItem1 )

		self.m_menuItem2 = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"Exit", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.Append( self.m_menuItem2 )

		self.m_menubar1.Append( self.m_menu1, u"File" )

		self.m_menu6 = wx.Menu()
		self.vaelg_bord = wx.MenuItem( self.m_menu6, wx.ID_ANY, u"Vælg bord", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu6.Append( self.vaelg_bord )
		self.vaelg_bord.Enable( False )

		self.m_menuItem4 = wx.MenuItem( self.m_menu6, wx.ID_ANY, u"Ny deltager", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu6.Append( self.m_menuItem4 )

		self.m_menubar1.Append( self.m_menu6, u"Edit" )

		self.SetMenuBar( self.m_menubar1 )

		bSizer3 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Deltagerliste", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )

		self.m_staticText1.SetFont( wx.Font( 18, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer3.Add( self.m_staticText1, 0, wx.ALL, 5 )

		listbox_deltagereChoices = []
		self.listbox_deltagere = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, listbox_deltagereChoices, 0 )
		bSizer3.Add( self.listbox_deltagere, 1, wx.ALL, 5 )

		self.opdaterKnap = wx.Button( self, wx.ID_ANY, u"Opdater", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.opdaterKnap, 0, wx.ALL, 5 )


		self.SetSizer( bSizer3 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_MENU, self.login, id = self.m_menuItem1.GetId() )
		self.Bind( wx.EVT_MENU, self.afslut, id = self.m_menuItem2.GetId() )
		self.Bind( wx.EVT_MENU, self.vaelgbord, id = self.vaelg_bord.GetId() )
		self.Bind( wx.EVT_MENU, self.ny_deltager, id = self.m_menuItem4.GetId() )
		self.listbox_deltagere.Bind( wx.EVT_LISTBOX, self.vis_deltager )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def login( self, event ):
		event.Skip()

	def afslut( self, event ):
		event.Skip()

	def vaelgbord( self, event ):
		event.Skip()

	def ny_deltager( self, event ):
		event.Skip()

	def vis_deltager( self, event ):
		event.Skip()


###########################################################################
## Class DeltagerDialog
###########################################################################

class DeltagerDialog ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Ny Deltager", pos = wx.DefaultPosition, size = wx.Size( 379,258 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer4 = wx.BoxSizer( wx.VERTICAL )

		bSizer5 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"Fornavn:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )

		bSizer5.Add( self.m_staticText2, 0, wx.ALL, 5 )

		self.fnavn = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.fnavn, 0, wx.ALL, 5 )

		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"Efternavn:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )

		bSizer5.Add( self.m_staticText3, 0, wx.ALL, 5 )

		self.enavn = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.enavn, 0, wx.ALL, 5 )


		bSizer4.Add( bSizer5, 0, wx.EXPAND, 5 )

		bSizer6 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"Klasse:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )

		bSizer6.Add( self.m_staticText4, 0, wx.ALL, 5 )

		self.klasse = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer6.Add( self.klasse, 0, wx.ALL, 5 )


		bSizer4.Add( bSizer6, 0, wx.EXPAND, 5 )

		bordvalgChoices = [ u"Stort Bord", u"Lille Bord" ]
		self.bordvalg = wx.RadioBox( self, wx.ID_ANY, u"Vælg bord", wx.DefaultPosition, wx.DefaultSize, bordvalgChoices, 1, wx.RA_SPECIFY_COLS )
		self.bordvalg.SetSelection( 0 )
		bSizer4.Add( self.bordvalg, 0, wx.ALL, 5 )

		m_sdbSizer4 = wx.StdDialogButtonSizer()
		self.m_sdbSizer4OK = wx.Button( self, wx.ID_OK )
		m_sdbSizer4.AddButton( self.m_sdbSizer4OK )
		self.m_sdbSizer4Cancel = wx.Button( self, wx.ID_CANCEL )
		m_sdbSizer4.AddButton( self.m_sdbSizer4Cancel )
		m_sdbSizer4.Realize();

		bSizer4.Add( m_sdbSizer4, 0, wx.EXPAND, 5 )


		self.SetSizer( bSizer4 )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


###########################################################################
## Class LogInDialog
###########################################################################

class LogInDialog ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Log in", pos = wx.DefaultPosition, size = wx.Size( 188,140 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		bSizer7 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"Brugernavn:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )

		bSizer7.Add( self.m_staticText5, 0, wx.ALL, 5 )

		self.username = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer7.Add( self.username, 0, wx.ALL, 5 )


		bSizer1.Add( bSizer7, 1, wx.EXPAND, 5 )

		bSizer9 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, u"Adgangskode:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )

		bSizer9.Add( self.m_staticText6, 0, wx.ALL, 5 )

		self.pword = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer9.Add( self.pword, 0, wx.ALL, 5 )


		bSizer1.Add( bSizer9, 1, wx.EXPAND, 5 )

		m_sdbSizer1 = wx.StdDialogButtonSizer()
		self.m_sdbSizer1OK = wx.Button( self, wx.ID_OK )
		m_sdbSizer1.AddButton( self.m_sdbSizer1OK )
		self.m_sdbSizer1Cancel = wx.Button( self, wx.ID_CANCEL )
		m_sdbSizer1.AddButton( self.m_sdbSizer1Cancel )
		m_sdbSizer1.Realize();

		bSizer1.Add( m_sdbSizer1, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


###########################################################################
## Class BordDialog
###########################################################################

class BordDialog ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Vælg Bord", pos = wx.DefaultPosition, size = wx.Size( 296,185 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		bordvalgChoices = [ u"Stort bord", u"Lille bord" ]
		self.bordvalg = wx.RadioBox( self, wx.ID_ANY, u"Vælg bord", wx.DefaultPosition, wx.DefaultSize, bordvalgChoices, 1, wx.RA_SPECIFY_COLS )
		self.bordvalg.SetSelection( 0 )
		bSizer2.Add( self.bordvalg, 0, wx.ALL, 5 )

		m_sdbSizer2 = wx.StdDialogButtonSizer()
		self.m_sdbSizer2OK = wx.Button( self, wx.ID_OK )
		m_sdbSizer2.AddButton( self.m_sdbSizer2OK )
		self.m_sdbSizer2Cancel = wx.Button( self, wx.ID_CANCEL )
		m_sdbSizer2.AddButton( self.m_sdbSizer2Cancel )
		m_sdbSizer2.Realize();

		bSizer2.Add( m_sdbSizer2, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer2 )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass



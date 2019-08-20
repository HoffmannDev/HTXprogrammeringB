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
## Class mainFrame
###########################################################################

class mainFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Telefonbog", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		self.m_menubar1 = wx.MenuBar( 0 )
		self.m_file = wx.Menu()
		self.m_exit = wx.MenuItem( self.m_file, wx.ID_ANY, u"Exit", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_file.Append( self.m_exit )

		self.m_menubar1.Append( self.m_file, u"File" )

		self.m_edit = wx.Menu()
		self.m_tilføjKontakt = wx.MenuItem( self.m_edit, wx.ID_ANY, u"Tilføj kontakt", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_edit.Append( self.m_tilføjKontakt )

		self.m_menubar1.Append( self.m_edit, u"Edit" )

		self.m_view = wx.Menu()
		self.m_seKontakt = wx.MenuItem( self.m_view, wx.ID_ANY, u"Se kontakter", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_view.Append( self.m_seKontakt )

		self.m_menubar1.Append( self.m_view, u"View" )

		self.SetMenuBar( self.m_menubar1 )

		bSizer3 = wx.BoxSizer( wx.VERTICAL )


		bSizer3.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		bSizer4 = wx.BoxSizer( wx.HORIZONTAL )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_seKontakt2 = wx.Button( self, wx.ID_ANY, u"Se kontakter", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.m_seKontakt2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_tilføjKontakt2 = wx.Button( self, wx.ID_ANY, u"Tilføj Kontakt", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.m_tilføjKontakt2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer3.Add( bSizer4, 1, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer3.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer3 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_MENU, self.exit, id = self.m_exit.GetId() )
		self.Bind( wx.EVT_MENU, self.vis_kontakter, id = self.m_seKontakt.GetId() )
		self.m_seKontakt2.Bind( wx.EVT_BUTTON, self.vis_kontakter )
		self.m_tilføjKontakt2.Bind( wx.EVT_BUTTON, self.ny_kontakt )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def exit( self, event ):
		event.Skip()

	def vis_kontakter( self, event ):
		event.Skip()


	def ny_kontakt( self, event ):
		event.Skip()


###########################################################################
## Class listFrame
###########################################################################

class listFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Kontaktliste", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer1 = wx.BoxSizer( wx.HORIZONTAL )

		m_listBox1Choices = []
		self.m_listBox1 = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 300,250 ), m_listBox1Choices, 0 )
		bSizer1.Add( self.m_listBox1, 0, wx.ALL, 5 )

		bSizer3 = wx.BoxSizer( wx.VERTICAL )


		bSizer3.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_opdater = wx.Button( self, wx.ID_ANY, u"Opdater", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.m_opdater, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_luk = wx.Button( self, wx.ID_ANY, u"Luk", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.m_luk, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer3.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer1.Add( bSizer3, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_opdater.Bind( wx.EVT_BUTTON, self.opdater )
		self.m_luk.Bind( wx.EVT_BUTTON, self.luk )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def opdater( self, event ):
		event.Skip()

	def luk( self, event ):
		event.Skip()


###########################################################################
## Class nyKontakt
###########################################################################

class nyKontakt ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Ny kontakt", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer5 = wx.BoxSizer( wx.VERTICAL )

		bSizer7 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Fornavn", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )

		bSizer7.Add( self.m_staticText1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.fNavn_felt = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer7.Add( self.fNavn_felt, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer5.Add( bSizer7, 1, wx.EXPAND, 5 )

		bSizer71 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"Efternavn", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )

		bSizer71.Add( self.m_staticText2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.eNavn_felt = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer71.Add( self.eNavn_felt, 0, wx.ALL, 5 )


		bSizer5.Add( bSizer71, 1, wx.EXPAND, 5 )

		bSizer8 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"Telefon", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )

		bSizer8.Add( self.m_staticText3, 0, wx.ALL, 5 )

		self.tlf_felt = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer8.Add( self.tlf_felt, 0, wx.ALL, 5 )


		bSizer5.Add( bSizer8, 1, wx.EXPAND, 5 )

		bSizer9 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"Adresse", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )

		bSizer9.Add( self.m_staticText5, 0, wx.ALL, 5 )

		self.adr_felt = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer9.Add( self.adr_felt, 0, wx.ALL, 5 )


		bSizer5.Add( bSizer9, 1, wx.EXPAND, 5 )

		bSizer11 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, u"Postnummer", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )

		bSizer11.Add( self.m_staticText6, 0, wx.ALL, 5 )

		self.postnr_felt = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer11.Add( self.postnr_felt, 0, wx.ALL, 5 )


		bSizer5.Add( bSizer11, 1, wx.EXPAND, 5 )

		self.m_gemKontakt = wx.Button( self, wx.ID_ANY, u"Gem", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.m_gemKontakt, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_anuller = wx.Button( self, wx.ID_ANY, u"Anuller", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.m_anuller, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.SetSizer( bSizer5 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_gemKontakt.Bind( wx.EVT_BUTTON, self.gem_kontakt )
		self.m_anuller.Bind( wx.EVT_BUTTON, self.anuller )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def gem_kontakt( self, event ):
		event.Skip()

	def anuller( self, event ):
		event.Skip()



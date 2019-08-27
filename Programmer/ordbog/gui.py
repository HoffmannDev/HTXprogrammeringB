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
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"Hoffmanns Custom Dictionary", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )

		bSizer1.Add( self.m_staticText2, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_button4 = wx.Button( self, wx.ID_ANY, u"Find word", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.m_button4, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_button5 = wx.Button( self, wx.ID_ANY, u"Add word", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.m_button5, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_button6 = wx.Button( self, wx.ID_ANY, u"Exit", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.m_button6, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


###########################################################################
## Class addWord
###########################################################################

class addWord ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Add word", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer6 = wx.BoxSizer( wx.VERTICAL )

		bSizer7 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"Danish Word", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )

		bSizer7.Add( self.m_staticText4, 0, wx.ALL, 5 )

		self.danishWord = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer7.Add( self.danishWord, 0, wx.ALL, 5 )


		bSizer6.Add( bSizer7, 0, wx.EXPAND, 5 )

		bSizer8 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, u"English Word", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )

		bSizer8.Add( self.m_staticText6, 0, wx.ALL, 5 )

		self.englishWord = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer8.Add( self.englishWord, 0, wx.ALL, 5 )


		bSizer6.Add( bSizer8, 0, wx.EXPAND, 5 )

		self.addWordBtn = wx.Button( self, wx.ID_ANY, u"Add word", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer6.Add( self.addWordBtn, 0, wx.ALL, 5 )


		self.SetSizer( bSizer6 )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


###########################################################################
## Class findWord
###########################################################################

class findWord ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Find word", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer11 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer12 = wx.BoxSizer( wx.VERTICAL )

		self.search = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer12.Add( self.search, 0, wx.ALL, 5 )

		self.searchBtn = wx.Button( self, wx.ID_ANY, u"Search", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer12.Add( self.searchBtn, 0, wx.ALL, 5 )


		bSizer11.Add( bSizer12, 0, wx.EXPAND, 5 )

		self.showAllBtn = wx.Button( self, wx.ID_ANY, u"Show all", wx.Point( -1,-1 ), wx.DefaultSize, 0 )
		bSizer11.Add( self.showAllBtn, 0, wx.ALL, 5 )

		m_listBox2Choices = []
		self.m_listBox2 = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,250 ), m_listBox2Choices, 0 )
		bSizer11.Add( self.m_listBox2, 0, wx.ALL, 5 )


		self.SetSizer( bSizer11 )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass



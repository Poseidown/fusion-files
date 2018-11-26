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
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Fusion Files", pos = wx.DefaultPosition, size = wx.Size( 600,800 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )

		bSizer73 = wx.BoxSizer( wx.VERTICAL )

		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		bSizer14 = wx.BoxSizer( wx.HORIZONTAL )


		bSizer14.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.GuiTitleLabel = wx.StaticText( self, wx.ID_ANY, u"Fusion Files", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
		self.GuiTitleLabel.Wrap( -1 )

		self.GuiTitleLabel.SetFont( wx.Font( 36, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Georgia" ) )
		self.GuiTitleLabel.SetForegroundColour( wx.Colour( 65, 230, 17 ) )

		bSizer14.Add( self.GuiTitleLabel, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		bSizer14.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer2.Add( bSizer14, 0, wx.EXPAND, 5 )

		self.MainPanel = wx.ScrolledWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )
		self.MainPanel.SetScrollRate( 5, 5 )
		self.MainPanel.SetForegroundColour( wx.Colour( 65, 230, 17 ) )
		self.MainPanel.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOTEXT ) )

		bSizer3 = wx.BoxSizer( wx.VERTICAL )

		sbSizer2 = wx.StaticBoxSizer( wx.StaticBox( self.MainPanel, wx.ID_ANY, u"Load Legitimate File\n" ), wx.VERTICAL )

		self.LegitFilePanel = wx.Panel( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer421 = wx.BoxSizer( wx.HORIZONTAL )

		self.LoadLegitFile = wx.FilePickerCtrl( self.LegitFilePanel, wx.ID_ANY, wx.EmptyString, u"Select Legitimate File", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_FILE_MUST_EXIST|wx.FLP_OPEN|wx.FLP_SMALL )
		self.LoadLegitFile.SetToolTip( u"Can be any file type." )

		bSizer421.Add( self.LoadLegitFile, 0, wx.ALL, 5 )

		self.LegitFileLabel = wx.StaticText( self.LegitFilePanel, wx.ID_ANY, u"File:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.LegitFileLabel.Wrap( -1 )

		self.LegitFileLabel.SetFont( wx.Font( 10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial" ) )
		self.LegitFileLabel.SetForegroundColour( wx.Colour( 65, 230, 17 ) )

		bSizer421.Add( self.LegitFileLabel, 0, wx.ALL, 5 )

		self.LegitFileTextCtrl = wx.StaticText( self.LegitFilePanel, wx.ID_ANY, u"None", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.LegitFileTextCtrl.Wrap( -1 )

		self.LegitFileTextCtrl.SetForegroundColour( wx.Colour( 65, 230, 17 ) )

		bSizer421.Add( self.LegitFileTextCtrl, 0, wx.ALL, 5 )


		self.LegitFilePanel.SetSizer( bSizer421 )
		self.LegitFilePanel.Layout()
		bSizer421.Fit( self.LegitFilePanel )
		sbSizer2.Add( self.LegitFilePanel, 1, wx.EXPAND |wx.ALL, 5 )


		bSizer3.Add( sbSizer2, 1, wx.EXPAND, 5 )

		sbSizer4 = wx.StaticBoxSizer( wx.StaticBox( self.MainPanel, wx.ID_ANY, u"Load Payload File" ), wx.VERTICAL )

		self.PayloadFilePanel = wx.Panel( sbSizer4.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer41 = wx.BoxSizer( wx.HORIZONTAL )

		self.LoadPayloadFile = wx.FilePickerCtrl( self.PayloadFilePanel, wx.ID_ANY, wx.EmptyString, u"Select Malicious File", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_FILE_MUST_EXIST|wx.FLP_OPEN|wx.FLP_SMALL )
		self.LoadPayloadFile.SetToolTip( u"Can be any file type." )

		bSizer41.Add( self.LoadPayloadFile, 0, wx.ALL, 5 )

		self.PayloadFileLable = wx.StaticText( self.PayloadFilePanel, wx.ID_ANY, u"File:", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_LEFT )
		self.PayloadFileLable.Wrap( -1 )

		self.PayloadFileLable.SetFont( wx.Font( 10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial" ) )
		self.PayloadFileLable.SetForegroundColour( wx.Colour( 65, 230, 17 ) )

		bSizer41.Add( self.PayloadFileLable, 0, wx.ALL, 5 )

		self.PayloadFileTextCtrl = wx.StaticText( self.PayloadFilePanel, wx.ID_ANY, u"None", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.PayloadFileTextCtrl.Wrap( -1 )

		self.PayloadFileTextCtrl.SetForegroundColour( wx.Colour( 65, 230, 17 ) )

		bSizer41.Add( self.PayloadFileTextCtrl, 0, wx.ALL, 5 )


		self.PayloadFilePanel.SetSizer( bSizer41 )
		self.PayloadFilePanel.Layout()
		bSizer41.Fit( self.PayloadFilePanel )
		sbSizer4.Add( self.PayloadFilePanel, 1, wx.EXPAND |wx.ALL, 5 )


		bSizer3.Add( sbSizer4, 1, wx.EXPAND, 5 )

		sbSizer5 = wx.StaticBoxSizer( wx.StaticBox( self.MainPanel, wx.ID_ANY, u"Version File (Optional)" ), wx.VERTICAL )

		self.VersionFilePanel = wx.Panel( sbSizer5.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer411 = wx.BoxSizer( wx.HORIZONTAL )

		self.LoadVersionFile = wx.FilePickerCtrl( self.VersionFilePanel, wx.ID_ANY, wx.EmptyString, u"Select Version File", u"*.py", wx.DefaultPosition, wx.DefaultSize, wx.FLP_FILE_MUST_EXIST|wx.FLP_OPEN|wx.FLP_SMALL )
		self.LoadVersionFile.SetToolTip( u"In the resources folder, you have an example version_template.py. Customize your own!" )

		bSizer411.Add( self.LoadVersionFile, 0, wx.ALL, 5 )

		self.VersionFileLabel = wx.StaticText( self.VersionFilePanel, wx.ID_ANY, u"File:", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_LEFT )
		self.VersionFileLabel.Wrap( -1 )

		self.VersionFileLabel.SetFont( wx.Font( 10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial" ) )
		self.VersionFileLabel.SetForegroundColour( wx.Colour( 65, 230, 17 ) )

		bSizer411.Add( self.VersionFileLabel, 0, wx.ALL, 5 )

		self.VersionFileTextCtrl = wx.StaticText( self.VersionFilePanel, wx.ID_ANY, u"None", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.VersionFileTextCtrl.Wrap( -1 )

		self.VersionFileTextCtrl.SetForegroundColour( wx.Colour( 65, 230, 17 ) )

		bSizer411.Add( self.VersionFileTextCtrl, 0, wx.ALL, 5 )


		self.VersionFilePanel.SetSizer( bSizer411 )
		self.VersionFilePanel.Layout()
		bSizer411.Fit( self.VersionFilePanel )
		sbSizer5.Add( self.VersionFilePanel, 1, wx.EXPAND |wx.ALL, 5 )


		bSizer3.Add( sbSizer5, 1, wx.EXPAND, 5 )

		sbSizer51 = wx.StaticBoxSizer( wx.StaticBox( self.MainPanel, wx.ID_ANY, u"Icon File (Optional)" ), wx.VERTICAL )

		self.IconFilePanel = wx.Panel( sbSizer51.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer4111 = wx.BoxSizer( wx.HORIZONTAL )

		self.LoadIconFile = wx.FilePickerCtrl( self.IconFilePanel, wx.ID_ANY, wx.EmptyString, u"Select Icon File", u"*.ico", wx.DefaultPosition, wx.DefaultSize, wx.FLP_FILE_MUST_EXIST|wx.FLP_OPEN|wx.FLP_SMALL )
		self.LoadIconFile.SetToolTip( u"In the resources folder you will find some useful icon files." )

		bSizer4111.Add( self.LoadIconFile, 0, wx.ALL, 5 )

		self.IconFileLabel = wx.StaticText( self.IconFilePanel, wx.ID_ANY, u"File:", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_LEFT )
		self.IconFileLabel.Wrap( -1 )

		self.IconFileLabel.SetFont( wx.Font( 10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial" ) )
		self.IconFileLabel.SetForegroundColour( wx.Colour( 65, 230, 17 ) )

		bSizer4111.Add( self.IconFileLabel, 0, wx.ALL, 5 )

		self.IconFileTextCtrl = wx.StaticText( self.IconFilePanel, wx.ID_ANY, u"None", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.IconFileTextCtrl.Wrap( -1 )

		self.IconFileTextCtrl.SetForegroundColour( wx.Colour( 65, 230, 17 ) )

		bSizer4111.Add( self.IconFileTextCtrl, 0, wx.ALL, 5 )


		self.IconFilePanel.SetSizer( bSizer4111 )
		self.IconFilePanel.Layout()
		bSizer4111.Fit( self.IconFilePanel )
		sbSizer51.Add( self.IconFilePanel, 1, wx.EXPAND |wx.ALL, 5 )


		bSizer3.Add( sbSizer51, 1, wx.EXPAND, 5 )


		self.MainPanel.SetSizer( bSizer3 )
		self.MainPanel.Layout()
		bSizer3.Fit( self.MainPanel )
		bSizer2.Add( self.MainPanel, 1, wx.EXPAND |wx.ALL, 5 )


		bSizer73.Add( bSizer2, 1, wx.EXPAND, 5 )

		bSizer24 = wx.BoxSizer( wx.VERTICAL )

		bSizer24.SetMinSize( wx.Size( -1,150 ) )
		bSizer12 = wx.BoxSizer( wx.HORIZONTAL )

		self.lblAdditionalOptions = wx.StaticText( self, wx.ID_ANY, u"Additional Options:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblAdditionalOptions.Wrap( -1 )

		self.lblAdditionalOptions.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial" ) )
		self.lblAdditionalOptions.SetForegroundColour( wx.Colour( 0, 255, 0 ) )

		bSizer12.Add( self.lblAdditionalOptions, 0, wx.ALL, 5 )

		self.chkAntiVM = wx.CheckBox( self, wx.ID_ANY, u"Anti VM", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.chkAntiVM.SetForegroundColour( wx.Colour( 0, 255, 0 ) )

		bSizer12.Add( self.chkAntiVM, 0, wx.ALL, 5 )


		bSizer12.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.chkDelay = wx.CheckBox( self, wx.ID_ANY, u"Delay", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.chkDelay.SetForegroundColour( wx.Colour( 0, 255, 0 ) )

		bSizer12.Add( self.chkDelay, 0, wx.ALL, 5 )

		self.txtDelaySeconds = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 40,-1 ), 0 )
		bSizer12.Add( self.txtDelaySeconds, 0, wx.ALL, 5 )

		self.lblDelaySeconds = wx.StaticText( self, wx.ID_ANY, u"Seconds", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblDelaySeconds.Wrap( -1 )

		self.lblDelaySeconds.SetForegroundColour( wx.Colour( 0, 255, 0 ) )

		bSizer12.Add( self.lblDelaySeconds, 0, wx.ALL, 5 )


		bSizer12.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer24.Add( bSizer12, 1, wx.EXPAND, 5 )

		bSizer141 = wx.BoxSizer( wx.HORIZONTAL )

		self.OutFileLabel = wx.StaticText( self, wx.ID_ANY, u"Output File Name:", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
		self.OutFileLabel.Wrap( -1 )

		self.OutFileLabel.SetFont( wx.Font( 10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial" ) )
		self.OutFileLabel.SetForegroundColour( wx.Colour( 65, 230, 17 ) )
		self.OutFileLabel.SetToolTip( u"Name of the final executable" )

		bSizer141.Add( self.OutFileLabel, 0, wx.ALL, 5 )

		self.OutputFileTextCtrl = wx.TextCtrl( self, wx.ID_ANY, u"payload.pdf", wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		self.OutputFileTextCtrl.SetToolTip( u"You do not need to include file extension, but can if you want to spoof it. (example: payload.pdf would result in payload.pdf.exe)" )

		bSizer141.Add( self.OutputFileTextCtrl, 0, wx.ALL, 5 )

		self.EncryptDropperCheckBox = wx.CheckBox( self, wx.ID_ANY, u"Encrypt", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.EncryptDropperCheckBox.SetValue(True)
		self.EncryptDropperCheckBox.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial" ) )
		self.EncryptDropperCheckBox.SetForegroundColour( wx.Colour( 65, 230, 17 ) )
		self.EncryptDropperCheckBox.SetToolTip( u"Encrypt the binded files providing SCAN TIME FUD." )

		bSizer141.Add( self.EncryptDropperCheckBox, 0, wx.ALL, 5 )


		bSizer141.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText13 = wx.StaticText( self, wx.ID_ANY, u"Drop to:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText13.Wrap( -1 )

		self.m_staticText13.SetForegroundColour( wx.Colour( 65, 230, 17 ) )

		bSizer141.Add( self.m_staticText13, 0, wx.ALL, 5 )

		SystemEnvChoiceChoices = [ u"HOMEPATH", u"TEMP", u"APPDATA" ]
		self.SystemEnvChoice = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, SystemEnvChoiceChoices, 0 )
		self.SystemEnvChoice.SetSelection( 2 )
		self.SystemEnvChoice.SetForegroundColour( wx.Colour( 65, 230, 17 ) )
		self.SystemEnvChoice.SetToolTip( u"Drops both files to:\nHOMEPATH: C:\\Users\\USERNAME\\HERE\nTEMP: %TEMP%\\HERE\nAPPDATA: %APPDATA%\\HERE" )

		bSizer141.Add( self.SystemEnvChoice, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		bSizer141.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer24.Add( bSizer141, 1, wx.EXPAND, 5 )

		self.ConsoleBoxTextCtrl = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TE_MULTILINE|wx.TE_READONLY )
		self.ConsoleBoxTextCtrl.SetForegroundColour( wx.Colour( 65, 230, 17 ) )
		self.ConsoleBoxTextCtrl.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		self.ConsoleBoxTextCtrl.SetMinSize( wx.Size( -1,150 ) )

		bSizer24.Add( self.ConsoleBoxTextCtrl, 0, wx.ALL|wx.EXPAND, 5 )

		bSizer271 = wx.BoxSizer( wx.HORIZONTAL )

		self.BuildButton = wx.Button( self, wx.ID_ANY, u"Combine Files", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer271.Add( self.BuildButton, 0, wx.ALL, 5 )


		bSizer271.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.SaveConfigLabel = wx.StaticText( self, wx.ID_ANY, u"Save Config", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.SaveConfigLabel.Wrap( -1 )

		self.SaveConfigLabel.SetFont( wx.Font( 10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial" ) )
		self.SaveConfigLabel.SetForegroundColour( wx.Colour( 65, 230, 17 ) )

		bSizer271.Add( self.SaveConfigLabel, 0, wx.ALL, 5 )

		self.SaveConfigFile = wx.FilePickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Save As", u"*.json", wx.DefaultPosition, wx.DefaultSize, wx.FLP_OVERWRITE_PROMPT|wx.FLP_SAVE|wx.FLP_SMALL )
		bSizer271.Add( self.SaveConfigFile, 0, wx.ALL, 5 )


		bSizer271.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText15 = wx.StaticText( self, wx.ID_ANY, u"Load Config", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText15.Wrap( -1 )

		self.m_staticText15.SetFont( wx.Font( 10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial" ) )
		self.m_staticText15.SetForegroundColour( wx.Colour( 65, 230, 17 ) )

		bSizer271.Add( self.m_staticText15, 0, wx.ALL, 5 )

		self.LoadConfigFile = wx.FilePickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select Config File", u"*.json", wx.DefaultPosition, wx.DefaultSize, wx.FLP_FILE_MUST_EXIST|wx.FLP_OPEN|wx.FLP_SMALL )
		self.LoadConfigFile.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		bSizer271.Add( self.LoadConfigFile, 0, wx.ALL, 5 )


		bSizer271.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.ClearOptionsButton = wx.Button( self, wx.ID_ANY, u"Clear", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer271.Add( self.ClearOptionsButton, 0, wx.ALL, 5 )


		bSizer24.Add( bSizer271, 1, wx.EXPAND, 5 )


		bSizer73.Add( bSizer24, 0, wx.EXPAND, 5 )


		self.SetSizer( bSizer73 )
		self.Layout()
		self.StatusBar = self.CreateStatusBar( 1, wx.STB_SIZEGRIP, wx.ID_ANY )

		self.Centre( wx.BOTH )

		# Connect Events
		self.LoadLegitFile.Bind( wx.EVT_FILEPICKER_CHANGED, self.UpdateLegitFile )
		self.LoadPayloadFile.Bind( wx.EVT_FILEPICKER_CHANGED, self.UpdatePayloadFile )
		self.LoadVersionFile.Bind( wx.EVT_FILEPICKER_CHANGED, self.UpdateVersionFile )
		self.LoadIconFile.Bind( wx.EVT_FILEPICKER_CHANGED, self.UpdateIconFile )
		self.BuildButton.Bind( wx.EVT_BUTTON, self.BuildFinal )
		self.SaveConfigFile.Bind( wx.EVT_FILEPICKER_CHANGED, self.CreateConfig )
		self.LoadConfigFile.Bind( wx.EVT_FILEPICKER_CHANGED, self.ReadConfig )
		self.ClearOptionsButton.Bind( wx.EVT_BUTTON, self.ClearOptions )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def UpdateLegitFile( self, event ):
		event.Skip()

	def UpdatePayloadFile( self, event ):
		event.Skip()

	def UpdateVersionFile( self, event ):
		event.Skip()

	def UpdateIconFile( self, event ):
		event.Skip()

	def BuildFinal( self, event ):
		event.Skip()

	def CreateConfig( self, event ):
		event.Skip()

	def ReadConfig( self, event ):
		event.Skip()

	def ClearOptions( self, event ):
		event.Skip()



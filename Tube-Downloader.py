#!/usr/bin/env python3
import os
import wx
import wx.lib.filebrowsebutton
from pytube import YouTube
from logger import get_logger
from util import delete_file
#import wx.lib.inspection

log = get_logger('tube-downloader.py')

class MyFrame(wx.Frame):
    # class member variables
    out_path = ''
    request_url = ''
    resolution_px = '480'
    file_name = ''
    yt = ''
    error_exists = False

    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=wx.Size(500, 257))

        #-------------Widgets----------------------
        label1 = wx.StaticText(self, label='URL: ')
        self.input1 = wx.TextCtrl(self)

        self.dirInput = wx.lib.filebrowsebutton.DirBrowseButton(self, labelText = 'Path:',
                                                            buttonText = '...',
                                                            toolTip='Type directory name or browse to select where do you want to save your video/audio'
                                                            )

        label3 = wx.StaticText(self, label='Quality: ')
        self.input3 = wx.Choice(self, choices=['1080p', '720p', '480p', '360p', '240p', '144p'])

        label4 = wx.StaticText(self, label='File Name: ')
        self.input4 = wx.TextCtrl(self)

        downloadBtn = wx.Button(self, label='Download')
        self.Bind(wx.EVT_BUTTON, self.onDownload, downloadBtn)
        #testBtn = wx.Button(self, label='Test')
        #self.Bind(wx.EVT_BUTTON, self.onTest, testBtn)

        #--------------------Sizers--------------------
        mainSizer = wx.BoxSizer(wx.VERTICAL)
        input1Sizer = wx.BoxSizer(wx.HORIZONTAL)
        input2Sizer = wx.BoxSizer()
        input3Sizer = wx.BoxSizer()
        input4Sizer = wx.BoxSizer()
        downBtnSizer = wx.BoxSizer()


        input1Sizer.Add(window=label1, proportion=0, flag=wx.ALL, border=12)
        input1Sizer.Add(window=self.input1, proportion=1, flag=wx.ALL|wx.EXPAND, border=5)

        input2Sizer.Add(window=self.dirInput, proportion=1, flag=wx.ALL|wx.EXPAND, border=5)

        input3Sizer.Add(window=label3, proportion=0, flag=wx.ALL, border=12)
        input3Sizer.Add(window=self.input3, proportion=1, flag=wx.ALL|wx.EXPAND, border=5)

        input4Sizer.Add(window=label4, proportion=0, flag=wx.ALL, border=12)
        input4Sizer.Add(window=self.input4, proportion=1, flag=wx.ALL|wx.EXPAND, border=5)

        downBtnSizer.Add(window=downloadBtn, proportion=1, flag=wx.ALL|wx.EXPAND, border=5)
        #downBtnSizer.Add(window=testBtn, proportion=0, flag=wx.ALL, border=5)

        mainSizer.Add(input1Sizer, 0, wx.ALL|wx.EXPAND, 0)
        mainSizer.Add(input2Sizer, 0, wx.ALL|wx.EXPAND, 0)
        mainSizer.Add(input3Sizer, 0, wx.ALL|wx.EXPAND, 0)
        mainSizer.Add(input4Sizer, 0, wx.ALL|wx.EXPAND, 0)
        mainSizer.Add(downBtnSizer, 0, wx.ALL|wx.EXPAND, 0)


        self.SetSizer(mainSizer)
        #mainSizer.Fit(self)  #This will fir all the widgets in the smallest frame size possible
        self.Layout()
        #wx.lib.inspection.InspectionTool().Show()
        self.Show(True)

    def getInputData(self):

        self.request_url = self.input1.GetValue() #https://www.youtube.com/watch?v=O2deXwf4drE // https://www.youtube.com/watch?v=ARoe7vXa1Ek
        self.resolution_px = self.input3.GetString(n=self.input3.GetSelection())
        self.out_path = self.dirInput.GetValue()
        self.file_name = self.input4.GetValue()
        self.yt = YouTube(self.request_url)
        #if fileName == '':
            #fileName = yt.title

     #def onTest(self, e):
         #pass

    def messageBox(self, msg):
        dlg = wx.RichMessageDialog(self, message=msg, style=wx.OK|wx.CENTER)
        dlg.ShowModal()

    def checkUserInput(self):
        if self.out_path[-1] == '/' or ' ' in self.file_name:
            self.messageBox('[Error] make sure that:\n- The filename does not have spaces\n- The output path does not end with "/"')
            self.error_exists = True
        else:
            self.error_exists = False

    def download_video(self):
        log.info('>>> Downloading video...')
        self.yt.streams.filter(res=self.resolution_px, subtype='mp4').first().download(self.out_path, 'video') #, only_video=True, subtype='mp4'
    
    def download_audio(self):
        log.info('>>> Downloading audio..')
        self.yt.streams.get_audio_only(subtype='mp4').download(self.out_path, 'audio')
    
    def generate_media_file(self):
        log.info('>>> Combining audio and video...')
        ffmpeg_exec_path = f'ffmpeg -i {self.out_path}/video.mp4 -i {self.out_path}/audio.mp4 -c copy -map 0:v:0 -map 1:a:0 {self.out_path}/{self.file_name}.mp4'
        os.system(ffmpeg_exec_path)
        
    def remove_temp_files(self):
        file_temp_video = f'{self.out_path}/video.mp4'
        file_temp_audio = f'{self.out_path}/audio.mp4'
        delete_file(file_temp_video)
        delete_file(file_temp_audio)

    def onDownload(self, e):
        try:
            self.getInputData()
            self.checkUserInput()
            if self.error_exists:
                log.error('Oops! there seems to be an error.')
                return
            log.info('>>> Download started...')
            self.download_video()
            self.download_audio()
            self.generate_media_file()
            self.remove_temp_files()
            self.messageBox('Download finished!')  
        except:
            self.messageBox('[Error] either:\n- Invalid link\n- Resolution is not supported by the video')
            self.error(f'Failed to complete download procedure with error: {sys.exc_info()[0]}')

if __name__ == "__main__":
    app = wx.App(False)
    frame = MyFrame(None, 'Tube-Downloader')
    app.MainLoop()

import shutil
import os
import time
import datetime
import wx

class windowClass(wx.Frame):

    def __init__(self, *args, **kwargs):
        super(windowClass, self).__init__(*args, **kwargs)
        self.basicGUI()

    def basicGUI(self):
        
        menuBar = wx.MenuBar()

        fileButton = wx.Menu()

        exitItem = fileButton.Append(wx.ID_EXIT, 'Exit', '')

        menuBar.Append(fileButton, 'File')
        
        self.SetMenuBar(menuBar)
        self.Bind(wx.EVT_MENU, self.Quit, exitItem)

        dlg = wx.DirDialog(None, "Choose source directory", "",
                           wx.DD_DEFAULT_STYLE | wx.DD_DIR_MUST_EXIST)
        dlg2 =wx.DirDialog(None, "Choose destination directory", "",
                           wx.DD_DEFAULT_STYLE | wx.DD_DIR_MUST_EXIST)
        src = dlg.ShowModal()
        dst = dlg2.ShowModal()

        srcpath = dlg.GetPath()
        dstpath = dlg2.GetPath()
        #print src
        #print dst

        for name in os.listdir(srcpath):
            src = srcpath + '\{}'.format(name)
            dst = dstpath + '\{}'.format(name)

            #now = time.time()
            #print now
            time_diff = time.time() - (os.path.getmtime(src))

            _24hoursago = time.time() - (24 *60 *60)
            last_24_hrs = time.time() - _24hoursago 


            if time_diff < last_24_hrs:
                print 'File moved: {}'.format(src)
                print 'last modified: {}'.format(time.ctime(os.path.getmtime(src)))
                shutil.move(src, dst)
                
        
        dlg.Destroy()
        dlg2.Destroy()
        
        self.SetTitle('Move Files')
        self.Show(True)



    def Quit(self,e):
        self.Close()

def main():
    app = wx.App()
    windowClass(None, title = 'Move files!')
    app.MainLoop()

if __name__== "__main__":
    main()


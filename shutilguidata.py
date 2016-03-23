import shutil
import os
import time
import datetime
import wx
import sqlite3


conn = sqlite3.connect('FileMoveRecord.db')

c = conn.cursor()

c.execute("CREATE TABLE IF NOT EXISTS FileMoveTimes(date TEXT)")

#initiate idfordb to 1
#idfordb = 1

#Current unix time
current_time1 = time.time()
#current datetime stamp
current_time = datetime.datetime.now()
current_time2 = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
c.execute("INSERT INTO FileMoveTimes(date) VALUES (?)", [(current_time1)])
c.execute("SELECT * FROM FileMoveTimes")

allData = c.fetchall()
lastrun = float((allData)[-1][-1])
print(lastrun)

conn.commit()
#Creating the window Frame
class windowClass(wx.Frame):

    
    def __init__(self, *args, **kwargs):
        super(windowClass, self).__init__(*args, **kwargs)
        self.basicGUI()

   
        

    def basicGUI(self):

        panel = wx.Panel(self)
        
        menuBar = wx.MenuBar()

        fileButton = wx.Menu()

        exitItem = fileButton.Append(wx.ID_EXIT, 'Exit', '')

        menuBar.Append(fileButton, 'File')
        
        self.SetMenuBar(menuBar)
        self.Bind(wx.EVT_MENU, self.Quit, exitItem)

        #use DirDialog for file select
        dlg = wx.DirDialog(None, "Choose source directory", "",
                           wx.DD_DEFAULT_STYLE | wx.DD_DIR_MUST_EXIST)
        dlg2 =wx.DirDialog(None, "Choose destination directory", "",
                           wx.DD_DEFAULT_STYLE | wx.DD_DIR_MUST_EXIST)
        src = dlg.ShowModal()
        dst = dlg2.ShowModal()

        srcpath = dlg.GetPath()
        dstpath = dlg2.GetPath()

        #script to move files that were modified less than 24 hours ago 
        for name in os.listdir(srcpath):
            #idfordb = 1
            src = srcpath + '\{}'.format(name)
            dst = dstpath + '\{}'.format(name)

            
            time_diff = current_time1 - (os.path.getmtime(src))

            _24hoursago = current_time1 - (24 *60 *60)
            last_24_hrs = current_time1 - _24hoursago

            #print(time_diff)

            #print(lastrun)
            #print(last_24_hrs)
            #print(_24hoursago)
            #print type(last_24_hrs)

            #while lastrun is equal to the last 24hours and if the file was modified within the last
            #24 hours, move the file 
            #if time_diff < last_24_hrs:
            
            if time_diff < last_24_hrs:
                print 'File Moved: {} '.format(src)
                print "Last Modified: {}".format(time.ctime(os.path.getmtime(src)))
                shutil.move(src, dst)


        dlg.Destroy()
        dlg2.Destroy()

        lastRun = wx.StaticText(panel, -1, "Last Run: " + str(lastrun), (3,3))
        
        
        self.SetTitle('Move Files')
        self.Show(True)



    def Quit(self,e):
        self.Close()

def main():
    app = wx.App()
    windowClass(None, title = 'Move files!')
    app.MainLoop()



main()



"""
Autonomous file controller: core code::

Rev.01 31/10/24 
Rev.02 13/11/24


EMERGING Technology - MMR
"""
import pandas as pd
import os
import shutil
import xlwings as xw
from configparser import ConfigParser
import win32com.client as win32

config = ConfigParser()
config.read('xlsxcount.ini')

class Moplene():
    lastRow = 0
    def __init__(self):
        self.TRdict = None
        self.current_report = None
    def open(self, path):
        try:
            df = pd.read_excel(path)
            lastRow = len(df)
            lastRowConfig = int(config.get('Excel Counter', 'lastRow'))
            if lastRow > lastRowConfig:
                newReport = abs(lastRow - lastRowConfig)
                for i in range(newReport,0,-1):
                    sender = df.iloc[-i,4]
                    title = df.iloc[-i,5]
                    time = df.iloc[-i,6]
                    loc = df.iloc[-i,7]
                    cr = df.iloc[-i,9]
                    act = df.iloc[-i,10]
                    losstime = df.iloc[-i,11]
                    
                    self.TRdict = {'sender': sender, 'title': title, 'time': time, 'loc': loc, 'cr': cr, 'act': act, 'lt': losstime}
    
                    self.write(r'C:\Users\mrm\Documents\Production Engineering\Reporting system\FRM.PRO.01.45.XLS', 'FRM.PRO.01.45.xlsx', self.TRdict)

                    email_subject = 'Trouble Report Notification: ' + self.TRdict['title']
                    self.email(email_subject, self.current_report)
                    
            config.set('Excel Counter', 'lastRow', str(lastRow))
            with open('xlsxCount.ini', 'w') as configfile:
                    config.write(configfile)
                    
        except Exception as e:
            pass
        
        return self.TRdict
    
    def email(self, subject, reportPath, attachPath = None):
        app = win32.Dispatch('Outlook.Application')
        appNS = app.GetNameSpace('MAPI')
        mailItem = app.CreateItem(0)
        mailItem.Subject = subject
        mailItem.BodyFormat = 1
        mailItem.Body = 'Trouble Report Notifications'
        mailItem.To = 'riyan.madya@polytama.co.id'
##        mailItem.CC = 'faisal.alrasyid@polytama.co.id' #'TroubleReportReceiver@polytama.co.id'

        mailItem.Attachments.Add(reportPath)
##        mailItem.Attachments.Add('dir')

##        mailItem.Display()

##        mailItem.Save()
##        mailItem.Send()
        
        
    def write(self, path, filename,mydict):
        fileloc = os.getcwd()
        sender = mydict['sender']
        subject = mydict['title']
        date = mydict['time']
        cr = mydict['cr']
        act = mydict['act']
        lt = mydict['lt']
        
        strf_time = str(mydict['time'].strftime('%Y-%m-%d'))
        rt_container = ['Trouble Report ', strf_time,' ', subject, '.xlsx']
        report_title = ''.join(rt_container)
        self.current_report = fileloc + '\\' + report_title
        shutil.copy(fileloc + '\\' + filename, fileloc + '\\' + report_title)

        wb_app = xw.App(visible = False)
        wb = xw.Book(fileloc + '\\' + report_title)
        sheet = wb.sheets[0]
        sheet.range(11,3).value = sender
        sheet.range(15,3).value = subject
        sheet.range(17,3).value = date
        sheet.range(20,3).value = subject
        sheet.range(30,3).value = cr
        sheet.range(44,3).value = act
        sheet.range(63,3).value = lt
        sheet.range(73,6).value = sender

        wb.save()
        wb.close()
        wb_app.quit()
     

# Test-1

myExcel = Moplene()
myd = myExcel.open(r'C:\Users\mrm\OneDrive - Polytama Propindo\Trouble Report Production Dept.xlsx')
##write(r'C:\Users\mrm\Documents\Production Engineering\Reporting system\FRM.PRO.01.45.XLS', 'FRM.PRO.01.45.xlsx', myd)

##myExcel.email('Trouble')

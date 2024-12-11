"""
Autonomous Reporting System: core code::

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
from plotify import plotify
from datetime import datetime
import time
from servercall import main

config = ConfigParser()
config.read('xlsxcount.ini')


class Moplene():
    lastRow = 0
    def __init__(self):
        self.TRdict = None
        self.current_report = None
        self.stats = {}
        self.imgTitle = None
        self.report_title = 'Masplene'
        self.oldest_report = 0
    def open(self, path):
        try:
##            df = pd.read_excel(path)
##            print(df.iloc[:,4:6])
            # code for location is col 7
            # code for classification is col 8

            df = main()
            lastRow = len(df)
##            print(lastRow)
            lastRowConfig = int(config.get('Excel Counter', 'lastRow'))
            if lastRow > lastRowConfig:
                newReport = abs(lastRow - lastRowConfig)
##                print(newReport)
                newStats, latestVal = self.counter(df)
                self.imgTitle = datetime.now().strftime('%d-%m-%y %H-%M') + '.png'
                plotify(newStats, self.imgTitle, latestVal) 

                i = 0
                
                for i in range(newReport,0,-1):
                    sender = df.iloc[-i,1]
                    title = df.iloc[-i,2]
                    time = df.iloc[-i,3]
                    loc = df.iloc[-i,4]
                    cr = df.iloc[-i,6]
                    act = df.iloc[-i,7]
                    losstime = df.iloc[-i,8]
                    
                    self.TRdict = {'sender': sender, 'title': title, 'time': time, 'loc': loc, 'cr': cr, 'act': act, 'lt': losstime}
                    
                    if loc == 'Bulk':
                        path = r"D:\Polytama Propindo\Production - Documents\General\Trouble Report dan Laporan Kejadian\Trial-Bulk"
                    elif loc == 'Utility':
                        path = r"D:\Polytama Propindo\Production - Documents\General\Trouble Report dan Laporan Kejadian\Trial-Utility"
                    elif loc == 'Pelletizing 1':
                        path = r"D:\Polytama Propindo\Production - Documents\General\Trouble Report dan Laporan Kejadian\Trial-Pelletizing 1"
                    elif loc == 'Pelletizing 2':
                        path = r"D:\Polytama Propindo\Production - Documents\General\Trouble Report dan Laporan Kejadian\Trial-Pelletizing 2"
                    elif loc == 'Bagging 1':
                        path = r"D:\Polytama Propindo\Production - Documents\General\Trouble Report dan Laporan Kejadian\Trial-Bagging 1"
                    elif loc == 'Bagging 2':
                        path = r"D:\Polytama Propindo\Production - Documents\General\Trouble Report dan Laporan Kejadian\Trial-Bagging 2"

                    thrashfolder = r"C:\Users\ssv\AppData\Local\Programs\Python\Python311\InjectionX\__program\__thrash"
                    self.write(thrashfolder, 'FRM.PRO.01.45.xlsx', self.TRdict)
                    email_subject = 'Trouble Report Notification: ' + self.TRdict['title']
                    self.email(email_subject, self.current_report)
                    try:
                        if os.path.exists(path + '\\' + self.report_title):
                            os.remove(path + '\\' + self.report_title)
                            shutil.copy(self.current_report, path + '\\' + self.report_title)
                        else:
                            shutil.copy(self.current_report, path + '\\' + self.report_title)
                    except Exception as e:
                        pass
                    
                    os.remove(thrashfolder + '\\' + self.report_title)
                    
            config.set('Excel Counter', 'lastRow', str(lastRow))
            with open('xlsxCount.ini', 'w') as configfile:
                    config.write(configfile)
                    
        except Exception as e:
            pass
        
        return self.TRdict
    
    def email(self, subject, reportPath , attachPath = None):
        app = win32.gencache.EnsureDispatch("Outlook.Application").GetNamespace("MAPI")
        app = win32.Dispatch("Outlook.Application")
        
##        app = win32.Dispatch('Outlook.Application')
##        appNS = app.GetNameSpace('MAPI')
        mailItem = app.CreateItem(0x0)
        mailItem.To = 'wifandy.purba@polytama.co.id'
        mailItem.Subject = subject
        mailItem.Attachments.Add(reportPath)
        attachment = mailItem.Attachments.Add(r'C:\Users\ssv\AppData\Local\Programs\Python\Python311\InjectionX\__program\__buffer' + '\\' + self.imgTitle)
        attachment.PropertyAccessor.SetProperty("http://schemas.microsoft.com/mapi/proptag/0x3712001F", "imgTitle")
        mailItem.BodyFormat = 2
        mailItem.CC = 'TroubleReportReceiver@polytama.co.id; s.supervisor@polytama.co.id'
        mailItem.HTMLBody =\
                f"""
                  <p class=MsoNormal style='line-height:36.0pt'><b><span style='font-size:
                  15.0pt;font-family:"Segoe UI",sans-serif;mso-fareast-font-family:"Times New Roman";
                  color:#008272;letter-spacing:.4pt'>Trouble Report News<o:p></o:p></span></b></p>
                  </div>
                  </div>
                  <div style='margin-left:30.0pt;margin-top:22.5pt;margin-bottom:45.0pt'>
                  <div style='margin-top:7.5pt'>
                  <p class=MsoNormal style='line-height:15.75pt'><span style='font-size:
                  12.0pt;font-family:"Segoe UI",sans-serif;mso-fareast-font-family:"Times New Roman";
                  color:#505050;letter-spacing:.15pt'><!-- // FormTitle --> Dear Mr. Wifandy and Production Team,<o:p></o:p></span ></p>
            <!-- // EmailSalutation -->
                  <p class=MsoNormal style='line-height:15.75pt'><span style='font-size:
                  12.0pt;font-family:"Segoe UI",sans-serif;mso-fareast-font-family:"Times New Roman";
                  color:#505050;letter-spacing:.15pt'>A new trouble has just happened with the title "{self.TRdict['title']}".<o:p></o:p></span></p>
                  <p class=MsoNormal style='line-height:15.75pt'><span style='font-size:
                  12.0pt;font-family:"Segoe UI",sans-serif;mso-fareast-font-family:"Times New Roman";
                  color:#505050;letter-spacing:.15pt'>The latest trouble report statistic: <o:p></o:p></span></p>
                  <p class=MsoNormal style='line-height:15.75pt'><span style='font-size:
                  12.0pt;font-family:"Segoe UI",sans-serif;mso-fareast-font-family:"Times New Roman";
                  color:#505050;letter-spacing:.15pt'>*The oldest report as the statistic timestamp is {self.oldest_report}* <o:p></o:p></span></p>
                  </div>
                  <img border=0 src="cid:imgTitle"><br><br>
                  </td>
                 </tr>
                </table>
                </td>
               </tr>
               <tr style='mso-yfti-irow:2'>
                <td style='padding:0cm 0cm 0cm 0cm;word-break:break-word'
                vertical-align=middle>
                <div align=center>
                <table class=MsoNormalTable border=0 cellspacing=0 cellpadding=0
                 style='border-collapse:collapse;mso-yfti-tbllook:1184;mso-padding-alt:
                 0cm 0cm 0cm 0cm' role=presentation>
                 <tr style='mso-yfti-irow:0;mso-yfti-firstrow:yes;mso-yfti-lastrow:yes'>
                  <td style='border:solid #03787C 1.0pt;mso-border-alt:solid #03787C .75pt;
                  background:#03787C;padding:4.5pt 7.15pt 4.5pt 7.15pt' role=presentation>
                  <p class=MsoNormal align=center style='text-align:center'><span
                  style='mso-fareast-font-family:"Times New Roman";color:black;mso-color-alt:
                  windowtext'><a
                  href="https://docs.google.com/spreadsheets/d/1UMl4JvrWhmnjXkVmoqRND_c43l9HdU2Ey_Gx4R6jDZY/edit?gid=1157492794#gid=1157492794"
                  target="_blank" style='display:inline-block;border-radius:4px'><b><span
                  style='font-size:10.5pt;font-family:"Segoe UI",sans-serif;color:white;
                  background:#03787C;text-decoration:none;text-underline:none'>View&nbsp;Register
                  <img border=0 width=14 id="_x0000_i1026"
                  src="https://cdn.forms.office.net/forms/images/notification/link_white.png"
                  style='margin-bottom:2px;margin-left:7px;margin-right:3px;margin-top:
                  0in;vertical-align:middle' heigh=14></span></b></a></span><span
                  style='mso-fareast-font-family:"Times New Roman"'><o:p></o:p></span></p>
                  </td>
                 </tr>
                </table>
                </div>
                </td>
               </tr>
               </div>
                Warm Regards, <br><br>
                Production Assistant Ver 0.0.1
                """
##                <img src="cid:imgTitle"><br><br>
##                The detail report is on the attachment. <br><br>
##                The updated trouble report register is on this link <a href="https://github.com/polzerdo55862/Python-Email-Template" style="color: #00000;">GitHub</a>.</p>
##                </td>
##        f"""
##            <html>
##            <head>
##              <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
##              <title>Data Report Template</title>
##              <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
##            </head>
##
##            <body style="margin: 0; padding: 0;">
##              <table role="presentation" border="0" cellpadding="0" cellspacing="0" width="100%">
##                <tr>
##                  <td style="padding: 20px 0 30px 0;">
##                    <table align="center" border="0" cellpadding="0" cellspacing="0" width="100%" style="border-collapse: collapse; border: 1px solid #cccccc;">
##                      <tr>
##                        <td align="center" bgcolor="#096192" style="padding: 40px 0 30px 0;">
##                          <h1 style="font-size: 32px; margin: 0; color: #ffffff;">Trouble Report Production Department</h1>
##                        </td>
##                      </tr>
##                      <tr>
##                        <td bgcolor="#ffffff" style="padding: 40px 30px 40px 30px;">
##                          <table border="0" cellpadding="0" cellspacing="0" width="100%" style="border-collapse: collapse;">
##                            <tr>
##                              <td style="color: #153643; font-family: Arial, sans-serif;">
##                                <h1 style="font-size: 24px; margin: 0;">Updated Troubleshooting Statistics</h1>
##                              </td>
##                            </tr>
##                            <tr>
##                              <td style="color: #153643; font-family: Arial, sans-serif; font-size: 16px; line-height: 24px; padding: 20px 0 30px 0;">
##                                <p style="margin: 0;">Here are the current statistics of trouble report of Production Department.</p>
##                              </td>
##                            </tr>
##                            <tr>
##                              <td>
##                                <img src="cid:imgTitle" alt="Creating Email Magic.">
##                              </td>
##                            </tr>
##                            <tr>
##                              <td style="color: #153643; font-family: Arial, sans-serif; font-size: 16px; line-height: 24px; padding: 20px 0 30px 0;">
##                                <p style="margin: 0;">Here are the current statistics of trouble report of Production Department.</p>
##                              </td>
##                            </tr>
##                          </table>
##                        </td>
##                      </tr>
##                      <tr>
##                        <td bgcolor="#096192" style="padding: 30px 30px;">
##                            <table border="0" cellpadding="0" cellspacing="0" width="100%" style="border-collapse: collapse;">
##                            <tr>
##                              <td style="color: #00000; font-family: Arial, sans-serif; font-size: 14px;">
##                                <p style="margin: 0;">&reg; DP, Germany 2021<br/>
##                                  You can find the source code to send this email on <a href="https://github.com/polzerdo55862/Python-Email-Template" style="color: #00000;">GitHub</a>.</p>
##                              </td>
##                              <td align="right">
##                                <table border="0" cellpadding="0" cellspacing="0" style="border-collapse: collapse;">
##                                </table>
##                              </td>
##                            </tr>
##                          </table>
##                        </td>
##                      </tr>
##                    </table>
##
##                  </td>
##                </tr>
##              </table>
##            </body>
##            </html>
##        """
    
##        mailItem.Display()
        mailItem.Save()
        mailItem.Send()
        
        
    def write(self, path, filename,mydict):
        fileloc = os.getcwd()
        sender = mydict['sender']
        subject = mydict['title']
        date = mydict['time']
        cr = mydict['cr']
        act = mydict['act']
        lt = mydict['lt']

        
        strf_time = mydict['time'].replace('/', '-').replace(':', '-')

        rt_container = ['Trouble Report ', strf_time,' ', subject, '.xlsx']
        self.report_title = ''.join(rt_container)
        self.current_report = path + '\\' + self.report_title
        shutil.copy(fileloc + '\\' + filename, path + '\\' + self.report_title)

        wb_app = xw.App(visible = False)
        wb = xw.Book(path + '\\' + self.report_title)
        sheet = wb.sheets[0]
        sheet.range(11,3).value = sender
        sheet.range(15,3).value = subject
        sheet.range(17,3).value = date
        sheet.range(20,3).value = subject
        sheet.range(30,3).value = cr
        sheet.range(44,3).value = act
        if mydict['loc'] == 'Bulk' or mydict['loc'] == 'Utility':
            sheet.range(64,3).value = lt
        else:
            sheet.range(66,3).value = lt
        sheet.range(73,6).value = sender
        sheet.range(73,8).value = 'Wifandy Purba'

        wb.save()
        wb.close()
        wb_app.quit()

    def counter(self, df):
        d = []
        p = []
        q = []
        s = []
        for i in range(len(df)):
            if i != 0:
                date = df.iloc[i,3]
                date = datetime.strptime(date,  '%m/%d/%Y %H:%M:%S')
                d.append(date)
            locs = df.iloc[i,4]
            cluster = df.iloc[i,5]
            if cluster == 'Process':
                p.append(locs)
            elif cluster == 'Quality':
                q.append(locs)
            elif cluster == 'Safety':
                s.append(locs)
        d.sort()
        self.oldest_report = d[0]
    
        
        i = 0 
        for l in [p,q,s]:
            a1 = l.count('Bulk')
            a2 = l.count('Utility')
            a3 = l.count('Pelletizing 1')
            a4 = l.count('Pelletizing 2')
            a5 = l.count('Bagging 1')
            a6 = l.count('Bagging 2')
                
            if i == 0:
                self.stats['Process'] = [a1, a2, a3, a4, a5, a6]
            elif i == 1:
                self.stats['Quality'] = [a1, a2, a3, a4, a5, a6]
            else:
                self.stats['Safety'] = [a1, a2, a3, a4, a5, a6]
            i += 1
            
        latestVal = str(locs) + " : Cluster " +  str(cluster)
        return self.stats, latestVal
     

# Test-1

    
myExcel = Moplene()
myd = myExcel.open(r'D:\OneDrive - Polytama Propindo\Trouble Report Register\Trouble Report Production Department.xlsx')
##write(r'C:\Users\mrm\Documents\Production Engineering\Reporting system\FRM.PRO.01.45.XLS', 'FRM.PRO.01.45.xlsx', myd)
##myExcel.email('GOOD')

##myExcel.email('Trouble')

##import psutil
##import subprocess
##def open_outlook():
##    try:
##        subprocess.call([r'C:\Program Files\Microsoft Office\root\Office16\OUTLOOK.EXE'])
##        os.system(r'C:\Program Files\Microsoft Office\root\Office16\OUTLOOK.EXE');
##    except Exception as e:
##        raise e
##        print("Outlook didn't open successfully")
##
### Checking if outlook is already opened. If not, open Outlook.exe and send email
##for item in psutil.pids():
##    p = psutil.Process(item)
##    if p.name() == "OUTLOOK.EXE":
##        flag = 1
##        break
##    else:
##        flag = 0
##
##if (flag == 1):
##    myExcel.email('OKOK')
##else:
##    open_outlook()
##    myExcel.email('OKOK')

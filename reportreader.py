"""
Extracting excel then creating a new one with specific format

Rev.01 31/10/24 MRM
"""
import pandas as pd
import os
import shutil
import xlwings as xw


def open(path):
    df = pd.read_excel(path)
    sender = df.iloc[-1,4]
    title = df.iloc[-1,5]
    time = df.iloc[-1,6]
    loc = df.iloc[-1,7]
    cr = df.iloc[-1,8]
    act = df.iloc[-1,9]

    TRdict = {'sender': sender, 'title': title, 'time': time, 'loc': loc, 'cr': cr, 'act': act}
    
    return TRdict

def write(path, filename,mydict):
    fileloc = os.getcwd()
    sender = mydict['sender']
    subject = mydict['title']
    date = mydict['time']
    cr = mydict['cr']
    act = mydict['act']
    
    strf_time = str(mydict['time'].strftime('%Y-%m-%d'))
    rt_container = ['Trouble Report ', strf_time,' ', subject, '.xlsx']
    report_title = ''.join(rt_container)

    shutil.copy(fileloc + '\\' + filename, fileloc + '\\' + report_title)

    wb_app = xw.App(visible = False)
    wb = xw.Book(fileloc + '\\' + report_title)
    sheet = wb.sheets[0]
    sheet.range(11,3).value = sender
    sheet.range(15,3).value = subject
    sheet.range(17,3).value = date
    sheet.range(20,3).value = cr
    sheet.range(30,3).value = act
    sheet.range(40,3).value = act

    wb.save()
    wb.close()
    wb_app.quit()
     

# Test-1

myd = open(r'C:\Users\mrm\OneDrive - Polytama Propindo\Trouble Report Production Dept.xlsx')
write(r'C:\Users\mrm\Documents\Production Engineering\Reporting system\FRM.PRO.01.45.XLS', 'FRM.PRO.01.45.xlsx', myd)


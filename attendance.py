import pandas as pd
while(True):
    attendance = pd.read_excel('Attendance sheet.xlsx')
    name=attendance['Name'].tolist()
    name = input('Enter ur Name:')
    if name in attendance['Name'].tolist():
        date = attendance.columns
        date = input('select the date'+',\n'.join(date)+'\n:')
        if date in attendance.columns:
            attendance = attendance.loc[attendance['Name']==name ,date]
            print(attendance.values[0])
        else:
            print('attendance found!!')
    else:
        print('Your not an employee')
        continue if input('enter to continue or esc to exit')=='\n' else break
"""
Add a current datetime to a file in c:\Temp
"""
from datetime import datetime

with open('C:\Temp\HelloJenkins.txt', 'a') as file:
    file.write(f'Current date time: {datetime.now()}\n')



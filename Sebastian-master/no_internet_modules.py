'This file includes those modules that\
can be used without access to the internet.\
For complete list of these modules please refer to documentation.'

import datetime


months = ['January','February','March','April','May','June','July',
         'August','September','October','November','December']
days = ['Monday','Tuesday','Wednesday','Thirsday','Friday','Saturday','Sunday']

now = datetime.datetime.now()
_day = str(now.day)
_month = str(months[now.month-1])
_year = str(now.year)
_date = _day+' '+_month+' '+_year

def date():
    print("Today's date is "+_date+"\n");
def day():
    print("Today is "+days[now.day]+"\n");
def month():
    print("The current month is "+_month+"\n")
def year():
    print("The current year is "+_year+"\n")
def test():
    print("The module \'no_internet_modules\' was imported")
def time():
    print("It\'s ",now.hour,":",now.minute,"\n")

if __name__ == '__main__':
    print("\n\
    This module was accessed directly.\n\
    If you are lost, it's best if you leave.\n\
    Executing functions and classes intended for testing purposes.\n")
    print('\n\n\n\n')
    time()

import datetime
from sys import argv
#script, DATE = argv

#print DATE
def date_range(start, end):
    r = (end+datetime.timedelta(days=1)-start).days
    return [start+datetime.timedelta(days=i) for i in range(r)]
mylist = [] 
start = datetime.date(2016,06,01)
end = datetime.date(2016,07,01)
dateList = date_range(start, end)
#print '\n'.join([str(date) for date in dateList])
for date in dateList:
    print date.strftime("%m_%d_%Y")

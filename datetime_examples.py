from datetime import date,datetime,timedelta

#date表示日期（年月日）；datetime（年月日时分秒...）继承 date；time表示时间（时分秒...）
# timedelta 表示时间差；tzinfo 表示时区信息

today = date.today()
now = datetime.now()




#30days later
today_plus30 = today + timedelta(30)


print(today.strftime('%Y/%m/%d'))

print(now.strftime('%Y/%m/%d %H%:%M:%S'))
print(today_plus30)


#获取本周/本月/上月最后一天
import calendar
today = datetime.date.today()

sunday = today + datetime.timedelta(6 - today.weekday())

_,last_day_num = calendar.monthrange(today.year,today.month)
last_day = datetime.date(today.year,today.month,last_day_num)

first = datetime.date(today.year,today.month,1)
lastMonth = first - datetime.timedelta(1)







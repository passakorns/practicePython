#รับวันเดือนปีเกิด (dd/mm/yyyy) และให้แสดงอายุกี่ ปี เดือน
#birthday = "01/01/2540"
from datetime import datetime

currentDay = datetime.now()

birthday_str = input('วันเดือนปีเกิดของคุณ (วัน/เดือน/ปี พ.ศ.) ')

print(currentDay)
birthday_lst = birthday_str.split(sep='/')
year = int(birthday_lst[2])-543
birthday_new = birthday_lst[0]+"/"+birthday_lst[1]+"/"+str(year)
birthday_date = datetime.strptime(birthday_new,"%d/%m/%Y")
print(birthday_date)
dif = currentDay - birthday_date
ageY = dif.days//365        #จำนวนปี
ageM = ageD = 0
if dif.days>=365:
    ageY = dif.days//365
    ageM = (dif.days%365)//30
    ageD = (dif.days%365)%30
elif dif.days>=30:
    ageY = 0
    ageM = dif.days//30
    ageD = dif.days%30
else:
    ageY = 0
    ageM = 0
    ageD = dif.days
print(f'คุณอายุ {ageY} ปี {ageM} เดือน {ageD} วัน')
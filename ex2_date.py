from datetime import datetime

# รับค่าวันที่ปัจจุบันจากระบบ
nowDay = datetime.now()
print(f'วันนี้คือวันที่ {nowDay}')
print(type(nowDay))

# เปลี่ยนรูปแบบการแสดงผลของวันที่และเวลา
fm1_nowDay = nowDay.strftime("%d/%m/%Y %H:%M")
print(f'วันนี้คือวันที่ {fm1_nowDay}')
print(type(fm1_nowDay))

fm2_nowDay = nowDay.strftime("%A, %d %B %Y")
print(f'fm2 วันนี้คือวันที่ {fm2_nowDay}')

# fm3 >> Tue-2024-09-03 01:15PM
fm3_nowDay = nowDay.strftime("%a-%Y-%m-%d %I:%M%p")
print(f'fm3 วันนี้คือวันที่ {fm3_nowDay}')

# การเปลี่ยนข้อความวันที่และเวลา ให้เป็นชนิด datetime
date_str = "2024-01-05"
date_obj = datetime.strptime(date_str,"%Y-%m-%d")
print(f'วันที่ของคุณ {date_obj}')
print(type(date_obj))

# การคำนวณจำนวนวันระหว่างวันที่ปัจจุบัน nowDay กับวันที่ของผู้ใช้ date_obj
countDay = nowDay - date_obj
print(f'nowDay และ date_obj จำนวนวันห่างกัน เท่ากับ {countDay.days} วัน')
num_month = countDay.days//30    #หารเอาจำนวนเต็ม
num_day = countDay.days%30       #หารเอาเศษ

# m1 คือ ชื่อเดือนแบบเต็มของ nowDay
m1 = nowDay.strftime("%d %B")
# m2 คือ ชื่อเดือนแบบเต็มของ date_obj
m2 = date_obj.strftime("%d %B")
print(f'วันที่ {m2} ถึง วันที่ {m1} ห่างกัน {num_month} เดือน {num_day} วัน')

print('='*30)
# อีกกี่วันจะถึงสิ้นปี
year_end = "30-09-2024" #วันสิ้นปี
year_end_obj = datetime.strptime(year_end,"%d-%m-%Y")
dif = year_end_obj - nowDay
ageM = ageD = 0
if dif.days <= 30:
    ageD = dif.days
elif dif.days <= 365:
    ageM = dif.days//30
    ageD = dif.days%30

print(f'วันนี้ {fm1_nowDay} ถึง วันสิ้นปี ห่างกัน {ageM}  เดือน {ageD} วัน')
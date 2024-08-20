#การสร้างที่เก็บข้อมูลแบบ dictionary
person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
contries = {
    'th': 'Thailand',
    'kr': 'Korea',
    'jp': 'Japan'
}
print(person)
print(contries)

#การเข้าถึงข้อมูลโดยการใช้คีย์
age = person['age']
name = person['name']
print(f'Name of person: {name}')
print(f'Age of person: {age}')
print(f'City of person: ',person['city'])

#การเข้าถึงข้อมูลโดยการใช้ฟังก์ชัน get
cty = contries.get('th')
print(f'Contries name is: {cty}')

cty = contries.get('us')
print(cty)              # None

#การแก้ไขข้อมูล
person['age'] = 31
person['city'] = 'Cannada'
print(person)

#การเพิ่มข้อมูล
person["email"] = "alice@example.com"
print("Updated dictionary:", person)

#การลบข้อมูล
# del person['age']
# print('Deleted dict of person: ', person)

person.pop('age')
print('Deleted dict of person: ', person)

#1.การใช้ Loop for in เพื่อเข้าถึงค่าคีย์
for k in person:
    print('key of person is ', k)
print('-'*20)

#2.การใช้ Loop for in เพื่อเข้าถึงค่าข้อมูล
for v in person.values():
    print('value of person is ', v)
print('-'*20)

#3.การใช้ Loop for in เพื่อเข้าถึงค่าคีย์ และข้อมูล
for k, v in person.items():
    print(f'person[{k}] = {v}')
print('-'*20)

#การตรวจสอบคีย์
if 'age' in person:
    print('age have in person')
else:
    person['age'] = 31
print(person)
if 'age' in person:
    print('age have in person')
else:
    person['age'] = 31
print(person)

if 'phone' not in person:
    person['phone'] = '123-456'
else:
    print('phone have in person')
print(person)

print(f'Size of person : {len(person)}')

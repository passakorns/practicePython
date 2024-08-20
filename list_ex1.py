# การสร้างลิสต์
fruits = ["apple", "banana", "cherry", "date"]

print(fruits)

#การเข้าถึงสมาชิก
first_fruit = fruits[0]
print("First fruit:", first_fruit)
print(f'Forth fruit: {fruits[3]}')

#การแก้ไขข้อมูลในลิสต์
fruits[3] = 'Durian'
print(f'Forth fruit: {fruits[3]}')
print(fruits)

#การเพิ่มสมาชิกในลิสต์
fruits.append('Blueberry')
print(fruits)

#การแทรกสมาชิกในลิสต์
fruits.insert(1, 'Fig')
print(fruits)

#การลบสมาชิกในลิสต์
fruits.remove('Fig')
print(fruits)

del fruits[4]
print(fruits)

#การแสดงผลสมาชิกในลิสต์
print(fruits)
print(fruits[2])
print(fruits[1:3])
print(fruits[1:4])
print(fruits[:3])
print(fruits[2:])

#การเข้าถึงสมาชิกในลิสต์ด้วย Loop for in
for f in fruits:
    print(f'Fruits: {f}')

#การตรวจสมาชิกในลิสต์
data = 'Blueberry'
if data not in fruits:
    fruits.append(data)
else:
    print(f'no append {data}')
print(fruits)

data = 'Blueberry'
if data not in fruits:
    fruits.append(data)
else:
    print(f'no append {data}')
print(fruits)

#นับจำนวนสมาชิกของลิสต์
countMember = len(fruits)
print(f'Size of fruits: {countMember}')

#จัดเรียงสมาชิกในลิสต์
fruits.sort()       #จัดเรียงน้อยไปมาก
print(fruits)

fruits.sort(reverse=True) #จัดเรียงมากไปน้อย
print(fruits)

num = [45, 20, 30, 15, 50]
num.sort()
print(num)
num.sort(reverse=True)
print(num)
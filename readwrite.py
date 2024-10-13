input_filename = 'file/input.txt'
output_filename = 'file/output.txt'

# อ่านข้อมูลจากไฟล์ input.txt
file = open(file=input_filename, mode='r', encoding='utf8')
students= file.readlines()
lst_std = []
for line in students:
    name, score = line.split(',')
    lst_std.append([name, int(score)])
file.close()

# คำนวณค่าเฉลี่ยคะแนน
totalScore=0
for name, score in lst_std:
    totalScore = totalScore+score
averageScore = totalScore/len(lst_std)

# เขียนข้อมูลนักเรียนที่มีคะแนนสูงกว่าค่าเฉลี่ยลงไฟล์ output.txt
file = open(file=output_filename, mode='w', encoding='utf8')
for name, score in lst_std:
    if score > averageScore:
        file.write(f'{name}, {score}\n')
file.close()


print(f'ค่าเฉลี่ยคะแนน: {averageScore:.2f}')
print(f'เขียนข้อมูลนักเรียนที่มีคะแนนสูงกว่าค่าเฉลี่ยลงในไฟล์ {output_filename} เรียบร้อยแล้ว')

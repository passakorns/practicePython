from tkinter import *
from tkinter import messagebox


# ฟังก์ชันสำหรับการคำนวณ
def getNum():

        # ดึงค่าจาก Entry และแปลงเป็นตัวเลข
        value1 = float(num1.get())
        value2 = float(num2.get())
        
        return value1, value2

def add():
    try:
        x, y = getNum()
        result = x + y
        # แสดงผลลัพธ์ใน Label
        result_label.config(text=f"{x} + {y} ผลลัพธ์: {result:.3f}")
    except ValueError:
        # กรณีที่แปลงเป็น float ไม่ได้
        messagebox.showerror("Error", "กรุณากรอกตัวเลขที่ถูกต้อง")
    except ZeroDivisionError:
        # กรณีหารด้วย 0
        messagebox.showerror("Error", "ไม่สามารถหารด้วยศูนย์ได้")

def div():
    try:
        x, y = getNum()
        result = x / y
        # แสดงผลลัพธ์ใน Label
        result_label.config(text=f"{x} / {y} ผลลัพธ์: {result:.2f}")

    except ValueError:
        # กรณีที่แปลงเป็น float ไม่ได้
        messagebox.showerror("Error", "กรุณากรอกตัวเลขที่ถูกต้อง")
    except ZeroDivisionError:
        # กรณีหารด้วย 0
        messagebox.showerror("Error", "ไม่สามารถหารด้วยศูนย์ได้")

def multi():
    try:
        x, y = getNum()
        result = x * y
        # แสดงผลลัพธ์ใน Label
        result_label.config(text=f"{x} * {y} ผลลัพธ์: {result:.2f}")
        
    except ValueError:
        # กรณีที่แปลงเป็น float ไม่ได้
        messagebox.showerror("Error", "กรุณากรอกตัวเลขที่ถูกต้อง")
    except ZeroDivisionError:
        # กรณีหารด้วย 0
        messagebox.showerror("Error", "ไม่สามารถหารด้วยศูนย์ได้")
def delete():
    try:
        x, y = getNum()
        result = x - y
        # แสดงผลลัพธ์ใน Label
        result_label.config(text=f"{x} - {y} ผลลัพธ์: {result:.2f}")
        
    except ValueError:
        # กรณีที่แปลงเป็น float ไม่ได้
        messagebox.showerror("Error", "กรุณากรอกตัวเลขที่ถูกต้อง")

    except ZeroDivisionError:
        # กรณีหารด้วย 0
        messagebox.showerror("Error", "ไม่สามารถหารด้วยศูนย์ได้")

def clean():
    entry1.delete(0, END)
    entry2.delete(0, END)
    result_label.config(text=f"ผลลัพธ์: ")

# สร้างหน้าต่างหลัก
root = Tk()
root.title("โปรแกรมคำนวณตัวเลข")
root.geometry("300x200+500+200")

num1 = StringVar()
num2 = StringVar()

# สร้าง Label และ Entry สำหรับรับค่าจากผู้ใช้
label1 = Label(root, text="ใส่ตัวเลขที่ 1:")
label1.pack()

entry1 = Entry(root, textvariable=num1)
entry1.pack()

label2 = Label(root, text="ใส่ตัวเลขที่ 2:")
label2.pack()

entry2 = Entry(root, textvariable=num2)
entry2.pack()

# สร้าง Label สำหรับแสดงผลลัพธ์
result_label = Label(root, text="ผลลัพธ์: ")
result_label.pack()


# สร้างปุ่มสำหรับคำนวณ
btnAdd = Button(root, text="บวก", command=add, width=7)
btnAdd.pack(side="left")

btnDel = Button(root, text="ลบ", command=delete, width=7)
btnDel.pack(side="left")

btnMulti = Button(root, text="คูณ", command=multi,  width=7)
btnMulti.pack(side="left")

btnDiv = Button(root, text="หาร", command=div, width=7)
btnDiv.pack(side="left")

btnClean = Button(root, text="ล้าง", command=clean, width=7)
btnClean.pack(side="left")

# รันโปรแกรม
root.mainloop()

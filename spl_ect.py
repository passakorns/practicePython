import tkinter as tk
from tkinter import messagebox

# ฟังก์ชันสำหรับการคำนวณ
def calculate():
    try:
        # ดึงค่าจาก Entry และแปลงเป็นตัวเลข
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result = num1 / num2

        # แสดงผลลัพธ์ใน Label
        result_label.config(text=f"ผลลัพธ์: {result:.3f}")
    except ValueError:
        # กรณีที่แปลงเป็น float ไม่ได้
        messagebox.showerror("Error", "กรุณากรอกตัวเลขที่ถูกต้อง")
    except ZeroDivisionError:
        # กรณีหารด้วย 0
        messagebox.showerror("Error", "ไม่สามารถหารด้วยศูนย์ได้")

# สร้างหน้าต่างหลัก
root = tk.Tk()
root.title("โปรแกรมคำนวณหาร")

# สร้าง Label และ Entry สำหรับรับค่าจากผู้ใช้
label1 = tk.Label(root, text="ใส่ตัวเลขที่ 1:")
label1.pack()

entry1 = tk.Entry(root)
entry1.pack()

label2 = tk.Label(root, text="ใส่ตัวเลขที่ 2:")
label2.pack()

entry2 = tk.Entry(root)
entry2.pack()

# สร้างปุ่มสำหรับคำนวณ
calculate_button = tk.Button(root, text="คำนวณ", command=calculate)
calculate_button.pack()

# สร้าง Label สำหรับแสดงผลลัพธ์
result_label = tk.Label(root, text="ผลลัพธ์: ")
result_label.pack()

# รันโปรแกรม
root.mainloop()

import tkinter as tk
from tkinter import messagebox
import random

# สร้างเลขสุ่มที่ต้องการให้ผู้ใช้ทาย
secret_number = random.randint(1, 100)

# ฟังก์ชันสำหรับการทายตัวเลข
def guess_number():
    try:
        # รับค่าจาก Entry และแปลงเป็นตัวเลข
        guess = int(entry.get())
        
        # ตรวจสอบว่าเลขที่ทายถูกต้องหรือไม่
        if guess < 1 or guess > 100:
            raise ValueError("กรุณากรอกตัวเลขระหว่าง 1 ถึง 100")
        
        if guess < secret_number:
            result_label.config(text="ทายต่ำไป!")
        elif guess > secret_number:
            result_label.config(text="ทายสูงไป!")
        else:
            result_label.config(text="ทายถูกต้องแล้ว! คุณชนะ!")
            messagebox.showinfo("ชนะ", "ทายถูกต้องแล้ว! เกมจบ!")
            reset_game()
    except ValueError:
        messagebox.showerror("Error", "กรุณากรอกตัวเลขที่ถูกต้อง")
    
# ฟังก์ชันสำหรับรีเซ็ตเกม
def reset_game():
    global secret_number
    secret_number = random.randint(1, 100)
    result_label.config(text="ทายเลขใหม่อีกครั้ง!")
    entry.delete(0, tk.END)

# สร้างหน้าต่างหลัก
root = tk.Tk()
root.title("เกมทายตัวเลข")

# สร้าง Label สำหรับแนะนำการเล่น
instruction_label = tk.Label(root, text="ทายเลขระหว่าง 1 ถึง 100:")
instruction_label.pack()

# สร้าง Entry สำหรับรับค่าตัวเลขที่ผู้ใช้ทาย
entry = tk.Entry(root)
entry.pack()

# สร้างปุ่มสำหรับทายตัวเลข
guess_button = tk.Button(root, text="ทาย", command=guess_number)
guess_button.pack()

# สร้าง Label สำหรับแสดงผลลัพธ์
result_label = tk.Label(root, text="")
result_label.pack()

# สร้างปุ่มสำหรับรีเซ็ตเกม
reset_button = tk.Button(root, text="เริ่มเกมใหม่", command=reset_game)
reset_button.pack()

# รันโปรแกรม
root.mainloop()

from tkinter import *
import subprocess

root = Tk()
root.title("Face Attendance System")
root.geometry("500x400")

def register():
    subprocess.Popen(["python", "register.py"])

def attendance():
    subprocess.Popen(["python", "attendance.py"])

def login():
    subprocess.Popen(["python", "login.py"])

Button(root,text="Admin Login",
       command=login,width=20).pack(pady=10)

Button(root,text="Register Student",
       command=register,width=20).pack(pady=10)

Button(root,text="Start Attendance",
       command=attendance,width=20).pack(pady=10)

Button(root,text="Exit",
       command=root.destroy,width=20).pack(pady=10)

root.mainloop()
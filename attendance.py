import pandas as pd
import os

file_path = r"C:\Users\HP\OneDrive\Desktop\Face-Attendence-Sytem\database\attendance.xlsx"

# Create the file if it doesn't exist or is empty
if not os.path.exists(file_path) or os.path.getsize(file_path) == 0:
    df = pd.DataFrame(columns=["Name", "Date", "Time"])
    df.to_excel(file_path, index=False, engine="openpyxl")
    print("Created new attendance file.")
else:
    df = pd.read_excel(file_path, engine="openpyxl")
    print("File loaded successfully.")

today = "06-06-2026"
name = "Pranab Naskar"

if ((df["Name"] == name) & (df["Date"] == today)).any():
    print("Already Marked Today")
else:
    print("Attendance Added")
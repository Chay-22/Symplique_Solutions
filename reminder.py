import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
from datetime import datetime

# ---------- Database Setup ----------
conn = sqlite3.connect('reminders.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS reminders (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT,
        time TEXT,
        message TEXT,
        reminder_type TEXT
    )
''')
conn.commit()

# ---------- Functions ----------
def submit_reminder():
    date = date_entry.get()
    time = time_entry.get()
    message = message_entry.get("1.0", tk.END).strip()
    reminder_type = reminder_type_var.get()

    if not date or not time or not message or not reminder_type:
        messagebox.showerror("Error", "All fields are required.")
        return

    try:
        datetime.strptime(f"{date} {time}", "%Y-%m-%d %H:%M")
    except ValueError:
        messagebox.showerror("Error", "Date/Time format is invalid.\nUse YYYY-MM-DD and HH:MM (24hr).")
        return

    cursor.execute("INSERT INTO reminders (date, time, message, reminder_type) VALUES (?, ?, ?, ?)",
                   (date, time, message, reminder_type))
    conn.commit()

    messagebox.showinfo("Success", "🎉 Reminder saved successfully!")
    clear_fields()

def clear_fields():
    date_entry.delete(0, tk.END)
    time_entry.delete(0, tk.END)
    message_entry.delete("1.0", tk.END)
    reminder_type_var.set("")

# ---------- GUI Setup ----------
root = tk.Tk()
root.title("⏰ Remind-Me-Later")
root.geometry("450x500")
root.config(bg="silver")

# ---------- Styles ----------
label_font = ("Rockwell", 11, "bold")
entry_font = ("Rockwell", 10)
bg_color = "snow"
accent_color = "#4CAF50"
button_font = ("Rockwell", 10, "bold")

# ---------- Header ----------
tk.Label(root, text="Remind-Me-Later", font=("Rockwell", 16, "bold"),
         fg="Black", bg="silver").pack(pady=20)

# ---------- Form Frame ----------
form_frame = tk.Frame(root, bg=bg_color)
form_frame.pack(pady=10)

# ---------- Date ----------
tk.Label(form_frame, text="📅 Date (YYYY-MM-DD):", font=label_font, bg=bg_color).grid(row=0, column=0, sticky="w", pady=5)
date_entry = tk.Entry(form_frame, font=entry_font, width=30)
date_entry.grid(row=0, column=1, pady=5)

# ---------- Time ----------
tk.Label(form_frame, text="⏰ Time (HH:MM 24hr):", font=label_font, bg=bg_color).grid(row=1, column=0, sticky="w", pady=5)
time_entry = tk.Entry(form_frame, font=entry_font, width=30)
time_entry.grid(row=1, column=1, pady=5)

# ---------- Message ----------
tk.Label(form_frame, text="💬 Reminder Message:", font=label_font, bg=bg_color).grid(row=2, column=0, sticky="nw", pady=5)
message_entry = tk.Text(form_frame, font=entry_font, height=5, width=30)
message_entry.grid(row=2, column=1, pady=5)

# ---------- Reminder Type ----------
tk.Label(form_frame, text="📨 Reminder Type:", font=label_font, bg=bg_color).grid(row=3, column=0, sticky="w", pady=5)
reminder_type_var = tk.StringVar()
reminder_dropdown = ttk.Combobox(form_frame, textvariable=reminder_type_var, font=entry_font, width=28, state="readonly")
reminder_dropdown['values'] = ('email', 'sms')
reminder_dropdown.grid(row=3, column=1, pady=5)

# ---------- Submit Button ----------
submit_btn = tk.Button(root, text="Save Reminder", command=submit_reminder,
                       bg="gray", fg="snow", font="Rockwell", width=20, relief="flat", pady=8)
submit_btn.pack(pady=30)

# ---------- Footer ----------
tk.Label(root, text="Built using Tkinter", font=("Rockwell", 12), bg="silver", fg="black").pack(side="bottom", pady=10)

root.mainloop()

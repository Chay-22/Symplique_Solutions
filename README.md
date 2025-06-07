# Symplique_Solutions

# ⏰ Remind-Me-Later

A visually appealing desktop application built with Python and Tkinter that allows users to schedule reminders with a message, date, time, and delivery type (Email or SMS).

> ✅ Submission for the Full Stack Developer position screening assignment at Symplique Solutions.

---

## 🖥 Features

- Elegant and modern GUI using Tkinter
- Collects:
  - 📅 Date (YYYY-MM-DD)
  - ⏰ Time (HH:MM - 24hr format)
  - 💬 Reminder Message
  - 📨 Reminder Type (Email or SMS)
- Stores reminders locally in SQLite database
- Input validation with error messages
- Clean layout with themed buttons and fonts

---

## 🛠 Tech Stack

- Python 3
- Tkinter (for GUI)
- SQLite (for local data storage)

---

## 📋 Project Structure

- `remind_me_gui.py` - Main Python script containing the GUI and database logic
- `reminders.db` - SQLite database file created automatically on first run

---

## 🧠 Code Explanation

This is a standalone desktop GUI app that accepts and stores reminder details. Here's how it works:

### 1. Database Setup

- Connects to an SQLite database `reminders.db`.
- Creates a table `reminders` with columns: `id`, `date`, `time`, `message`, `reminder_type` if it doesn't exist.

### 2. User Input and Validation

- Users enter the date (YYYY-MM-DD), time (HH:MM 24hr format), reminder message, and select reminder type (email or sms).
- The app validates that all fields are filled.
- Validates date and time formats using Python's `datetime.strptime`.
- Shows error popup if inputs are invalid.

### 3. Saving Reminder

- Upon successful validation, reminder details are inserted into the SQLite database.
- A success message popup confirms the save.
- Input fields are cleared for new entries.

### 4. GUI Design

- The interface is built with Tkinter widgets (`Label`, `Entry`, `Text`, `Combobox`, `Button`).
- Uses custom fonts and colors for a clean and user-friendly look.
- The form fields are grouped inside a frame with padding.
- The app window is sized to 450x500 pixels with a silver background.

---

## 🚀 How to Run

### Prerequisites

- Python 3.x installed on your system
- Tkinter (usually comes pre-installed with Python)
- No external libraries required

### Steps

1. Clone the repository:

2. Run the application:
  
3. The GUI window will open. Fill in the date, time, message, and select reminder type, then click **Save Reminder**.

4. Your reminder will be saved in the local SQLite database `reminders.db`.

---

## 📬 Contact

Created by:- Chay-22
📧 chaitanyasarve@2912gmail.com  

---

## 📝 Disclaimer

This application **does not** send actual SMS or Email messages. It only stores the scheduled reminder information locally in a database, as per assignment requirements.

---

Thank you for reviewing my submission! I look forward to your feedback.

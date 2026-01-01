import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
from zoneinfo import ZoneInfo

# ---------------- WINDOW ----------------
window = tk.Tk()
window.title("Time Zone Calculator")
window.resizable(False, False)
window.configure(bg="#0F172A")

# ---------------- COLORS ----------------
BLUE = "#2563EB"
DARK = "#0F172A"
GRAY = "#94A3B8"
WHITE = "white"

# ---------------- TIME ZONES ----------------
TIME_ZONES = {
    "India (IST)": "Asia/Kolkata",
    "UTC": "UTC",
    "USA (EST)": "America/New_York",
    "USA (PST)": "America/Los_Angeles",
    "UK (BST)": "Europe/London",
    "Japan (JST)": "Asia/Tokyo",
    "Australia (AEST)": "Australia/Sydney"
}

# ---------------- FUNCTIONS ----------------
def calculate_time():
    try:
        time_str = time_entry.get().strip()
        from_zone = TIME_ZONES[from_combo.get()]
        to_zone = TIME_ZONES[to_combo.get()]

        base_time = datetime.strptime(time_str, "%H:%M")
        base_time = base_time.replace(
            tzinfo=ZoneInfo(from_zone),
            year=datetime.now().year,
            month=datetime.now().month,
            day=datetime.now().day
        )

        converted = base_time.astimezone(ZoneInfo(to_zone))

        result_label.config(
            text=converted.strftime("%H:%M (%d %b %Y)")
        )

    except Exception:
        messagebox.showerror(
            "Invalid Input",
            "Enter time in HH:MM format (24-hour)"
        )

# ---------------- UI ----------------
header = tk.Label(
    window,
    text="Time Zone Calculator",
    font=("Arial", 18, "bold"),
    bg="#1E293B",
    fg=WHITE,
    pady=10
)
header.pack(fill="x")

frame = tk.Frame(window, bg=DARK, padx=20, pady=20)
frame.pack()

tk.Label(frame, text="Time (HH:MM)", bg=DARK, fg=GRAY).grid(row=0, column=0, sticky="w")
time_entry = tk.Entry(frame, font=("Arial", 12), width=15)
time_entry.grid(row=1, column=0, pady=5)

tk.Label(frame, text="From Time Zone", bg=DARK, fg=GRAY).grid(row=2, column=0, sticky="w", pady=(10,0))
from_combo = ttk.Combobox(frame, values=list(TIME_ZONES.keys()), state="readonly")
from_combo.grid(row=3, column=0, pady=5)
from_combo.set("India (IST)")

tk.Label(frame, text="To Time Zone", bg=DARK, fg=GRAY).grid(row=4, column=0, sticky="w", pady=(10,0))
to_combo = ttk.Combobox(frame, values=list(TIME_ZONES.keys()), state="readonly")
to_combo.grid(row=5, column=0, pady=5)
to_combo.set("UTC")

calc_btn = tk.Button(
    frame,
    text="Convert Time",
    font=("Arial", 12, "bold"),
    bg=BLUE,
    fg=WHITE,
    width=20,
    command=calculate_time
)
calc_btn.grid(row=6, column=0, pady=15)

result_label = tk.Label(
    frame,
    text="Converted time will appear here",
    bg=DARK,
    fg=WHITE,
    font=("Arial", 13)
)
result_label.grid(row=7, column=0)

# ---------------- CENTER WINDOW ----------------
window.update()
w, h = window.winfo_width(), window.winfo_height()
x = (window.winfo_screenwidth() // 2) - (w // 2)
y = (window.winfo_screenheight() // 2) - (h // 2)
window.geometry(f"{w}x{h}+{x}+{y}")

window.mainloop()

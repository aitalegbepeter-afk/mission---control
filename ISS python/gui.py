import tkinter as tk
import api
import database


def check_position():
    global label
    try:
       pos = api.get_iss_position()
       database.save_position(pos["latitude"], pos["longitude"])
       label.config(text=f"Lat: {pos['latitude']}, Lon: {pos['longitude']}")
    except Exception as error:
       label.config(text=f"Status check failed: {error}")

def view_history():
    global history_label
    rows = database.get_all_positions()
    history_text = "\n".join(str(row) for row in rows[:8])
    history_label.config(text=history_text or "No logs yet.")


def start_gui():
    global label, history_label
    database.setup_database()
    window = tk.Tk()
    window.title("Mission Control")
    window.geometry("350x180")
    label = tk.Label(window, text="ISS Mission Control Dashboard")
    label.pack(pady=20)
    tk.Button(window, text="Run Status Check", command=check_position).pack()
    tk.Button(window, text="View History", command=view_history).pack(pady=8)
    history_label = tk.Label(window, text="No logs yet.", justify="left")
    history_label.pack()
    window.config(bg="midnight blue")
    label.config(font=("Arial", 16))
    window.mainloop()
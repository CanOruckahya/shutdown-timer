import tkinter as tk
import os

def schedule_shutdown(hours, minutes):
    seconds = hours * 3600 + minutes * 60
    os.system(f"shutdown -s -t {seconds}")

def cancel_shutdown():
    os.system("shutdown -a")
    status_label.config(text="Kapanma iptal edildi")

def set_shutdown():
    try:
        time_input = time_entry.get().strip()
        if not time_input:
            status_label.config(text="Süre girin")
            return
            
        # Parse time input like "3.35" (3 hours 35 minutes)
        if '.' in time_input:
            parts = time_input.split('.')
            if len(parts) == 2:
                h = int(parts[0])
                m = int(parts[1])
                # Handle cases like "3.5" (3 hours 5 minutes) vs "3.50" (3 hours 50 minutes)
                if len(parts[1]) == 1:
                    m = m * 10  # "3.5" means 3 hours 50 minutes
            else:
                status_label.config(text="Geçersiz format (örn: 3.35)")
                return
        else:
            # If no decimal point, treat as minutes only
            m = int(time_input)
            h = 0
            
        total_seconds = h * 3600 + m * 60
        if total_seconds <= 0:
            status_label.config(text="0'dan büyük bir süre girin")
            return
        schedule_shutdown(h, m)
        status_label.config(text=f"PC {h} saat {m} dk sonra kapanacak")
    except ValueError:
        status_label.config(text="Geçerli sayı girin (örn: 3.35)")

root = tk.Tk()
root.title("PC Kapatma Zamanlayıcı")

tk.Label(root, text="Süre (örn: 3.35 = 3 saat 35 dk):").pack(pady=2)
time_entry = tk.Entry(root)
time_entry.pack(pady=2)

tk.Button(root, text="Zamanla", command=set_shutdown).pack(pady=5)
tk.Button(root, text="İptal Et", command=cancel_shutdown).pack(pady=5)

status_label = tk.Label(root, text="")
status_label.pack(pady=10)

root.mainloop()

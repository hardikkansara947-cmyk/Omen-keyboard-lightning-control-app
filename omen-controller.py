#!/usr/bin/env python3
import tkinter as tk
from tkinter import colorchooser
import subprocess
import os

RGB_PATH = "/sys/devices/platform/omen-rgb-keyboard/rgb_zones"

def write_driver(file_name, value):
    try:
        path = os.path.join(RGB_PATH, file_name)
        subprocess.run(["sudo", "tee", path], input=f"{value}\n", text=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except Exception as e:
        print(f"Error: {e}")

class OmenControllerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("OMEN Lighting Control")
        self.root.geometry("420x540")
        self.root.resizable(False, False)
        self.root.configure(bg="#121212")

        write_driver("animation_mode", "off")

        self.current_hex = "8B0000"

        title = tk.Label(root, text="VICTUS / OMEN RGB", font=("Arial", 16, "bold"), fg="#ffffff", bg="#121212")
        title.pack(pady=(20, 10))

        self.preview = tk.Frame(root, width=320, height=80, bg=f"#{self.current_hex}", relief="flat", highlightbackground="#333333", highlightthickness=2)
        self.preview.pack(pady=10)
        self.preview.pack_propagate(False)

        self.hex_label = tk.Label(self.preview, text=f"#{self.current_hex}", font=("Arial", 13, "bold"), fg="#ffffff", bg=f"#{self.current_hex}")
        self.hex_label.pack(expand=True)

        pick_btn = tk.Button(root, text="Open Color Picker Wheel", font=("Arial", 11, "bold"),
                             bg="#e50914", fg="#ffffff", activebackground="#b80710", activeforeground="#ffffff",
                             relief="flat", padx=15, pady=8, cursor="hand2", command=self.open_color_picker)
        pick_btn.pack(pady=12)

        bright_label = tk.Label(root, text="BRIGHTNESS", font=("Arial", 10, "bold"), fg="#888888", bg="#121212")
        bright_label.pack(anchor="w", padx=50, pady=(10, 0))

        self.slider = tk.Scale(root, from_=0, to=100, orient="horizontal", bg="#121212", fg="#ffffff",
                               highlightthickness=0, troughcolor="#222222", activebackground="#e50914",
                               command=self.set_brightness)
        self.slider.set(100)
        self.slider.pack(fill="x", padx=50, pady=(0, 15))

        preset_title = tk.Label(root, text="QUICK PRESETS", font=("Arial", 10, "bold"), fg="#888888", bg="#121212")
        preset_title.pack(anchor="w", padx=50, pady=(5, 5))

        preset_frame = tk.Frame(root, bg="#121212")
        preset_frame.pack(padx=50, pady=5)

        presets = [
            ("Dark Red", "8B0000"), ("Bright Red", "FF0000"),
            ("Dim Orange", "7A2500"), ("Cyan", "00FFFF"),
            ("Deep Blue", "00008B"), ("Purple", "4B0082"),
            ("Soft White", "AAAAAA"), ("Off", "000000")
        ]

        for i, (name, hex_val) in enumerate(presets):
            row = i // 2
            col = i % 2
            btn = tk.Button(preset_frame, text=name, font=("Arial", 9, "bold"),
                            bg=f"#{hex_val}" if hex_val != "000000" else "#202020",
                            fg="#ffffff", activeforeground="#ffffff",
                            width=14, pady=5, relief="flat", cursor="hand2",
                            command=lambda h=hex_val: self.apply_hex(h))
            btn.grid(row=row, column=col, padx=5, pady=5)

        self.apply_hex(self.current_hex)

    def apply_hex(self, hex_val):
        self.current_hex = hex_val.upper()
        self.preview.configure(bg=f"#{self.current_hex}")
        self.hex_label.configure(text=f"#{self.current_hex}", bg=f"#{self.current_hex}")
        write_driver("all", self.current_hex)
        write_driver("zone00", self.current_hex)

    def set_brightness(self, val):
        write_driver("brightness", val)

    def open_color_picker(self):
        chosen = colorchooser.askcolor(title="Choose Keyboard Color", color=f"#{self.current_hex}")
        if chosen and chosen[1]:
            new_hex = chosen[1].replace("#", "")
            self.apply_hex(new_hex)

if __name__ == "__main__":
    app_root = tk.Tk()
    app = OmenControllerApp(app_root)
    app_root.mainloop()

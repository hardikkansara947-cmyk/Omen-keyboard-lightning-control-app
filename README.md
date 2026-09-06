# OMEN / Victus Linux Keyboard Lighting Control

A lightweight, persistent graphical dashboard built with Python/Tkinter to manage and customize RGB keyboard lighting on HP Victus and HP OMEN laptops running Linux.

---

## Requirements

### 1. Hardware
* **Device:** HP Victus or HP OMEN laptop with single-zone or multi-zone RGB backlit keyboard.
* **BIOS:** Factory HP WMI interface enabled (default state).

### 2. Operating System
* **OS:** Debian, Linux Mint, Ubuntu, or derivative distributions.
* **Kernel:** 5.15 or newer recommended.
* **Privileges:** Sudo access required during initial installation for udev rules and hardware node permissions.

### 3. Core Software & Drivers
* **Driver Module:** [`omen-rgb-keyboard`](https://github.com/thesofproject/omen-rgb-keyboard) kernel module installed and active (`lsmod | grep omen`).
* **Python Runtime:** Python 3.8+ (`python3`).
* **GUI Toolkit:** Python Tkinter bindings (`python3-tk`).
* **System Tools:** `coreutils` (`tee`), `bash`, `zenity`.

---

## Features

* **Persistent GUI:** Stays open on screen; does not close unexpectedly after selecting a color.
* **Full RGB Spectrum:** Interactive color picker wheel supporting millions of hex colors.
* **Quick Color Presets:** Instant one-click selection for Dark Red, Bright Red, Dim Orange, Cyan, Deep Blue, Purple, Soft White, and Off.
* **Live Brightness Slider:** Smooth brightness adjustment from 0% to 100%.
* **Animation Override:** Automatically halts driver animation loops to ensure static colors display immediately.
* **Desktop Menu Integration:** Adds a standard launcher entry to your system's application menu.

---

## Installation

1. Clone the repository:
   ```bash
   git clone [https://github.com/hardikkansara947-cmyk/Omen-keyboard-lightning-control-app.git](https://github.com/hardikkansara947-cmyk/Omen-keyboard-lightning-control-app.git)
   cd Omen-keyboard-lightning-control-appchmod +x install.sh
./install.shUsage
Launch from Application Menu

Open your system application menu, search for OMEN Lighting Control, and click the icon.
Launch from Terminal
Bash

~/.local/bin/omen-controller
How It Works

HP OMEN and Victus keyboards interact with the system via direct sysfs hardware attributes created by the omen-rgb-keyboard driver:

    Mode control: /sys/devices/platform/omen-rgb-keyboard/rgb_zones/animation_mode

    Brightness control: /sys/devices/platform/omen-rgb-keyboard/rgb_zones/brightness

    Color allocation: /sys/devices/platform/omen-rgb-keyboard/rgb_zones/all and zone00

The application communicates directly with these kernel sysfs nodes while bypassing root password prompts via dedicated udev/sudo permissions configured by install.sh.
Troubleshooting

    Keyboard color does not change:
    Verify the driver is loaded:
    Bash

    lsmod | grep omen

    Check driver logs for ACPI communication:
    Bash

    sudo dmesg | grep -i omen

    Permissions error when setting color:
    Reapply the udev permissions rule:
    Bash

    echo "$USER ALL=(ALL) NOPASSWD: /usr/bin/tee /sys/devices/platform/omen-rgb-keyboard/rgb_zones/*" | sudo tee /etc/sudoers.d/omen-rgb

Uninstallation

To remove the controller and desktop launcher completely:
Bash

rm -f ~/.local/bin/omen-controller
rm -f ~/.local/share/applications/omen-lighting.desktop
sudo rm -f /etc/sudoers.d/omen-rgb
update-desktop-database ~/.local/share/applications 2>/dev/null || true

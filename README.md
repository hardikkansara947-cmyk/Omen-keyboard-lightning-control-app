# **OMEN / Victus Linux Keyboard Lighting Control**

> A lightweight, persistent graphical dashboard built with **Python/Tkinter** to manage and customize RGB keyboard lighting on **HP Victus** and **HP OMEN** laptops running **Linux**.

---

### **Quick Navigation**
* [**Requirements**](#requirements)
* [**Features**](#features)
* [**Installation Options**](#installation-options)
  * [**Option 1: Debian / Ubuntu / Mint (.deb)**](#option-1-debian--ubuntu--linux-mint-deb-package--recommended)
  * [**Option 2: Portable AppImage**](#option-2-standalone-portable-appimage)
  * [**Option 3: Manual Source Installation**](#option-3-manual-source-installation)
* [**Usage**](#usage)
* [**How It Works**](#how-it-works)
* [**Troubleshooting**](#troubleshooting)
* [**Uninstallation**](#uninstallation)

---

## **Requirements**

### **1. Hardware**
* **Device:** **HP Victus** or **HP OMEN** laptop with single-zone or multi-zone RGB backlit keyboard.
* **BIOS:** Factory **HP WMI** interface enabled (default state).

### **2. Operating System**
* **OS:** **Debian**, **Linux Mint**, **Ubuntu**, **Arch Linux**, or derivative distributions.
* **Kernel:** Version **5.15** or newer recommended.
* **Privileges:** **Sudo access** required during initial installation for hardware node permissions.

### **3. Core Software & Drivers**
* **Driver Module:** [**omen-rgb-keyboard**](https://github.com/thesofproject/omen-rgb-keyboard) kernel module installed and active (`lsmod | grep omen`).
* **Python Runtime:** **Python 3.8+** (`python3`).
* **GUI Toolkit:** Python Tkinter bindings (**`python3-tk`**).
* **System Tools:** **`coreutils`** (`tee`), **`bash`**.

---

## **Features**

* **Dedicated Power Controls:** Fast one-click **Turn ON** and **Turn OFF** buttons.
* **Persistent GUI:** Stays open on screen; does not close unexpectedly after selecting a color.
* **Full RGB Spectrum:** Interactive color picker wheel supporting millions of hex colors.
* **Quick Color Presets:** Instant one-click selection for presets and primary shades.
* **Live Brightness Slider:** Smooth brightness adjustment from **0% to 100%**.
* **Auto-Restore on Boot:** Automatically saves preferences and restores your color when you log in.
* **Desktop Menu Integration:** Installs a standard desktop icon and launcher entry.

---

## **Installation Options**

Choose the installation method that best matches your distribution and workflow:

### **Option 1: Debian / Ubuntu / Linux Mint (`.deb` Package) — Recommended**

Installs system-wide with application shortcuts, launcher icons, and permission configurations automatically.

1. Download the latest **`.deb`** package from the [**Releases**](https://github.com/hardikkansara947-cmyk/Omen-keyboard-lightning-control-app/releases/latest) page.
2. Install the package using **`apt`**:
   ```bash
   sudo apt install ./omen-keyboard-lightning-control_2.0.0_all.deb

(Or double-click the downloaded .deb file in your desktop file manager).

**Option 2: Standalone Portable (.AppImage)**

Runs directly on any Linux distribution without system-level installation.

    Download the latest .AppImage file from the Releases page.

    Mark the file as executable:
    Bash

    chmod +x Omen-Lighting-Control-2.0.0-x86_64.AppImage

    Run the application:
    Bash

    ./Omen-Lighting-Control-2.0.0-x86_64.AppImage

**Option 3: Manual Source Installation**

    Clone the repository:
    Bash

    git clone [https://github.com/hardikkansara947-cmyk/Omen-keyboard-lightning-control-app.git](https://github.com/hardikkansara947-cmyk/Omen-keyboard-lightning-control-app.git)
    cd Omen-keyboard-lightning-control-app

    Make the installer executable and run it:
    Bash

    chmod +x install.sh
    ./install.sh

**Usage**

    Launch from Application Menu: Open your desktop application launcher, search for OMEN Lighting Control, and click the launcher icon.

    Launch from Terminal:
    Bash

    omen-controller

    (If installed manually via script, use ~/.local/bin/omen-controller)

    Restore Profile on Login (Headless):
    Bash

    omen-controller --restore
**
How It Works**

HP OMEN and Victus keyboards interact with the system via direct sysfs hardware attributes created by the omen-rgb-keyboard driver:

    Mode control: /sys/devices/platform/omen-rgb-keyboard/rgb_zones/animation_mode

    Brightness control: /sys/devices/platform/omen-rgb-keyboard/rgb_zones/brightness

    Color allocation: /sys/devices/platform/omen-rgb-keyboard/rgb_zones/all and /sys/devices/platform/omen-rgb-keyboard/rgb_zones/zone00

The application communicates directly with these kernel sysfs nodes while bypassing root password prompts via dedicated permissions configured in /etc/sudoers.d/omen-rgb. Configuration files are saved locally to ~/.config/omen-rgb/config.json.

**Troubleshooting**
Keyboard color does not change

Verify that the kernel module is active:
Bash

lsmod | grep omen

Check driver messages in the kernel log:
Bash

sudo dmesg | grep -i omen
**
Permissions error when setting color**

Verify that passwordless access to the RGB nodes is configured:
Bash

echo "$USER ALL=(ALL) NOPASSWD: /usr/bin/tee /sys/devices/platform/omen-rgb-keyboard/rgb_zones/*" | sudo tee /etc/sudoers.d/omen-rgb
sudo chmod 0440 /etc/sudoers.d/omen-rgb

**Uninstallation**

    If installed via .deb package:
    Bash

    sudo apt remove omen-keyboard-lightning-control

    If installed via install.sh:
    Bash

    rm -f ~/.local/bin/omen-controller
    rm -f ~/.local/share/applications/omen-lighting.desktop
    rm -f ~/.config/autostart/omen-lighting-autostart.desktop
    rm -rf ~/.config/omen-rgb
    sudo rm -f /etc/sudoers.d/omen-rgb
    update-desktop-database ~/.local/share/applications 2>/dev/null || true

    If using AppImage:
    Delete the .AppImage file and clear the local settings folder:
    Bash

    rm -rf ~/.config/omen-rgb

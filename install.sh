#!/usr/bin/env bash
set -e

echo "Installing dependencies..."
sudo apt update && sudo apt install -y python3-tk zenity

echo "Installing application..."
mkdir -p ~/.local/bin ~/.local/share/applications
cp omen-controller.py ~/.local/bin/omen-controller
chmod +x ~/.local/bin/omen-controller

cat << DESKTOP > ~/.local/share/applications/omen-lighting.desktop
[Desktop Entry]
Type=Application
Name=OMEN Lighting Control
Comment=Control HP Victus RGB keyboard lighting
Exec=python3 $HOME/.local/bin/omen-controller
Icon=preferences-desktop-theme
Terminal=false
Categories=Settings;HardwareSettings;Utility;
DESKTOP

chmod +x ~/.local/share/applications/omen-lighting.desktop
update-desktop-database ~/.local/share/applications 2>/dev/null || true

echo "Setting up udev/sudo permissions for non-root control..."
echo "$USER ALL=(ALL) NOPASSWD: /usr/bin/tee /sys/devices/platform/omen-rgb-keyboard/rgb_zones/*" | sudo tee /etc/sudoers.d/omen-rgb > /dev/null

echo "Installation complete! You can launch 'OMEN Lighting Control' from your application menu."

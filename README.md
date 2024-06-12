# Access-Blocker
A fully functioning tool to block access to the computer via a password. No need to lock!

# About
You know those times, when you need to get away from your PC/Laptop and want to block access to the computer, but you dont want to Lock it? That is when this tool comes in handy.

It is written in Python and uses the default Tkinter GUI Framework. It prevents you from closing in any way possible: Alt F4 doesn't work with it, it is full screen so no close buttons, it remains always on top, and it auto-closes the start menu if you try to open it. The only way to close it is to either enter the correct password or to just restart using the power button. 

# Interface
I am not actually that good with PySide or PyQT so you are encouraged to open a pull request to move Tk into Qt, because Tk is very basic.

# Compatibility
The application was built for the Windows operating system, and testing on Linux is yet to be done. It might work out if I change some code but it might need to completely change the entire code. Compatibility with macOS is not to be expected and will not be officially tested as I don't use macOS. 

# Running
You can either download the executables from the [Releases](https://github.com/Chocolandia-Software/Access-Blocker/releases) for your computer or you can run the Python file. To do so, first install PyAutoGUI:

```
pip install pyautogui
```
remember to use pip3 if it doesn't work. Then:
```
python "path\to\Security Vault.py"
```
Again, use python3 if that doesn't work.
Python 3.11 is recommended. I use 3.11.5.

# Building
If you want to build it into an EXE yourself, use the PyInstaller command 
```
pyinstaller --noconfirm --onedir --windowed  "path\to\Security Vault.py"
```
I built it with Auto Py To EXE which basically is a GUI for PyInstaller because I'm too lazy to read the PyInstaller Documentation.

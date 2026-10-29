# Python Autoclicker

A simple autoclicker that repeatedly left-clicks at the current mouse cursor position. Use keyboard shortcuts to start, pause, or quit.

## Setup

Requires Python 3 and the `pyautogui` and `keyboard` packages.

On Windows, double-click `install_dependencies.bat` to install the dependencies. Python must be installed and available on PATH.

Alternatively, open a terminal in this folder and run:

```sh
python -m pip install -r requirements.txt
```

## Usage

Open a terminal in this folder and run:

```sh
python autoclicker.py
```

Move your cursor to the desired location, then use these shortcuts:

| Key | Action |
| --- | --- |
| F6 | Start or pause clicking |
| Esc | Quit the program |

Clicking is paused when the program starts.

## Click speed

The default target speed is **20 clicks per second**. To change it, edit `clicks_per_second` in `autoclicker.py`. Use a positive number; actual speed depends on system performance.

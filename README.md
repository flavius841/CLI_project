# CLI_project

This is a CLI project. It helps you to create files, find text, and edit them.
NOTE: this CLI only works in the folder you are in.


To run it you need to have installed already python and git.

**How to install python on MacOS**
Go to the official site: https://www.python.org/downloads/macos/
Download the .pkg installer.
Open it and follow the steps.

Then you need to install pipx
Run this commands:
1. python3 -m pip install --user pipx
2. python3 -m pipx ensurepath




**How to install python on Linux:**
Run this two commands in your terminal:
        sudo apt update
        sudo apt install python3

Then you need to install pip and pipx
Run this commands:
1. sudo apt install python3-pip
2. sudo apt update
3. sudo apt install pipx


**How to install python on Windows:**
1. Download Python

Go to the official site (safe + free):

https://www.python.org/downloads/windows/

Click the latest "Python 3.x.x" Windows installer.

2. Run the Installer

When the installer opens:

✔ Very important: Check the box “Add Python to PATH”
(If you miss this, Python won’t work in the terminal.)

Then click Install Now.

Once Python and pip are installed:

python -m pip install --user pipx
python -m pipx ensurepath

After running ensurepath, restart Command Prompt.


**How to install Git on MacOS**
If you have Homebrew installed: brew install git


**How to install Git on Linux:**
Just run this commands:
sudo apt update
sudo apt install git

**How to install Git on Windows:**
Go to: https://git-scm.com/download/win
Download the installer and follow the prompts (default options are fine).


After you installed all this you can now use my CLI. Just run this command first: 
pipx install git+https://github.com/flavius841/CLI_project.git

Now if you type file_editor in yor terminal or comand prompt you enter my application






# fusion-files
**Penetration Testing: File Binder and Encrypted Dropper**

**DISCLAIMER:**

**All information and software available in this repository is for educational purposes only. Use these at your own discretion, I cannot be held responsible for any damages caused.
Usage of all tools on this site for attacking targets without prior mutual consent is illegal. It is the end user’s responsibility to obey all applicable local, state and federal laws. I assume no liability and are not responsible for any misuse or damage caused by this project.**

![binaryDL](https://i.imgur.com/wFJh7WL.png)

**Fusion Files**
- The Legitimate File and Payload File will be hidden inside an executeable that extracts both and drops them to one of three locations of your choice: TEMP, APPDATA, or User's Home Folder.
- You can optionally set the icon for the executeable and version file (assembly information). Examples provided in the resources folder.

**Output Scantime Detection:** FUD

**Output Runtime Detection:** Depends on the files being executed. This can vary. If it was detected by 32 AVs before, it will probably be detected shortly after execution.

**Resources:**
- icon_examples: test icons provided
- version_example: test version file provided
- example config file

**Prerequisites to run from Source:**
- Windows 7+
- Python 2.7
- Pyinstaller
  - pip install pyinstaller
- Pywin32
  - pip install pypiwin32
- Pycrypto
  - pip install pycrypto
- wxPython
  - pip install -U wxPython
  
**Prequisites for running Binary:**
- Windows 7+
- Python 2.7
- Pyinstaller
  - pip install pyinstaller
  
**HOW TO RUN FROM SOURCE**
- Follow all of the steps from Prerequisites to run from Source. Then Navigate to the Main.py and you should be able to execute it through your favorite editor or at the command line by simply typing:
  -python Main.py

Questions or Suggestions? Email: RealPoseidOwn@mail.com

If you enjoy using this and would like to support development of this and other open source penetration testing software, consider donating!
**x32 and x64 Binaries**

[![paypal](https://i.imgur.com/IO4eM32.png)](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=J8ZS6X9PEZD7L)

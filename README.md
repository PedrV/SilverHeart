
<p align="center">
  <img width="220" height="220" src="http://g.recordit.co/j7YqWC7u99.gif">
</p>

# SilverHeart
A software fully developed in [Python 3.7](https://www.python.org/), *SilverHeart* is a keylogger concept, that can be deployed in Windows, Mac OS and Linux distributions.

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)     [![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/PedrV/SilverHeart/issues)
[![HitCount](http://hits.dwyl.io/PedrV/SilverHeart.svg)](http://hits.dwyl.io/PedrV/SilverHeart)

# About SilverHeart
*SilverHeart* is a program that when opened will create a decoy file and copy himself to a secure location where it will be alocated. Then it will take the necessery procedures to run on startup and be activelly looking and registrying keystrokes.
When the computer is about to shutdown SilverHeart will ensure the despatch of the log file via email.

# Readme Guide

+ [Installation](https://github.com/PedrV/SilverHeart#installation)
+ [Dependencies](https://github.com/PedrV/SilverHeart#dependencies)
+ [Getting Started](https://github.com/PedrV/SilverHeart#getting-started)
+ [The Process of Creation](https://github.com/PedrV/SilverHeart#the-process-of-creation)
+ [FAQ](https://github.com/PedrV/SilverHeart#faq)
+ [Version and Updates](https://github.com/PedrV/SilverHeart#version-and-updates)
+ [License](https://github.com/PedrV/SilverHeart#license)

## Installation
Clone the repository:
```
git clone https://github.com/PedrV/SilverHeart
```

To install as a module:
```
python setup.py install
```

## Dependencies
- [Pywin32](https://pypi.org/project/pywin32/)
- [pynput](https://pypi.org/project/pynput/)

## Getting Started

After the installation of *SilverHeart*, this is a quick guide to how it is actually structured.

### Windows

___
- The `replicator.py`:

This script is the one who is in charge of once the program is opened, it will create a *"decoy file"* and open that decoy file. Then it will replicate the original program to a safe place, creating a registry key for the program to run on startup.
Togheter with that, it will create a *"variable"* (file) so that it knows how to behave.

___
- The `keeper.py`:

`keeper.py` is a very special script that is a fundemental piece of *SilverHeart*. It will create a invisible window that will be activelly looking for [messages](https://docs.microsoft.com/en-us/windows/desktop/learnwin32/window-messages) sent by windows, specially messages when [logging off](https://docs.microsoft.com/en-us/windows/desktop/shutdown/logging-off) like [WM_QUERYENDSESSION](https://docs.microsoft.com/en-us/windows/desktop/Shutdown/wm-queryendsession).

When such message is intercepted this script will trigger the script that will send the logs via email.

___
- The `sender.py`:

This piece of code will execute only on command of `keeper.py`, it will be responsible for sending the logs via email.

___
- The `logger.py`:

It is without a shadow of a doubt the main script of the whole program. It records the keystrokes when __pressed__ and __released__ with time stamps.

___
- The `executer.py`:

It is this script that makes it happen. Connecting the majors scripts and running them simultaneously using the multiprocessing python library. This is the script to be compiled to actually get a functionally copy of *SilverHeart*. 

![*Building*](https://i.gifer.com/3jnq.gif)


## The Process of Creation
It all started with simple challenge, *build a keylogger from scratch*. Since I was looking for a way to test my python skills I accepted the challenge.
And so was born the SilverHeart program. After some work *(20 hours of work,  distribuited by 10 days, and many documentation reading)* the open source keylogger is ready to be released in the Alpha Version.


## FAQ

## Version and Updates

## Licence

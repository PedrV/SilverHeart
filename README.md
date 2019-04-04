
<p align="center">
  <img width="220" height="220" src="http://g.recordit.co/j7YqWC7u99.gif">
</p>

# SilverHeart
A software fully developed in [Python 3.7](https://www.python.org/), *SilverHeart* is a keylogger concept, that can be deployed in Windows. *(Mac OS and Linux distributions support will be added soon)*.

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

This script is the one who is in charge of once the program is opened, create a *"decoy file"* and open that decoy file. Then it will replicate the original program to a safe place, creating a registry key for the program to run on startup.
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


## The Process of Creation
It all started with simple challenge, *build a keylogger from scratch*. Since I was looking for a way to test my python skills I accepted the challenge.
And so was born the SilverHeart program. After some work *(24 hours of work,  distribuited by 11 days, and many documentation reading)* the open source keylogger is ready to be released in the Alpha Version.

- ##### The first flowchart of the project:

![Flowchart](http://g.recordit.co/QSxROXwIQ8.gif)


___

- ##### Adding registry key to registry:

<p align="left">
  <img width="700" height="300" src="http://g.recordit.co/6zVjrlzIu9.gif">
</p>


## FAQ

- **Can I contribute to *SilverHeart* ?**

Absolutely. Yes you can, contributions are always welcome, modifying or altering the source code is absolutely ok, as long as you follow the license guidelines.

___

- **Is this program spyware ?**

No. This is a keylogger. This is a common misunderstanding, spyware is a category of programs (most times malware, or "malicious software," - an umbrella term that refers to any malicious program or code that is harmful to systems) such as:

1. Trojans - typically malicious software programs that are disguised as legitimate programs. Trojans can delete files, encrypt files for ransom or allow others to have access to the user’s information.

2. Adware - often bundled in with free software, shareware programs and utilities downloaded from the internet. Cookies that track and record users' personal information and internet browsing habits are one of the most common types of adware.

3. Keyloggers - Keyloggers are a type of system monitor that are often used by cybercriminals to steal personally identifiable information, login credentials and sensitive enterprise data. Keyloggers may also be used by employers to observe employees' computer activities, parents to supervise their children's internet usage.


*- So, are keyloggers a program that can be spyware?*

Exactly, keyloggers either software or hardware can be classified as spyware when deployed without 3rd part agreement. Under the right circunstances a keylogger is not classifed as spyware if deployed with the *"victim's"* consent.

___

- **Is keylogger deployment legal ?**

Yes, keylogger deployment is legal, **ONLY** with the *"victim's"* consent. Deploying a keylogger without the other user consent is **HIGHLY** illegal. 

What many spyware producers argue is that, when someone clicks Consent to the license agreement they are consenting to spyware of any kind. Hence, the sypware does not exit on people's computers without their consent, wheter they read the license agreement or not, and it is therefore not violating any laws.


###### [Further Reading](https://searchsecurity.techtarget.com/definition/spyware) of [legal implications](https://www.spamlaws.com/what-is-spyware.html).
 
 ___
 
- **Can I use *SilverHeart* to supervise someone ?**

What you do with this program is 100% all up to you and it is of **YOUR** responsibility. As said before deploying keyloggers without the other part consent is illegal. I as a developer and as a person strongly recommend you to not use this program for 3rd party supervision.

**As a developer this code was made ONLY with learning purpose and is being released with the purpose of share and improvement.**

**With that said I CAN'T AND WIll NOT take any responsiblity with what others do with this code.**

For more informations regarding warranty or liability consulte Section 15, 16 & 17 of the applied [license](https://github.com/PedrV/SilverHeart#license).

___

- **Will *SilverHeart* get updates ?**

If all goes according to plan, I look for maintain this program and update it.
See [Version and Updates](https://github.com/PedrV/SilverHeart#versions-and-updates) for details.

___

## Version and Updates

This section is used for maintain a Version catalog, as whell as displaying information for updates and changelogs.

- Versions

 ##### Alpha:
| Version 1.0 | Released content|
| ------------- | ------------- |
| Windows  | Standard version* fully functional fully tested |
| macOS\Linux  | Standard version* not fully functional <sub>(run on startup and tests needed)</sub> |

<sub><sup>Standard version:  
Program that when opened will create a decoy file and copy himself to a secure location.
Runs on startup.
Logs keystrokes and sends the log file via email when the computer is shuting down.</sup></sub>

- Updates

Estimated release schedule:
*14/04/2019*

1. MacOS and Linux version released
2. Add screen capture feature.
3. Add more options for sending information.

![*Building*](https://i.gifer.com/3jnq.gif)

## License

- [GNUv3](https://opensource.org/licenses/GPL-3.0)

- Copyright 2019 © Pedro Vieira

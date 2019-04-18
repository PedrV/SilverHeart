# Changelog
All notable changes to this project will be documented in this file.

# v1.1.1 - 2019/04/18

### Added

- Directory where the program is allocated changed.

### Fixed

- Multidisk search optimization.
- File allocation optimization.

<sub><sup><i>Minor code cleanup.</i></sup></sub>

# v1.1.0 - 2019/04/14

### Added

- Detect Ctrl-V actions with text on clipboard and logs them to the file.
- Screenshot function.
  - Screenshot is taked every time "enter" is pressed.
- Option to send logs via FTP.
  
### Fixed

- `logger.py`:
  - Script not cleaning log files after sending them.
  - Computer begins to registry keystrokes very slowly after hundreds of keystrokes.

- `replicator.py`:
  - Sometimes, it crashes after 2 disk search implementation. 
  - It Crashes when executable is present in 2 disks at the same time.
  - Opens decoy file when executable is present in 2 disks at the same time.
  - Script not replicating proprely when started first time.
  - Doesn't proprely clean the executable after replication.
  
 - `executer.py`:
   - Spawns hundreds of processes after being compiled until no memory is left leading to system crash.
   
- Performance enhancement.

### Removed

- MacOS/Linux support and release date on hold.
  - Can't run tests on functionalities, leading to a suspension of the macOS/Linux versions.


# v1.0.1 - 2019/04/06

### Added

- Multi disk search support.
  - Can now search all the files of 2 disks.
  
### Fixed

- Problem when moving SilverHeart for the safe directory when `replicator.py` was active.
  - Now creates a new directory then copies SilverHeart to the new directory.


# v1.0.0 - 2019/04/05

### Added

- Standard* version of the program released for Windows with tests.
- Standard* version of the program released for macOS and Linux without tests.
  - Incomplete version for Linux and macOS, problem with auto launch option.
  
  
___  
<sub><sup>Standard version:  
Program that when opened will create a decoy file and copy himself to a secure location.
Runs on startup.
Logs keystrokes and sends the log file via email when the OS is shuting down.</sup></sub>

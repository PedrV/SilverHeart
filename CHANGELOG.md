# Changelog
All notable changes to this project will be documented in this file.

# v1.1 - 2019/04/14

### Added

- Detect text Ctrl-V actions and logs them to the file.
- Screenshot function.
  - Screenshot is taked every time "enter" is pressed.
- Option to send logs via FTP.
- Performance enhancement.
  
### Fixed

- `logger.py`:
  - Script not cleaning log files after sending them.
  - Computer begins to registry keystrokes very slowly after hundreds of keystrokes.

- `replicator.py`:
  - Sometimes, it crashes after 2 disk search implementation. 
  - It Crashes when executable is present in 2 disks at the same time.
  - Script not replicating proprely when started first time.
  - Opens decoy file when executable is present in 2 disks at the same time.
  - Doesn't proprely clean the executable after replication.
  
 - `executer.py`:
   - Spawns hundreds of processes after being compiled until no memory is left leading to system crash.

### Removed

- MacOS/Linux support and release date on hold.
  - Can't run tests on functionalities, leading to a suspension of the macOS/Linux versions.


# v1.0.1 - 2019/04/06

### Added

- Multi disk search support.
  - Can now search all the files of 2 disks.
  
### Fixed

- Problem when moving *SilverHeart* for the safe directory when `replicator.py` was active.
  - Now creates a new directory then copies *SilverHeart* to the new directory.


# v1.0.0 - 2019/04/05

### Added

- Standard version of the program released for Windows with tests.
- Standard version of the program released for macOS and Linux without tests.
  - Incomplete version for Linux and macOS, problem with auto launch option.

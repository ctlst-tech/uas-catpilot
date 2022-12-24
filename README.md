# UAS-Catpilot
UAS-Catpilot is an open-source project for drone control systems. It contains the [catpilot](git@github.com:ctlst-tech/catpilot.git) library to support various autopilots. It also contains control system modules described with XML-based DSL.

# Requirements
## Hardware requirements
- Host (Ubuntu, Arch, MacOS)
- Autopilot (Cube Orange)
- ST-LINK V2

## Software requirements
- cmake > 3.15
- openocd
- stlink-tools
- catch2
- bison
- flex
- [arm-none-eabi](https://developer.arm.com/downloads/-/gnu-rm)

# Getting started
### 1. Preparing
Connect your autopilot to a STLINK programmer
### 2. Clone repository
```bash
$ git clone --recurse-submodules git@github.com:ctlst-tech/uas-catpilot.git
$ cd uas-catpilot
```
### 3. Config
```bash
$ make config
```
### 4. Build
```bash
$ make cube
```
### 5. Flash
```bash
$ make flash
```

# Additional information
It is recommended to use Ubuntu as the host operating system, and Visual Studio Code as the code editor. For a quick installation you can use the package manager:

Ubuntu
```bash
$ sudo apt-get install cmake openocd stlink-tools catch2 bison flex
```

To build and debug with VS Code you need to set up *.json configuration files in the .vscode directory. You also need to install the following extensions
- CMake
- CMake Tools
- Clang-Format
- Cortex-Debug
- C/C++
- C/C++ Extension Pack
- C/C++ Themes
- XML Format

To build a project with a non-default configuration, you should specify a cmake build target (Release or Debug) and the following definitions:
- BOARD - Supported board type. For example: ```-DBOARD=cube```
- CLI_PORT - Port for communication with autopilot. For example: ```-DCLI_PORT=TELEM2```
- CLI_BAUDRATE - Serial port baudrate for communication. For example: ```-DCLI_BAUDRATE=57600```
- OS_MONITOR - Show system information: threads, cpu load, RAM: ```-DOS_MONITOR=ON```

And then you can build manually:
```bash
$ rm -r -f build
$ mkdir build
$ cd build
$ cmake .. -DCMAKE_BUILD_TYPE=Release -DBOARD=cube -DCLI_PORT=TELEM2 -DCLI_BAUDRATE=57600 -DOS_MONITOR=ON
$ make uas-catpilot.elf
$ cd ..
```

You can also download firmware with st-flash util:
```bash
$ st-flash write build/firmware/uas-catpilot.bin 0x08000000
```

If you use VS Code, you can change the *.json configuration files for auto build:

settings.json
```json
{
    "cmake.setBuildTypeOnMultiConfig": true,
    "cmake.configureSettings": {
        "BOARD": "cube",
        "CLI_PORT": "TELEM2",
        "CLI_BAUDRATE": "57600"
    },
    "cortex-debug.armToolchainPath": "/usr/bin",
    "cortex-debug.openocdPath": "/usr/local/bin/openocd",
    "cortex-debug.gdbPath": "/usr/bin/gdb-multiarch",
}
```

# UAS-Catpilot
UAS-Catpilot is an open-source project for drone control systems. It contains the [catpilot](git@github.com:ctlst-tech/catpilot.git) library for support various autopilots and control system modules described with XML-based DSL.

# Requirements
## Hardware requirement
- Host (Ubuntu, Arch, MacOS)
- Autopilot (Pixhawk 4, Cube Orange)
- ST-LINK V2

## Software requirement
- cmake > 3.15
- openocd
- stlink-tools
- catch2
- bison
- flex
- [arm-none-eabi](https://developer.arm.com/downloads/-/gnu-rm)

It is recommended to use Ubuntu as the host operating system, and Visual Studio Code as the code editor. For a quick installation you can use the package manager:

Ubuntu
```bash
$ sudo apt-get install cmake openocd stlink-tools catch2 bison flex
```

To build and debug with VS Code you need to set up *.json configuration files in the .vscode driectory. You also need to install the following extensions
- CMake
- CMake Tools
- Clang-Format
- Cortex-Debug
- C/C++
- C/C++ Extension Pack
- C/C++ Themes
- XML Format

# Getting started
### 1. Clone repository
```bash
$ git clone --recurse-submodules git@github.com:ctlst-tech/uas-catpilot.git
$ cd catpilot
```

### 2. Build
To build a project, you must specify cmake build target and board type. You also need to generate configuration files:
```bash
$ make quad config
$ make cube
```

### 3. Flash
```bash
$ make flash
```

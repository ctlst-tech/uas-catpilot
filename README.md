# ctlst-fmuv5
## Description

ctslt-fmuv5 is open sourcing project with c-atom library hardware integration

#### Software requirement
1. cmake > 3.15
2. openocd
3. stlink-tools
4. catch2
5. bison
6. flex
7. [arm-none-eabi](https://developer.arm.com/downloads/-/gnu-rm)

#### Hardware requirement
1. Linux (Ubuntu, Arch) / MacOS
2. Pixhawk 4 / Cube Orange
3. ST-LINK V2

## Getting started

---

### 1. Clone repository

```bash
$ git clone ssh://git@git.jetbrains.space/ctlst/flight-embed-open-sourcing/ctlst-fmuv5.git
$ cd ctlst-fmuv5
$ git submodule update --init --recursive
```

---

### 2. Build and flash

To build a project, you must specify cmake build target (Release/Debug) and platform type (PX4/Cube/Linux). Also you need to generate configuration files.

```bash
$ make prebuild
$ make build
$ make flash
```

---

### 3. IDE

You need to specify the build target, platform type, path to the compiler and other parameters that are required for your IDE.

### vscode

To build in vscode you need *.json configuration files. All required files are located in the .vscode project directory.

Mandatory extensions:

- CMake
- CMake Tools
- Cortex-Debug

Recommend extensions:

- C/C++
- C/C++ Extension Pack
- C/C++ Themes
- XML Format
- Output Colorizer

*Note: You may need to change the paths to bin*

### clion

In the settings, you need to specify the build target, platform type, and also select the toolchain.

---

### 3. Debug

**vscode**

To build in vscode you need the **Cortex-Debug** extension and configured **settings.json**, **task.json** and **launch.json**.

**clion**

---

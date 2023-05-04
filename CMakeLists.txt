cmake_minimum_required(VERSION 3.15)

set(PROJ_NAME "uas-catpilot")

if (BOARD STREQUAL "host")
    set(MCU_FAMILY host)
    set(MCU_MODEL host)
    set(OS "posix")
    set(FS "posix")
    set(CLI_PORT "stdio")
    set(CLI_BAUDRATE "")
elseif (BOARD STREQUAL "cube")
    set(MCU_FAMILY stm32)
    set(MCU_MODEL h753)
    set(IC_CUBEIO "ON")
    set(IC_ICM20602 "ON")
    set(IC_ICM20649 "ON")
    set(IC_ICM20948 "ON")
    set(IC_IST8310 "ON")
    set(IC_MS5611 "ON")
    set(IC_SD "ON")
    set(OS "freertos")
    set(FS "fatfs")

    set(ESWB_EQRB_NO_SOCKET "1")
    set(CATOM_NO_SOCKET "1")
    set(FAKE_PTHREAD "1")

    if (NOT DEFINED CLI_PORT)
        set(CLI_PORT "TELEM2")
    endif()
    if (NOT DEFINED CLI_BAUDRATE)
        set(CLI_BAUDRATE "115200")
    endif()
    if (OS_MONITOR STREQUAL "ON")
        add_definitions(-DOS_MONITOR)
    endif()
    if (MAINTENANCE_MODE STREQUAL "ON")
        add_definitions(-DMAINTENANCE_MODE)
    endif()
    add_definitions(-DCLI_PORT="${CLI_PORT}")
    add_definitions(-DCLI_BAUDRATE="${CLI_BAUDRATE}")
elseif (BOARD STREQUAL "ctlst")
    set(MCU_FAMILY zynq)
    set(MCU_MODEL 7020)
    set(OS "qnx")
    set(FS "qnx")
    set(IC_CTLST "ON")

    set(ESWB_EQRB_NO_SOCKET "1")
    set(CATOM_NO_SOCKET "1")
    set(FAKE_PTHREAD "1")
else ()
    message(FATAL_ERROR "Board is not selected!")
endif ()

execute_process (
        COMMAND bash -c "git show --quiet | grep 'commit ' | sed 's/commit //' | awk '{print substr($0,1,8)}' | tr '\n' ' '"
        OUTPUT_VARIABLE GIT_HASH_UAS
)
execute_process (
        COMMAND bash -c "if [ -z \"$(git status -s)\" ]; then echo clean; else echo dirty; fi | tr '\n' ' '"
        OUTPUT_VARIABLE GIT_STATE_UAS
)
execute_process (
        COMMAND bash -c "cd ../catpilot && git show --quiet | grep 'commit ' | sed 's/commit //' | awk '{print substr($0,1,8)}' | tr '\n' ' '"
        OUTPUT_VARIABLE GIT_HASH_CATPILOT
)
execute_process (
        COMMAND bash -c "cd ../catpilot && if [ -z \"$(git status -s)\" ]; then echo clean; else echo dirty; fi | tr '\n' ' '"
        OUTPUT_VARIABLE GIT_STATE_CATPILOT
)

add_definitions(-DGIT_HASH_UAS="${GIT_HASH_UAS}")
add_definitions(-DGIT_STATE_UAS="${GIT_STATE_UAS}")
add_definitions(-DGIT_HASH_CATPILOT="${GIT_HASH_CATPILOT}")
add_definitions(-DGIT_STATE_CATPILOT="${GIT_STATE_CATPILOT}")

set(CMAKE_TOOLCHAIN_FILE catpilot/bsp/mcu/core/${MCU_FAMILY}/${MCU_MODEL}/${MCU_MODEL}_toolchain.cmake)

set(ASM_FILE ${PROJECT_BINARY_DIR}/${PROJ_NAME}.asm)

set(MAP_CREATION "ON")

project(${PROJ_NAME} C ASM)
set(EXECUTABLE_OUTPUT_PATH ${CMAKE_BINARY_DIR}/firmware)

message("\n${PROJECT_NAME}:")
message("   Board: ${BOARD}")
message("   MCU family: ${MCU_FAMILY}")
message("   MCU model: ${MCU_MODEL}")
message("   Toolchain: ${CMAKE_TOOLCHAIN_FILE}")
message("   C Compiler: ${CMAKE_C_COMPILER}")
message("   C++ Compiler: ${CMAKE_CXX_COMPILER}")
message("   Compiler flags: ${COMMON_FLAGS}")
message("   Linker flags: ${LINKER_FLAGS}")
message("   Debug port: ${CLI_PORT} ${CLI_BAUDRATE}")
message("   uas-catpilot: ${GIT_HASH_UAS}${GIT_STATE_UAS}")
message("   catpilot: ${GIT_HASH_CATPILOT}${GIT_STATE_CATPILOT}\n")

add_subdirectory(catpilot)

include_directories(
    ${OS}
    ${BSP}
)

include(atomics.cmake)

add_executable(catom-launcher
    ${ATOMICS_REG}
    # FIXME
    catpilot/c-atom/function/conv.c
    catpilot/c-atom/function/error.c
)

add_executable(${PROJECT_NAME}.elf
    main.c
    # xml_inline.c
    # xml_inline_cfgs.c
    ${ATOMICS_REG}
    # FIXME
    catpilot/c-atom/function/error.c
    catpilot/c-atom/function/conv.c
)

target_link_libraries(catom-launcher PUBLIC 
    # os-static
    # bsp-static
    c-atom-launcher-static 
    ${ATOMICS_LIBS}
    socket
)

target_link_libraries(${PROJECT_NAME}.elf PUBLIC
    os-static
    bsp-static
    c-atom-static
    ${ATOMICS_LIBS}
    -lc -lm -lnosys
)

set(ELF_FILE ${EXECUTABLE_OUTPUT_PATH}/${PROJECT_NAME}.elf)
set(HEX_FILE ${EXECUTABLE_OUTPUT_PATH}/${PROJECT_NAME}.hex)
set(BIN_FILE ${EXECUTABLE_OUTPUT_PATH}/${PROJECT_NAME}.bin)

add_custom_command(TARGET "${PROJECT_NAME}.elf" POST_BUILD
    COMMAND ${CMAKE_OBJCOPY} -Obinary ${ELF_FILE} ${BIN_FILE}
    COMMAND ${CMAKE_OBJCOPY} -Oihex  ${ELF_FILE} ${HEX_FILE}
)

add_custom_command(TARGET "${PROJECT_NAME}.elf" POST_BUILD
    COMMAND ${CMAKE_COMMAND} -E copy ${HEX_FILE} "${EXECUTABLE_OUTPUT_PATH}/${PROJECT_NAME}.hex"
    COMMAND ${CMAKE_COMMAND} -E copy ${BIN_FILE} "${EXECUTABLE_OUTPUT_PATH}/${PROJECT_NAME}.bin"
    COMMAND ${CMAKE_SIZE} -A ${EXECUTABLE_OUTPUT_PATH}/${PROJECT_NAME}.elf
    COMMAND ${CMAKE_SIZE} --format=berkeley ${EXECUTABLE_OUTPUT_PATH}/${PROJECT_NAME}.hex
)


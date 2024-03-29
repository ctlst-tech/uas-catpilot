
atomics_flight:
	@echo Generating atomics functions code
	@./catpilot/c-atom/tools/fspecgen.py --catom_path catpilot/c-atom --code --cmake --registry_c ./atomics_reg.c --atomics_dirs cube:catpilot/atomics/cube ublox:catpilot/atomics/ublox odrive:catpilot/atomics/odrive  catom:catpilot/c-atom/atomics

atomics_ground:
	@./catpilot/c-atom/tools/fspecgen.py --catom_path catpilot/c-atom --code --cmake --registry_c ./atomics_reg.c --atomics_dirs catpilot:catpilot/atomics/ublox catom:catpilot/c-atom/atomics

xmlinline:
	@echo Inlining XML configs
	@./catpilot/c-atom/tools/xml2c_inliner.py --cfg_path config/quad/ --out xml_inline_cfgs.c

bblocks:
	@./catpilot/c-atom/tools/fspecgen.py --catom_path catpilot/c-atom --code --cmake --bbxml bblocks.xml --atomics_dirs catpilot:catpilot/atomics/ catom:catpilot/c-atom/atomics/

clean_build:
	@echo Building
	rm -r -f build
	mkdir build
	cd build && cmake .. -DBOARD=cube -DCMAKE_BUILD_TYPE=Release && make uas-catpilot.elf -j15

cube:
	rm -r -f build && mkdir build && cd build && cmake .. -DBOARD=cube -DCLI_PORT=DBG -DCLI_BAUDRATE=115200 -DOS_MONITOR=ON -DCMAKE_BUILD_TYPE=Release && make uas-catpilot.elf

flash:
	@echo Firmware downloading
	openocd -f interface/stlink.cfg -f ./catpilot/bsp/mcu/core/stm32/h753/stm32h753.cfg -c "init" -c "program ./build/firmware/uas-catpilot.elf verify reset exit"

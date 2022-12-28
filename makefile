
atomics:
	@echo Generating f_specs
	@./catpilot/c-atom/tools/fspecgen.py --catom_path catpilot/c-atom --code --cmake --registry_c ./f_specs_reg.c --f_specs_dirs catpilot:catpilot/f_specs catom:catpilot/c-atom/f_specs

xmlinline:
	@echo Inlining XML configs
	@./catpilot/c-atom/tools/xml2c_inliner.py --cfg_path config/quad/ --out xml_inline_cfgs.c

bblocks:
	@./catpilot/c-atom/tools/fspecgen.py --code --cmake --bbxml bblocks.xml --f_specs_dirs catpilot:catpilot/f_specs/ catom:catpilot/c-atom/f_specs/

clean_build:
	@echo Building
	rm -r -f build
	mkdir build
	cd build && cmake .. -DTYPE=Cube -DCMAKE_BUILD_TYPE=Release && make catpilot.elf -j15

cube:
	rm -r -f build && mkdir build && cd build && cmake .. -DBOARD=cube -DCLI_PORT=DBG -DCLI_BAUDRATE=115200 -DOS_MONITOR=ON && make uas-catpilot.elf

flash:
	@echo Firmware downloading
	openocd -f interface/stlink.cfg -f ./catpilot/bsp/mcu/core/stm32/h753/stm32h753.cfg -c "init" -c "program ./build/firmware/uas-catpilot.elf verify reset exit"

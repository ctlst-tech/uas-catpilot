
codegen:
	@echo Generating f_specs
	@./catpilot/c-atom/tools/fspecgen.py --code --cmake --registry_c ./f_specs_reg.c --f_specs_dirs cube:f_specs catom:catpilot/c-atom/f_specs/

prebuild: codegen
	@echo Inlining XML configs
	@./catpilot/c-atom/tools/xml2c_inliner.py --cfg_path config/cube/ --out xml_inline_cfgs.c

bblocks:
	@./catpilot/c-atom/tools/fspecgen.py --code --cmake --bbxml bblocks.xml --f_specs_dirs cube:f_specs catom:catpilot/c-atom/f_specs/

clean_build:
	@echo Building
	rm -r -f build
	mkdir build
	cd build && cmake .. -DTYPE=Cube -DCMAKE_BUILD_TYPE=Release && make catpilot.elf -j15

flash:
	@echo Firmware downloading
	openocd -f interface/stlink.cfg -f ./bsp/cube/mcu/stm32h753/core/stm32h7.cfg -c "init" -c "program ./build/firmware/catpilot.elf verify reset exit"

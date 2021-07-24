@echo off
mkdir atmosphere\exefs_patches\HigurashiEN > NUL 2> NUL
mkdir atmosphere\contents\0100F6A00A684000\romfs > NUL 2> NUL
@echo on
wsl patch --verbose -i 1diffasm.diff -o scenarionew/listing.temp scenario/listing.asm
python 1ScriptEXEFS.py
python 2ScriptJSON.py
@echo, 
@echo Compiling scenario...
ShinDataUtil\bin\Debug\netcoreapp5.0\shindatautil.exe scenario-layout extracted\newrodin.fnt scenarionew\listing.dat scenarionew\listing.asm
ShinDataUtil\bin\Debug\netcoreapp5.0\shindatautil.exe scenario-build scenarionew patch\main.snr
@echo Packing ROM file...
ShinDataUtil\bin\Debug\netcoreapp5.0\shindatautil.exe rom-build-from-dir atmosphere/contents/0100F6A00A684000/romfs/patch.rmm patch
@echo Finished executing script.
pause
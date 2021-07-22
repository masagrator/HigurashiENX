@echo off
mkdir atmosphere\exefs_patches\HigurashiEN > NUL 2> NUL
mkdir atmosphere\contents\0100F6A00A684000\romfs > NUL 2> NUL
mkdir patch\picture\c > NUL 2> NUL
mkdir patch\picture\e > NUL 2> NUL
mkdir scenarionew > NUL 2> NUL
@echo on
ShinDataUtil\bin\Debug\netcoreapp5.0\shindatautil.exe txa-encode extracted\adv patch\adv.txa
ShinDataUtil\bin\Debug\netcoreapp5.0\shindatautil.exe txa-encode extracted\bgmmode patch\bgmmode.txa
ShinDataUtil\bin\Debug\netcoreapp5.0\shindatautil.exe txa-encode extracted\cgmode patch\cgmode.txa
ShinDataUtil\bin\Debug\netcoreapp5.0\shindatautil.exe txa-encode extracted\chart patch\chart.txa
ShinDataUtil\bin\Debug\netcoreapp5.0\shindatautil.exe txa-encode extracted\charsel patch\charsel.txa
ShinDataUtil\bin\Debug\netcoreapp5.0\shindatautil.exe txa-encode extracted\config patch\config.txa
ShinDataUtil\bin\Debug\netcoreapp5.0\shindatautil.exe txa-encode extracted\kakera patch\kakera.txa
ShinDataUtil\bin\Debug\netcoreapp5.0\shindatautil.exe txa-encode extracted\kakeraget patch\kakeraget.txa
ShinDataUtil\bin\Debug\netcoreapp5.0\shindatautil.exe txa-encode extracted\logview patch\logview.txa
ShinDataUtil\bin\Debug\netcoreapp5.0\shindatautil.exe txa-encode extracted\moviemode patch\moviemode.txa
ShinDataUtil\bin\Debug\netcoreapp5.0\shindatautil.exe txa-encode extracted\msgtex patch\msgtex.txa
ShinDataUtil\bin\Debug\netcoreapp5.0\shindatautil.exe txa-encode extracted\otsuget patch\otsuget.txa
ShinDataUtil\bin\Debug\netcoreapp5.0\shindatautil.exe txa-encode extracted\saveload patch\saveload.txa
ShinDataUtil\bin\Debug\netcoreapp5.0\shindatautil.exe txa-encode extracted\snrsel patch\snrsel.txa
ShinDataUtil\bin\Debug\netcoreapp5.0\shindatautil.exe txa-encode extracted\tipsget patch\tipsget.txa
ShinDataUtil\bin\Debug\netcoreapp5.0\shindatautil.exe txa-encode extracted\tipsmode patch\tipsmode.txa
ShinDataUtil\bin\Debug\netcoreapp5.0\shindatautil.exe txa-encode extracted\title patch\title.txa
for %%G in (images\picture\c\*.png) do ShinDataUtil\bin\Debug\netcoreapp5.0\shindatautil.exe pic-encode %%G %~p0patch\picture\c\%%~nG.pic
for %%G in (images\picture\e\*.png) do ShinDataUtil\bin\Debug\netcoreapp5.0\shindatautil.exe pic-encode %%G %~p0patch\picture\e\%%~nG.pic
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
@echo off
mkdir extracted > NUL 2> NUL
mkdir scenario > NUL 2> NUL
@echo on
ShinDataUtil\bin\Debug\netcoreapp5.0\shindatautil.exe rom-scenario-decompile ROMs\patch.rom main.snr scenario
ShinDataUtil\bin\Debug\netcoreapp5.0\shindatautil.exe rom-txa-extract ROMs\patch.rom cgmode.txa extracted\cgmode
ShinDataUtil\bin\Debug\netcoreapp5.0\shindatautil.exe rom-txa-extract ROMs\patch.rom adv.txa extracted\adv
ShinDataUtil\bin\Debug\netcoreapp5.0\shindatautil.exe rom-txa-extract ROMs\data.rom bgmmode.txa extracted\bgmmode
ShinDataUtil\bin\Debug\netcoreapp5.0\shindatautil.exe rom-txa-extract ROMs\data.rom charsel.txa extracted\charsel
ShinDataUtil\bin\Debug\netcoreapp5.0\shindatautil.exe rom-txa-extract ROMs\data.rom chart.txa extracted\chart
ShinDataUtil\bin\Debug\netcoreapp5.0\shindatautil.exe rom-txa-extract ROMs\data.rom config.txa extracted\config
ShinDataUtil\bin\Debug\netcoreapp5.0\shindatautil.exe rom-txa-extract ROMs\data.rom kakera.txa extracted\kakera
ShinDataUtil\bin\Debug\netcoreapp5.0\shindatautil.exe rom-txa-extract ROMs\data.rom kakeraget.txa extracted\kakeraget
ShinDataUtil\bin\Debug\netcoreapp5.0\shindatautil.exe rom-txa-extract ROMs\data.rom logview.txa extracted\logview
ShinDataUtil\bin\Debug\netcoreapp5.0\shindatautil.exe rom-txa-extract ROMs\data.rom moviemode.txa extracted\moviemode
ShinDataUtil\bin\Debug\netcoreapp5.0\shindatautil.exe rom-txa-extract ROMs\data.rom msgtex.txa extracted\msgtex
ShinDataUtil\bin\Debug\netcoreapp5.0\shindatautil.exe rom-txa-extract ROMs\data.rom otsuget.txa extracted\otsuget
ShinDataUtil\bin\Debug\netcoreapp5.0\shindatautil.exe rom-txa-extract ROMs\data.rom saveload.txa extracted\saveload
ShinDataUtil\bin\Debug\netcoreapp5.0\shindatautil.exe rom-txa-extract ROMs\data.rom snrsel.txa extracted\snrsel
ShinDataUtil\bin\Debug\netcoreapp5.0\shindatautil.exe rom-txa-extract ROMs\data.rom tipsget.txa extracted\tipsget
ShinDataUtil\bin\Debug\netcoreapp5.0\shindatautil.exe rom-txa-extract ROMs\data.rom tipsmode.txa extracted\tipsmode
ShinDataUtil\bin\Debug\netcoreapp5.0\shindatautil.exe rom-txa-extract ROMs\data.rom title.txa extracted\title
ShinDataUtil\bin\Debug\netcoreapp5.0\shindatautil.exe rom-extract-all --regex "newrodin.fnt" ROMs\data.rom extracted
pause

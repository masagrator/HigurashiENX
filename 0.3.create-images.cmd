@echo off
mkdir patch\picture\c > NUL 2> NUL
mkdir patch\picture\t > NUL 2> NUL
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
for %%G in (images\picture\c\*.png) do ShinDataUtil\bin\Debug\netcoreapp5.0\shindatautil.exe pic-encode %%G %~dp0patch\picture\c\%%~nG.pic
for %%H in (images\picture\t\*.png) do ShinDataUtil\bin\Debug\netcoreapp5.0\shindatautil.exe pic-encode %%H %~dp0patch\picture\t\%%~nH.pic
@echo Finished creating images.
pause
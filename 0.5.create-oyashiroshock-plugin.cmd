@echo off
mkdir atmosphere\contents\0100F6A00A684000\exefs > NUL 2> NUL
@echo on
@cd OyashiroShock
bash -c "export DEVKITPRO=/opt/devkitpro; export DEVKITARM=/opt/devkitpro/devkitARM; make"
@cd ..\
@echo off
@copy OyashiroShock\main.npdm atmosphere\contents\0100F6A00A684000\exefs\main.npdm 
@copy OyashiroShock\subsdk9 atmosphere\contents\0100F6A00A684000\exefs\subsdk9
@echo on
@echo Finished executing.
pause
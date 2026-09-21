@echo off
setlocal enabledelayedexpansion

set /p cell="what cell do u want: "
set /p ex="how many ex do you want: "

:: Pad cell number with a leading zero if single digit
set "cell_pad=0%cell%"
set "cell_pad=%cell_pad:~-2%"

set "cell_dir=cell%cell_pad%"

:: Create the main cell directory
if not exist "%cell_dir%" mkdir "%cell_dir%"

:: Loop to create ex directories from 0 to specified number
for /l %%i in (0,1,%ex%) do (
    set "ex_pad=0%%i"
    set "ex_pad=!ex_pad:~-2!"
    mkdir "%cell_dir%\ex!ex_pad!"
)

echo.
echo Directories created successfully!
pause
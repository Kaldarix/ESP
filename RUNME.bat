@echo off
title ESP

:main
echo 1. Run ESP
echo.
set /p mainc="Option: "
if %mainc%==1 call :run
goto main

:run
cls
echo choose a Model.
echo.
echo 1 nano model (lightweight)
echo 2 small model (low load)
echo 3 Medium (Medium load)
echo.
set /p runc="model: "
if %runc%==1 call :nano
if %runc%==3 call :med
if %runc%==2 call :small

goto run

:nano
yolo.py --nano

:med
yolo.py --medium

:small
yolo.py --small
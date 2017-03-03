@echo off
rem setlocal enabledelayedexpansion
rem color 02
rem mode con cols=80 lines=20
rem title = meican robot


IF EXIST "main.py" (
  py\python  main.py
) ELSE (
  py\python  main.pyc
)
@echo off
rm -rf mcm_build
mkdir mcm_build

robocopy cfg mcm_build/cfg /mir 

robocopy src mcm_build/src /mir  
robocopy util mcm_build/util /mir 
xcopy main.py mcm_build 
xcopy README.md mcm_build 
xcopy start.bat mcm_build 
xcopy gen_startup.bat mcm_build

py\python -m compileall -f mcm_build
cd mcm_build && del /s /q *.py,*.cookie
cd ..

robocopy py mcm_build/py /mir

rem 7z a -tzip meican.7z  mcm_build
7z a -t7z meican.7z mcm_build
rmdir /s/q mcm_build
pause
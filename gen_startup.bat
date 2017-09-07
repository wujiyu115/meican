@rem @Author: wujiyu
@rem @Date:   2017-09-07 16:20:30
@rem @Last Modified by:   wujiyu
@rem Modified time: 2017-09-07 16:29:43

@echo off
@echo CD /D  %~dp0 > meican.bat
@echo start.bat >> meican.bat
@echo pause >> meican.bat
copy meican.bat "%AppData%\Microsoft\Windows\Start Menu\Programs\StartUp\"
del meican.bat
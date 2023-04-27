SetLocal ENABLEDELAYEDEXPANSION
for %%a in (*pdf) do (
  set "filename=%%a"
  set "char=!filename:~0,3!"
  
  if /i "!char!" neq "ppt" (
    echo Delete:%%a
    
    del /F %%a 
  )
)
exit

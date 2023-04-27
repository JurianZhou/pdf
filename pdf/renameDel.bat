SetLocal ENABLEDELAYEDEXPANSION
for /f "delims=" %%i in ('dir /s/b *.pdf') do (
    set "foo=%%~nxi"
    set foo=!foo: =!
    set foo=!foo: =!
    ren "%%~fi" "!foo!"
    
)
delete.bat
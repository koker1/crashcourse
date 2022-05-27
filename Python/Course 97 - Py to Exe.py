#(Windows Defender may prevent you from running)
#(make sure pip and pyinstaller are installed/updated)
#(before start you must prepare program file and icon png)
#(you can convert png to ico in icoconvert.com)
#
#1. cd to directory that contains your .py file
#
#2. pyinstaller -F -w -i icon.ico clock.py
#
#-F (all in 1 file)
#-w (removes terminal window)
#-i icon.ico (adds custom icon to .exe)
#clock.py (name of your main .py file)
#
#3. exe is located in the dist folder
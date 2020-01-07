import os

mainOutput = os.popen("gtf 2160 1080 60").read().strip().split('Modeline')[1]
os.system("adb devices && sleep 1")
os.system("adb reverse tcp:5900 tcp:5900 && clear && sleep 2")
os.system(f"xrandr --newmode{mainOutput} && sleep 2")
os.system("xrandr --addmode HDMI-1 2160x1080_60.00 && clear && sleep 2") 
os.system("xrandr --output HDMI-1   --mode 2160x1080_60.00 --left-of LVDS-1 && clear && sleep 2") 
os.system("x11vnc -clip 2160x1080+0+0")

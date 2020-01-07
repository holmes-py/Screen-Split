import os

mainOutput = os.popen("gtf 2160 1080 60").read().strip().split('Modeline')[1]
os.system(f"""adb devices && sleep 1 && adb reverse tcp:5900 tcp:5900 && clear && sleep 2 &&
xrandr --newmode{mainOutput} && clear && sleep 2 && 
xrandr --addmode HDMI-1 2160x1080_60.00 && clear && sleep 2 && 
xrandr --output HDMI-1   --mode 2160x1080_60.00 --left-of LVDS-1 && clear && sleep 2 && 
x11vnc -clip 2160x1080+0+0""")

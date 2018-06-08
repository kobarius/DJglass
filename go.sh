#/bin/sh -f

DIR='/home/pi/work/DJglass/'
sudo pigpiod
cd ${DIR}
python3 dj_glass.py



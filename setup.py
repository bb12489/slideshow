import subprocess
from subprocess import STDOUT, check_call
import os
WorkingDir = os.getcwd()
check_call(['sudo', 'apt-get', 'update', '-y'])
#check_call(['sudo', 'apt-get', 'upgrade', '-y'])
check_call(['sudo', 'apt-get', 'install', 'samba', 'samba-common-bin', '-y'])
check_call(['sudo', 'apt-get', 'install', 'usbmount', '-y'])
subprocess.call("(sudo cp /home/pi/temp/bin/smb.conf /etc/samba/smb.conf)", shell=True)
subprocess.call("(sudo apt-get install python3-dev python3-setuptools libjpeg-dev zlib1g-dev libpng12-dev libfreetype6-dev)", shell=True)
subprocess.call("(sudo apt-get install python3-pip)", shell=True)
subprocess.call("(sudo pip-3.2 install pi3d)", shell=True)
subprocess.call("(sudo pip-3.2 install Pillow)", shell=True)
subprocess.call("(sudo pip install pi3d)", shell=True)
subprocess.call("(sudo cp /home/pi/temp/app/shaders/*.*  /usr/local/lib/python2.7/dist-packages/pi3d/shaders)", shell=True)
subprocess.call("(sudo pip install pyinotify)", shell=True)
subprocess.call("(sudo mv /home/pi/temp/Advertising /home/pi/Advertising)", shell=True)
subprocess.call("(sudo mv /home/pi/temp/slideshow /home/pi/slideshow)", shell=True)
subprocess.call("(sudo mv /home/pi/temp/app /home/pi/app)", shell=True)
subprocess.call("(sudo mv /home/pi/temp/bin/rc.local /etc/rc.local)", shell=True)
subprocess.call("(sudo /etc/init.d/samba restart)", shell=True)
subprocess.call("(sudo reboot)", shell=True)

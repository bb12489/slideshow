Preparation:<br />
Start with clean, fresh and updated Raspbian SD Image<br />
https://www.raspberrypi.org/downloads/raspbian/<br />
<br />
In Desktop Environment:<br />
<br />
Connect to Wlan in upper right corner<br /> 
Startx: Menu ->Preferences -> Raspberry Pi Configuration -> System -> Boot: To CLI<br />
Startx: Menu ->Preferences -> Raspberry Pi Configuration -> System -> Network at boot: Wait for network checked<br />
Startx: Menu ->Preferences -> Raspberry Pi Configuration -> Performance -> GPU Memory: 128<br />
Then reboot<br />
<br />
<strong>Disconnect any USB-Drives bevor executing the setup command</strong><br />
Type commands to CLI:<br />
<br />
`sudo git clone https://github.com/Hatschi915/Slideshow.git /home/pi/temp`<br />
<br />
`cd temp`<br />
<br />
`sudo python setup.py`<br />
<br />
Wait for reboot then connect USB-Stick<br />
<br />
<strong>Featuers:</strong><br />
Preconfigured samba share, to access all needed folders and settings<br />
New pictures shown first, then randomly<br />
Display advertisment after x pictures<br />
Slideshow runs of USB Stick for easy deleting of files and to keep things tidy<br />
Local webserver to change settings of the slideshow. Connect to the Wlan, which the pi is connected to <br /> 
and type `http://raspberry` to access the settings page<br />
<br />
<strong>Useful knowledge:</strong><br />
<br />
To update remove /home/pi/temp from this installation and start over.<br />
<br />
To prevent autostart add a reset.txt file to the USB-Stick and boot.<br />
To quit running slideshow simply type to your Raspberry:<br />
<br />
`sudo killall python`<br />
<br />
Samba share structure:<br />
Advertising: Folder for Ads<br />
Application: The scripts and setting.ini file<br />
Slideshow_Hotfolder: Here you put new files in<br />
Slideshow_Content: The content of the slideshow (USB-Stick)<br />
<br />
Behaviour:<br />
The Slideshow works with an attached USB stick<br />
Any new .jpg/JPG/jpeg/JPEG file putted into the slideshow hotfolder will be displayed first and<br />
then moved to the USB Stick. If there is no file on the USB Stick the slideshow will display the ads<br />
If there is content on the USB Stick the slideshow will show it´s content in random order and after x pictures a ad.<br />
If there is no USB Stick attached new pictures will be displayed but deleted after.<br />
The USB Stick can be disconnected and reconnected while the slideshow is running<br />
<br />
PLEASE READ LICENSING AND COPYRIGHT NOTICES ESPECIALLY IF USING FOR COMMERCIAL PURPOSES<br />


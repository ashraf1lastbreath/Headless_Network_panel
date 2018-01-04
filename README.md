# Headless_Network_panel
A Python program to access Network panel on google chrome developer tools with Selenium, and to fetch the domain names of all elements present on the webpage

* Reads the domain name requirements from a JSON file
* Opens the website in CHrome headless tab, accesses teh Network Tab, and reads all the element URLs
* Sets up a Redis cache from config file
* Sends the domain name along with all its network element urls to Redis cache


## IMPORTANT NOTE :
### Make sure you clone this repo as it is on the root path of your UNIX machine
### Caution: Headless mode is available on Mac and Linux in Chrome 59 and above.
Windows support in Chrome 60. To check what version of Chrome you have, open chrome://version or on terminal, type : 'google-chrome --version'


## SYSTEM REQUIREMENTS :
512 MB Memory / 20 GB Disk / Ubuntu 16.04.3 x64
Python2.7
Chrome > 59 for Linux, MAC,  Chrome > 60 for Windows
latest ChromeDriver
selenium > 3.0.0
pyvirtualdisplay > 0.2.1


## USAGE :
1. cd /root/
2. git clone https://github.com/ashraf1lastbreath/Headless_Network_panel
3. ./install.sh
4. python network_headless.py



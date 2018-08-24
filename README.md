# Automatic-picture-download-from-social-site
Automatic picture download from social site
sudo apt-get install pyautogui
open browser on needed url, then mkdir test_pix
then run ./7.py in test_pix, place mouse pointer anywhere on picture
and jpg files will be downloaded for 2-3 weeks
Main idea here is mouse click on browser picture will refresh for new picture,
then bash command find -mtime or ls -rt|tail will find for example 10 recent
files in browser cache, extract text from them by binary editor, then script
will construct needed url for picture download  by wget. Last is most tricky
since there is no direct mention on jpg files which we need. You can see the way
it is done in scipt, kind of web crawler.

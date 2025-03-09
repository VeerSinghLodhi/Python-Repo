#https://github.com/VeerSinghLodhi
#https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExeHJsMm1seXhldjM4NDN5MXNlYWxtc3luazV1d2JndjRzdmo4czZjOSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/QBd2kLB5qDmysEXre9/giphy.gif

import segno
from urllib.request import urlopen
code =segno.make_qr('https://github.com/VeerSinghLodhi')
url=urlopen('https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExcWY5Y2xtamh2ZXlreXl0cXg0b2MzMWR0aW15Ynl3cWMxZmE2NWl6cyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/l0FF56cexcW2JAXCJj/giphy.gif')
code.to_artistic(background=url,target='C:\\Users\\Veersingh Lodhi\\Documents\\Qr_Code_Session\\hey.gif',scale=10,light='lightblue')
print("Saved")

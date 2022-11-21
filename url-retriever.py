from bs4 import BeautifulSoup
import urllib.request, urllib.parse, urllib.error
import ssl
import re

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
url = "http://py4e-data.dr-chuck.net/known_by_Hassanali.html"

# repeats it 7 times
for i in range(7):
    # retrieves the url
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    # counts the anchors
    count = 0
    for tag in tags:
        count = count +1
   
        # stops at position 3
        if count>18:
            break
        url = tag.get('href', None)

print(url)

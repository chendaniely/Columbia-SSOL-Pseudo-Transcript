'''
Created on May 21, 2013

@author: dyc2112

notes to attempt to connect to ssol website
'''
import cookielib
import urllib
import urllib2
import getpass
from Tkinter import *

userUsername = raw_input("Username: ")
userPassword = getpass.getpass()

# Store the cookies and create an opener that will hold them
cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))

# Add our headers
opener.addheaders = [('User-agent', 'RedditTesting')]

# Install our opener (note that this changes the global opener to the one
# we just made, but you can also just call opener.open() if you want)
urllib2.install_opener(opener)

# The action/ target from the form
authentication_url = 'https://ssol.columbia.edu/'
#https://ssol.columbia.edu/
#https://ssl.reddit.com/post/login

# Input parameters we are going to send
payload = {
  'op': 'login-main',
  'user': userUsername,
  'passwd': userPassword
  }

# Use urllib to encode the payload
data = urllib.urlencode(payload)

# Build our Request object (supplying 'data' makes it a POST)
req = urllib2.Request(authentication_url, data)

# Make the request and read the response
resp = urllib2.urlopen(req)
contents = resp.read()


print "resp: ", resp
print '---------'
print "contents: ", contents
print '=========='
print 'done'

'''
master = Tk()
a = StringVar()
b = StringVar()

Label(master, textvariable=a).pack()
Label(master, textvariable=b).pack()

a.set(resp)
b.set(contents)

master.mainloop()
'''
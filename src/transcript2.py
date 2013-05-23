'''
Created on May 21, 2013

@author: dyc2112

notes to attempt to connect to ssol website using httplib library
'''
import httplib

h1 = httplib.HTTPConnection('ssol.columbia.edu/')
h2 = httplib.HTTPSConnection('')
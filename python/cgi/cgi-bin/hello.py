#!/usr/bin/python3

import cgitb
import cgi 
import os

cgitb.enable()


def doget():
    print("""
    <html>
        <body>
            <form method='POST'>
                <input type="text" name="user" value=""/>
                <input type="submit" value="submit"/>
            </form>
        <body>
    </html>
    """ )


def dopost():
    form = cgi.FieldStorage()
    user = form.getvalue('user')
    if user is None:
        print("Please enter username !")
        doget()
    else:
        print("hello : %s" % user)







print("Content-type:text/html\r\n\r\n")

if os.environ['REQUEST_METHOD'] == 'GET':
    doget()
else:
    dopost()





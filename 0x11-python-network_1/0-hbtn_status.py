#!/usr/bin/python3
"""Python script that fetches https://alx-intranet.hbtn.io/status"""
import urllib.request


if __name__ == '__main__':
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as req:
        bd = req.read()
        print("Body response:")
        print("\t- type: {}".format(type(bd)))
        print("\t- content: {}".format(bd))
        print("\t- utf8 content: {}".format(bd.decode('utf-8')))

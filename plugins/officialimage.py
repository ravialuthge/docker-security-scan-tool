###conf dockerfile#

import os
import docker

class officialimage(object):
    """Check Docker Official Image"""
    def __init__(test):
       from tmp.filepath import FILEPATH
       test.p = FILEPATH
       test.a_h=[]
     
    def officialimagescan(test):
         try:
            f = open(test.p, "r")
            mystring  = f.read()

            for item in mystring.split("\n"):
               if "FROM" in item:
                  d =  item.strip()
                  _s = d.split()
                  img = _s[1]
                  s = img.split(':')
                  o = s[0]
                  client = docker.from_env()
                  images_off = client.images.search(o)
                  __images_off = str(images_off)
                  a__images_off_ch =  __images_off.split(",")
                  wo = " 'is_official':"
                  for im in a__images_off_ch:
                     if wo in im:
                        test.a_h.append(im)
                  __h = test.a_h[0]
                  _h = __h.split(":")
                  _install_version  = _h[1]
                  bbc =  _install_version.replace(" ",'')
               
          
                  if bbc == 'True':
                     print (o +" is Docker Official Image")
                     
                  else:
                     print (o +" not Docker Official Images")
         except FileNotFoundError:
            print ("I did not find the Dockerfile at, "+str(test.p))
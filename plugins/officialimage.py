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
                  #install_version = bbc.replace("'",'')
                  #print (_install_version)
                  #print (bbc)
                  #cmd = "docker search --format '{{.IsOfficial}}' --filter is-official=true " + o
                  #cmdout = os.popen(cmd).read()
                  #cmdout_a = cmdout.rstrip()
          
                  if bbc == 'True':
                     out = o +" is Docker Official Image"
                  
                  else:
                     out = o +" not Docker Official Images"
                  return out
         except FileNotFoundError:
            out = "I did not find the Dockerfile at, "+str(test.p)
            return out
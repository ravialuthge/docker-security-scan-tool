###conf dockerfile#

#import os
import tmp.imagename
from sdk.images_list import *

class officialimage(imageslist):
    """Check Docker Official Image"""
    def __init__(test):
       from tmp.filepath import FILEPATH 
       test.p = FILEPATH
       test.a_h=[]
     
    def officialimagescan(test):
            _images = test.a__images_off_ch
         #try:
            f = open(test.p, "r")
            mystring  = f.read()

            for item in mystring.split("\n"):
               if "FROM" in item:
                  d =  item.strip()
                  _s = d.split()
                  img = _s[1]
                  s = img.split(':')
                  o = s[0]
                  tmp.imagename.IMAGENAME = o
                  #cmd = "docker search --format '{{.IsOfficial}}' --filter is-official=true " + o
                  #cmdout = os.popen(cmd).read()
                  #cmdout_a = cmdout.rstrip()
           
            wo = " 'is_official':"
            for im in _images:
               if wo in im:
                  test.a_h.append(im)
            __off_image_name = test.a_h[0]
            _off_image_name = __off_image_name.split(":")
            off_image_name  = _off_image_name[1]
            bbc =  off_image_name.replace(" ",'')
            #install_version = bbc.replace("'",'')
            #print (_install_version)
            
            if bbc == 'True':
               print (o +" is Docker Official Image")
            else:
               print (o +" not Docker Official Images")
         #except FileNotFoundError:
         #   print ("I did not find the Dockerfile at, "+str(test.p))

###conf dockerfile#

#import os
#import tmp.imagename
from sdk.images_list import *

class officialimage(imageslist):
    """Check Docker Official Image"""
    def __init__(test):
       from tmp.filepath import FILEPATH
       from tmp.imagename import IMAGENAME
       test.p = FILEPATH
       test._o = IMAGENAME
     
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
                  
                  test._o = o
                  #cmd = "docker search --format '{{.IsOfficial}}' --filter is-official=true " + o
                  #cmdout = os.popen(cmd).read()
                  #cmdout_a = cmdout.rstrip()
                  cmdout_a = test.__images_off_ch
                  if cmdout_a == 'True':
                     print (o +" is Docker Official Image")
                  else:
                     print (o +" not Docker Official Images")
         except FileNotFoundError:
            print ("I did not find the Dockerfile at, "+str(test.p))

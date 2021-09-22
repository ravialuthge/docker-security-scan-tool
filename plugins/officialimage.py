import os

class officialimage(object):
    """Check Docker Official Image"""
    def __init__(test):
      test.p = input("Enter File Path:")

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
                  
                  cmd = "docker search --format '{{.IsOfficial}}' --filter is-official=true " + o
                  cmdout = os.popen(cmd).read()
                  cmdout_a = cmdout.rstrip()
                  print (cmdout_a)
                  if cmdout_a == '[OK]':
                     print (o +" is Docker Official Image")
                  #else:
                   #  print (o +" not Docker Official Images")
         except FileNotFoundError:
            print ("I did not find the Dockerfile at, "+str(test.p))

import os
import argparse

class officialimage(object):
    """Check Docker Official Image"""
    def __init__(test):
      parser = argparse.ArgumentParser()
      parser.add_argument("path")
      test.args = parser.parse_args()
      test.p = test.args.path

    def officialimagescan(test):
       try:
         f = open(test.p, "r")
         mystring  = f.read()

         for item in mystring.split("\n"):
            if "FROM" in item:
               d =  item.strip()
               s = d.split()
               o = s[1]
               cmd = "docker search --format '{{.IsOfficial}}' --filter is-official=true " + o
               cmdout = os.popen(cmd).read()
               cmdout_a = cmdout.rstrip()
               if cmdout_a == '[OK]':
                  print (o +" is Docker Official Image")
               else:
                  print (o +" not Docker Official Images")
       except FileNotFoundError:
          print ("I did not find the Dockerfile at, "+str(test.p))

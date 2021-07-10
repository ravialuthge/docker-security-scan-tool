import os

class officialimage:
    """Check Docker Official Image"""
    def scan(test):
       try:
         p = input("enter Dockerfile path :")
         f = open(p, "r")
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
                  print (o + "is Docker Official Image")
               else:
                  print (o + "not Docker Official Images")
       except:
          assert os.path.exists(p), "I did not find the file at, "+str(p)

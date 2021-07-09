p=(input("enter Dockerfile path :"))

f = open(p, "r")
mystring  = f.read()

for item in mystring.split("\n"):
   if "FROM" in item:
      print (item.strip())


docker search --format "{{.IsOfficial}}" --filter is-official=true redis
###conf dockerfile#

from other_modules.print import Print

class officialimage(Print):
    """Check Docker Official Image"""
    
     
    def officialimagescan(test):
       from tmp.filepath import FILEPATH
       dockerfile_path = FILEPATH
       officialimag = Print.host_officialimagescan_print(dockerfile_path)
       return officialimag
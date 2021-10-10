###conf dockerfile#

import os
import re
import docker
from other_modules.print import Print

from sdk.images import ImagesList

class officialimage(Print):
    """Check Docker Official Image"""
    
     
    def officialimagescan(test):
       from tmp.filepath import FILEPATH
       dockerfile_path = FILEPATH
       officialimag = Print.host_officialimagescan_print(dockerfile_path)
       return officialimag
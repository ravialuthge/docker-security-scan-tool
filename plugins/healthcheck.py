###Profile containers#
###CIS_Version 1.0.0:1.12.0#

from other_modules.print import Print

class healthcheck(Print):
    """Check container health at runtime"""
    
    def healthcheck_scan(test):
        
        _table_he_output = Print.container_healthcheck_print()
        return _table_he_output
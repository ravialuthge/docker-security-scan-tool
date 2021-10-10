from termcolor import colored

class Serverity(object):
    def wan():
        wan_output = colored('WARN  ', 'red')
        return wan_output
    
    def pas():
        pas_output = colored('PASS  ', 'green')
        return pas_output
    
    def info():
        info_output = colored('INFO   ', 'blue')
        return info_output

from termcolor import colored

class Serverity(object):
    def wan():
        wan_output = colored('WARN  ', 'red')
        return wan_output
    
    def pas():
        pas_output = colored('PASS  ', 'green')
        return pas_output

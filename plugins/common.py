from termcolor import colored

class banner:
    def scan(test):
        print(colored('custom test cases',attrs=['bold']))

class outputpl:
    
    def __init__(test, plugins):
        test.banner_out = [banner()]
        test.test_plugins = plugins

    def run(test):
        modules_run = test.banner_out + test.test_plugins
        for module in modules_run:
            module.scan()
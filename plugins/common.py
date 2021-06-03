from termcolor import colored

class banner:
    def scan(test):
        print(colored('custom test cases',attrs=['bold']))

class outputpl:
    
    def __init__(test, *, plugins: list=list()):
        test.test_modules = [banner()]
        test.test_plugins = plugins

    def run(test):
        modules_to_execute = test.test_modules + test.test_plugins
        for module in modules_to_execute:
            module.scan()
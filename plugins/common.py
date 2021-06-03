class banner:
    def scan(test):
        print("custom test cases")

class outputpl:
    
    def __init__(test, *, plugins: list=list()):
        test.test_modules = [banner()]
        test.test_plugins = plugins

        modules_to_execute = test.test_modules + test.test_plugins
        for module in modules_to_execute:
            module.scan()
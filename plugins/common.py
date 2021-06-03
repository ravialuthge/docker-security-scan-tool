class InternalPrinter:
    def scan(test):
        print("Internal Hello")

class MyApplication:
    
    def __init__(test, *, plugins: list=list()):
        test.internal_modules = [InternalPrinter()]
        test._plugins = plugins

    def run(test):
        print("Starting program")
        print("-" * 79)

        modules_to_execute = test.internal_modules + test._plugins
        for module in modules_to_execute:
            module.scan()

        print("-" * 79)
        print("Program done")
        print()
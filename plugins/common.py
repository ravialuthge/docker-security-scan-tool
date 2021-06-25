class outputpl:
    
    def __init__(test, *, plugins: list=list(), *args, **kwargs):
        test.test_plugins = plugins

    def run(test):
        modules_run = test.test_plugins
        for module in modules_run:
            module.scan()
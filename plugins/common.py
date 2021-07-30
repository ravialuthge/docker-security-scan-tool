class outputpl:
    
    def __init__(self, *, plugins: list=list()):
        self.test_plugins = plugins

    def run(self):
        modules_run = self.test_plugins
        for module in modules_run:
            module.scan()
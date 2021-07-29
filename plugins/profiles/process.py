class cis_version:
    
    def __init__(version, *, version_plugins: list=list()):
        version.version_test_plugins = version_plugins

    def version_run(version):
        version_modules_run = version.version_test_plugins
        for version_module in version_modules_run:
            version_module.version_scan()
from .restricted_python_driver import RestrictedPythonDriver


class Sandbox:
    def __init__(self, source_code,
                 driver_class=RestrictedPythonDriver):
        self.source_code = source_code
        self.print_logs = None
        self.driver = driver_class()


    def execute(self):
        try:
            self.driver.setup()
            print_logs = self.driver.execute(self.source_code)
            self.print_logs = print_logs
        finally:
            self.driver.teardown()

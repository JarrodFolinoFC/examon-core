from .unrestricted_driver import UnrestrictedDriver


class Sandbox:
    def __init__(self, source_code,
                 driver_class=UnrestrictedDriver):
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

    @staticmethod
    def run_function(source_code, driver=UnrestrictedDriver):
        ces = Sandbox(source_code, driver)
        ces.execute()

        return ces.print_logs

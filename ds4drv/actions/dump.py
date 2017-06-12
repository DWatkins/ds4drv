from ..action import ReportAction

ReportAction.add_option("--dump-reports", action="store_true",
                        help="Prints controller input reports")

host = '127.0.0.1'
port = 5555;

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

class ReportActionDump(ReportAction):
    """Pretty prints the reports to the log."""

    def __init__(self, *args, **kwargs):
        super(ReportActionDump, self).__init__(*args, **kwargs)
        self.timer = self.create_timer(0.5, self.dump)

    def enable(self):
        self.timer.start()

    def disable(self):
        self.timer.stop()

    def load_options(self, options):
        if options.dump_reports:
            self.enable()
        else:
            self.disable()

    def dump(self, report):
        dump = "Report dump\n"
        for key in report.__slots__:
            value = getattr(report, key)
            dump += "{0},".format(value)

        s.sendto(dump,(host,port))

        return True

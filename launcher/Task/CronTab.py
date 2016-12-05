# @file
# @version 0.4
# @copyright 2016 Desmodul
# @author Markus Riegert <desmodul@drow-land.de>

# ____________________________________________________________________________
# Starts the Application DroneDevice (IFS) which takes control over the drone.

from LoggerFactory import LogHandler


class CronTab(object):

    def __init__(self, _cronTabSection):
        self.logger = logger = LogHandler.getLogger(__name__)
        self.section = _cronTabSection
        for option in self.section.options():
            self.addCrontabEntry(option)

    def addCrontabEntry(self, _cronTabOption):
        # process section
        return True

    def removeCrontabEntry(self, _cronTabOption):
        # process section
        return True

    def setupMicroCrontab(self, _cronTabSection):
        # process section
        return True

def create(_cronTabSection):
    return CronTab(_cronTabSection)

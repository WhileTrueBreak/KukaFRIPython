from jadeClient.clientJVM import startJVM
startJVM()

from jadevep.client import LBRClientCallback
from jpype import JImplements, JOverride

@JImplements(LBRClientCallback)
class LBRJadeClientCallback:

    def __init__(self):
        self.onStateChange = None
        self.onMonitor = None
        self.onWaitForCommand = None
        self.onCommand = None

    @JOverride
    def onStateChange(self, client, oldState, newState):
        print("State changed from %s to %s" % (oldState, newState))
        if self.onStateChange:
            self.onStateChange(client, oldState, newState)

    @JOverride
    def monitor(self, client):
        if self.onMonitor:
            self.onMonitor(client)

    @JOverride
    def waitForCommand(self, client):
        if self.onWaitForCommand:
            self.onWaitForCommand(client)

    @JOverride
    def command(self, client):
        if self.onCommand:
            self.onCommand(client)

    def setOnStateChange(self, callback):
        self.onStateChange = callback
    
    def setOnMonitor(self, callback):
        self.onMonitor = callback
    
    def setOnWaitForCommand(self, callback):
        self.onWaitForCommand = callback
    
    def setOnCommand(self, callback):
        self.onCommand = callback
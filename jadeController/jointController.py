class JointController:

    def __init__(self):
        self.targetJointValues = None

    def onStateChange(self, client, oldState, newState):
        client.superOnStateChange(oldState, newState)

    def monitor(self, client):
        client.superMonitor()
        self.update(client)

    def waitForCommand(self, client):
        client.superWaitForCommand()
        self.update(client)

    def command(self, client):
        client.superCommand()
        self.update(client)
    
    def update(self, client):
        pass
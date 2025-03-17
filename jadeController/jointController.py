class JointController:

    def onStateChange(client, oldState, newState):
        client.superOnStateChange(oldState, newState)

    def monitor(client):
        client.superMonitor()

    def waitForCommand(client):
        client.superWaitForCommand()

    def command(client):
        client.superCommand()
    
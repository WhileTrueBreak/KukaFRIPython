class JadeController:

    def onStateChange(client, oldState, newState):
        client.superOnStateChange(oldState, newState)

    def monitor(client):
        client.superMonitor()

    def setOnWaitForCommand(client):
        client.superWaitForCommand()

    def setOnCommand(client):
        client.superCommand()
    
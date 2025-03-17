from jadeClient.clientJVM import stopJVM
from jadeClient.lbrJadeClientThread import LBRJadeClientThread
from jadeClient.lbrJadeClientCallback import LBRJadeClientCallback
from jadeController.jointController import JointController
from jadeController.utils.optimiseIK import optimiseFromXYZ
import signal

def signal_handler(sig, frame):
    print('You pressed Ctrl+C!')
    clientThread.stop()
    stopJVM()


signal.signal(signal.SIGINT, signal_handler)

hostname = "172.24.201.1"
port = 30200

clientThread = LBRJadeClientThread(hostname, port)
clientCallback = LBRJadeClientCallback()
clientThread.addClientCallback(clientCallback)
controller = JointController()
clientCallback.setOnStateChange(controller.onStateChange)
clientCallback.setOnMonitor(controller.monitor)
clientCallback.setOnWaitForCommand(controller.waitForCommand)
clientCallback.setOnCommand(controller.command)
clientThread.start()

controller.setTargetJointValues(optimiseFromXYZ(0.5, 0.5, 0.5))

while True:
    if input("Press q to quit: ") == "q":
        break

clientThread.stop()
clientThread.join()
stopJVM()

from jadeClient.clientJVM import startJVM
startJVM()

import threading

from com.kuka.connectivity.fastRobotInterface.clientSDK.connection import UdpConnection
from com.kuka.connectivity.fastRobotInterface.clientSDK.base import ClientApplication
from jadevep.client import LBRClientWrapper
import jpype

class LBRJadeClientThread(threading.Thread):
    def __init__(self, hostname, port):
        threading.Thread.__init__(self)
        self.isRunning = False

        self.hostname = hostname
        self.port = port

        self.client = LBRClientWrapper()
        self.connection = UdpConnection()
        self.app = ClientApplication(self.connection, self.client)
        self.app.connect(self.port, self.hostname)

    def run(self):
        print("Starting client thread...")
        self.isRunning = True
        while self.isRunning:
            self.step()
        self.stop()
        print("Stopped client thread.")
    
    def step(self):
        try:
            print("Stepping...")
            success = self.app.step()
            if not success:
                self.isRunning = False
        except Exception as e:
            print(f"Error in step(): {e}")
            self.isRunning = False

    def stop(self):
        if not self.isRunning: return
        print("Stopping client thread...")
        self.app.disconnect()
        self.isRunning = False

    def addClientCallback(self, callback):
        self.client.setCallback(callback)

    


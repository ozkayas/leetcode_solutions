from call import Call
from callhandler import CallHandler

from abc import ABC, abstractmethod

class Employee(ABC):

    def __init__(self, callhandler: CallHandler):
        self.callhandler = callhandler
        self.currentCall :Call = None

    # /* Start the conversation */
    def receiveCall(self, call: Call):
        self.currentCall = call
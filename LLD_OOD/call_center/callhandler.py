from typing import List, Optional
from employee import Employee
from respondant import Respondant
from manager import Manager
from director import Director
from call import Call
from caller import Caller

class CallHandler:

    def __init__(self) -> None:
        self.LEVELS = 3
        self.NUM_RESPONDENTS = 10
        self.NUM_MANAGERS = 4
        self.NUM_DIRECTORS = 2
        
        self.employeeLevel:List[List[Employee]] = [[] * 3]
        self.callQueues:List[List[Call]] = [[] * 3]

        self.respondants = [Respondant(self) for _ in range(self.NUM_RESPONDENTS)]
        self.managers = [Manager(self) for _ in range(self.NUM_MANAGERS)]
        self.directors = [Director(self) for _ in range(self.NUM_DIRECTORS)]

        self.employeeLevel[0].extend(self.respondants)
        self.employeeLevel[1].extend(self.managers)
        self.employeeLevel[2].extend(self.directors)
        
    #/* Gets the first available employee who can handle this call. */
    def getHandlerForCall(self, call:Call) -> Optional[Employee]:
        callLevel = call.getRank.value
        while callLevel < self.LEVELS:
            for emp in self.employeeLevel[callLevel]:
                if emp.isFree():
                    return emp
                
            callLevel += 1

        return None
    
    # /* Routes the call to an available employee, or saves in a queue if no employee available. */
    def dispatchCaller(self, caller: Caller):
        call = Call(caller)
        self.dispatchCall(call)

    def dispatchCall(self, call:Call):
        emp = self.getHandlerForCall(call)

        if emp:
            emp.receiveCall(call)
            call.setHandler(emp)
        else:
            call.reply("Please wait for free employee to reply")
            self.callQueues[call.getRank().value].append(call)

    # /* An employee got free. Look for a waiting call that he/she can serve. Return true
    # * if we were able to assign a call, false otherwise. */  
    def assignCall(self, emp:Employee) -> bool:
        # /* Check the queues, starting from the highest rank this employee can serve. */
        rank = emp.getRank().value

        for r in range(rank, -1, -1):
            que = self.callQueues[r]

            if len(que) > 0:
                call = que.pop(0)
                if call:
                    emp.receiveCall(call)
                    return True
                
        return False
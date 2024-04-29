
from rank import Rank
from caller import Caller
from employee import Employee

class Call:
    
    def __init__(self, c: Caller) -> None:
        self.caller = c
        self.rank = Rank.Responser

    def setHandler(self, e: Employee):
        self.hanler = e

    def reply(self, message:str):
        print(message)

    def getRank(self) -> Rank:
        return self.rank
    
    def setRank(self, rank: Rank):
        self.rank = rank

    def incrementRank(self) -> Rank:
        if self.rank == Rank.Responder:
            self.rank = Rank.Manager
        elif self.rank == Rank.Manager:
            self.rank = Rank.Director
        
        return self.rank
    
    def disconnect(self):
        self.reply("Thank you calling")
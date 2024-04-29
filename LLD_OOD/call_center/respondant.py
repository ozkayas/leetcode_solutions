
from employee import Employee
from callhandler import CallHandler
from rank import Rank

class Respondant (Employee):

    def __init__(self, callhandler:CallHandler):
        super().__init__(callhandler)
        self.rank = Rank.Respondant
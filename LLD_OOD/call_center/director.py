
from employee import Employee
from callhandler import CallHandler
from rank import Rank

class Director (Employee):

    def __init__(self, callhandler:CallHandler):
        super().__init__(callhandler)
        self.rank = Rank.Director
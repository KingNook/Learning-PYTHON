class Person:
    def __init__(self, fname, lname, job=None):
        self.forename = fname
        self.surname = lname
        self.job = job

    def __repr__(self):
        return f'{self.__class__.__name__}({self.forename}, {self.surname})'

    @property
    def fullname(self):
        return f'{self.forename} {self.surname}'

    @fullname.setter
    def fullname(self, name):
        self.forename, self.surname = name.split(' ')



class Employee(Person):
    def __init__(self, fname, lname, job=None, pay=None):
        super().__init__(fname, lname, job)
        self.pay = pay if pay != None else 20_000

class Developer(Employee):
    def __init__(self, fname, lname, job=None, pay=None, language=None):
        super().__init__(fname, lname, job, pay)
        self.language = language
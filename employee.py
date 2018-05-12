class Employee:

    def __init__(self, firstname, lastname):

        self.firstname = firstname
        self.lastname = lastname

    def toJSON(self):

        return {'firstName': self.firstname,
                'lastName': self.lastname}

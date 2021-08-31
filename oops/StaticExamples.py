class Employee:
    company = "Dassault" #Static or Class variable
    employeeno = 1000
    contract_company = "ABC"

    @staticmethod
    def get_eligibility(education, skill):
        education_qualification = ['BE', 'BTech', 'MS', 'MTech']
        skill_qualification = ['Selenium', 'Python', 'Jmeter', 'JavaScript']
        if education in education_qualification and skill in skill_qualification:
            return True
        else:
            return False

    @classmethod
    def create_contract_employee(cls, name):
        gender = "M"
        cls.contract_company = "XYZ"
        return cls(name, gender)

    # ClassMethods have access to the class variables
    @classmethod
    def create_male_employee(cls, name, empno):
        cls.employeeno = empno
        return cls(name, "M", cls.employeeno)

    @classmethod
    def create_female_employee(cls, name, empno):
        cls.employeeno = empno
        gender = "F"
        return cls(name, gender, cls.employeeno)

    def __init__(self, name, gender, empno = None):
        self.name = name
        self.gender = gender
        if empno is None:
            self.empno = Employee.employeeno+1
        else:
            self.empno = empno

    def get_info(self):
        dict1 = {
            'Company': Employee.company,
            'EmpNo': self.employeeno,
            'Emp Name': self.name,
            'Emp gender': self.gender
        }

        return dict1

    def print_info(self):
        print(self.get_info())


if Employee.get_eligibility("BE", "Selenium"):
    e1 = Employee("Ameya Naik", "M")
    e1.print_info()

print(e1.get_eligibility("BTech", "Python"))

e2 = Employee.create_male_employee("Roger", 5001)
e2.print_info()

c1 = Employee.create_contract_employee("Virat")
c1.print_info()
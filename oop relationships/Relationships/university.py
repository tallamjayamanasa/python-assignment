class EducationalInstitution:
    def show_institution(self):
        print("This is an educational institution")


class Department:
    def __init__(self, name):
        self.name = name

    def show_department(self):
        print("Department:", self.name)


class ExaminationService:
    def conduct_exam(self):
        print("Examination is conducted")


class University(EducationalInstitution):
    def __init__(self):
        self.departments = [
            Department("Computer Science"),
            Department("Mechanical"),
            Department("Civil")
        ]

    def show_departments(self):
        for department in self.departments:
            department.show_department()

    def conduct_examination(self, examination_service):
        examination_service.conduct_exam()


university = University()
exam = ExaminationService()

university.show_institution()
university.show_departments()
university.conduct_examination(exam)
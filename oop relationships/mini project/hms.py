class Employee:
    def work(self):
        print("Employee is working")


class Doctor(Employee):
    def work(self):
        print("Doctor treats patients")


class Nurse(Employee):
    def work(self):
        print("Nurse takes care of patients")


class Patient:
    def __init__(self, name):
        self.name = name

    def show_patient(self):
        print("Patient:", self.name)


class BillingService:
    def generate_bill(self, amount):
        print("Hospital bill:", amount)


class Hospital:
    def __init__(self):
        self.doctors = [
            Doctor(),
            Doctor()
        ]

        self.patients = [
            Patient("Jaya"),
            Patient("Ravi")
        ]

    def show_details(self):
        for doctor in self.doctors:
            doctor.work()

        for patient in self.patients:
            patient.show_patient()

    def create_bill(self, billing_service):
        billing_service.generate_bill(5000)


hospital = Hospital()
billing = BillingService()

hospital.show_details()
hospital.create_bill(billing)
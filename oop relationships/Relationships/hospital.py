class Doctor:
    def __init__(self, name):
        self.name = name

    def show_doctor(self):
        print("Doctor:", self.name)


class Patient:
    def __init__(self, name):
        self.name = name

    def show_patient(self):
        print("Patient:", self.name)


class BillingService:
    def generate_bill(self, amount):
        print("Bill amount:", amount)


class Hospital:
    def __init__(self):
        self.doctors = [
            Doctor("Dr. Ravi"),
            Doctor("Dr. Sita")
        ]

        self.patients = [
            Patient("Jaya"),
            Patient("Anu")
        ]

    def show_details(self):
        for doctor in self.doctors:
            doctor.show_doctor()

        for patient in self.patients:
            patient.show_patient()

    def create_bill(self, billing_service):
        billing_service.generate_bill(5000)


hospital = Hospital()
billing = BillingService()

hospital.show_details()
hospital.create_bill(billing)
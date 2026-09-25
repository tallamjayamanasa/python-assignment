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

class Hospital:
    def __init__(self):
        self.doctors = [
            Doctor("Dr. Ravi"),
            Doctor("Dr. Sita")
        ]

        self.patients = [
            Patient("Jaya"),
            Patient("Anu"),
            Patient("Kiran")
        ]

    def show_details(self):
        print("Doctors:")
        for doctor in self.doctors:
            doctor.show_doctor()

        print("Patients:")
        for patient in self.patients:
            patient.show_patient()

hospital = Hospital()
hospital.show_details()
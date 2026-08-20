class Patient:
    def __init__(self, patient_id, name, age):
        self.patient_id = patient_id
        self.name = name
        self.age = age

    def display(self):
        print("Patient ID:", self.patient_id)
        print("Name:", self.name)
        print("Age:", self.age)


class Doctor:
    def __init__(self, doctor_id, name, specialization):
        self.doctor_id = doctor_id
        self.name = name
        self.specialization = specialization

    def display(self):
        print("Doctor ID:", self.doctor_id)
        print("Doctor Name:", self.name)
        print("Specialization:", self.specialization)


class Appointment:
    def __init__(self, patient, doctor, date):
        self.patient = patient
        self.doctor = doctor
        self.date = date

    def display(self):
        print("Patient:", self.patient.name)
        print("Doctor:", self.doctor.name)
        print("Date:", self.date)


patient = Patient(101, "Ravi", 25)
doctor = Doctor(201, "Dr. Kumar", "Cardiology")
appointment = Appointment(patient, doctor, "20-08-2026")

print("--- Patient ---")
patient.display()

print("\n--- Doctor ---")
doctor.display()

print("\n--- Appointment ---")
appointment.display()
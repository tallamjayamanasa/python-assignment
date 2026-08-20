class Hospital:
    def __init__(self, patient_name, age, disease, doctor_name):
        self.patient_name = patient_name
        self.age = age
        self.disease = disease
        self.doctor_name = doctor_name

patient1 = Hospital("Rahul", 25, "Fever", "Dr. Kumar")
patient2 = Hospital("Priya", 30, "Cold", "Dr. Anil")
patient3 = Hospital("Sita", 40, "Diabetes", "Dr. Ravi")

print("Patient 1")
print("Name:", patient1.patient_name)
print("Age:", patient1.age)
print("Disease:", patient1.disease)
print("Doctor:", patient1.doctor_name)

print("\nPatient 2")
print("Name:", patient2.patient_name)
print("Age:", patient2.age)
print("Disease:", patient2.disease)
print("Doctor:", patient2.doctor_name)

print("\nPatient 3")
print("Name:", patient3.patient_name)
print("Age:", patient3.age)
print("Disease:", patient3.disease)
print("Doctor:", patient3.doctor_name)
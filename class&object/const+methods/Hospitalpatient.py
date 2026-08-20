class HospitalPatient:
    def __init__(self, patient_name, age, disease, doctor_name):
        self.patient_name = patient_name
        self.age = age
        self.disease = disease
        self.doctor_name = doctor_name

    def display(self):
        print("Patient Name:", self.patient_name)
        print("Age:", self.age)
        print("Disease:", self.disease)
        print("Doctor Name:", self.doctor_name)

patient = HospitalPatient(
    "Rahul",
    25,
    "Fever",
    "Dr. Kumar"
)

patient.display()
class InvalidPatientError(Exception):
    pass


class DoctorNotAvailableError(Exception):
    pass


class InvalidAppointmentError(Exception):
    pass


class Hospital:
    def __init__(self):
        self.doctors = {
            "cardiologist": True,
            "dentist": False,
            "general": True
        }

    def book_appointment(self, name, age, doctor, date):
        if name.strip() == "":
            raise InvalidPatientError(
                "Patient name cannot be empty."
            )

        if age <= 0 or age > 120:
            raise InvalidPatientError(
                "Invalid patient age."
            )

        if doctor not in self.doctors:
            raise DoctorNotAvailableError(
                "Doctor does not exist."
            )

        if not self.doctors[doctor]:
            raise DoctorNotAvailableError(
                "Doctor is not available."
            )

        if date.strip() == "":
            raise InvalidAppointmentError(
                "Appointment date cannot be empty."
            )

        print("Appointment booked successfully.")
        print("Patient:", name)
        print("Doctor:", doctor)
        print("Date:", date)


hospital = Hospital()

try:
    name = input("Enter patient name: ")
    age = int(input("Enter patient age: "))
    doctor = input("Enter doctor type: ").lower()
    date = input("Enter appointment date: ")

    hospital.book_appointment(name, age, doctor, date)

except (InvalidPatientError, DoctorNotAvailableError,
        InvalidAppointmentError) as e:
    print("Error:", e)

except ValueError:
    print("Error: Enter a valid age.")
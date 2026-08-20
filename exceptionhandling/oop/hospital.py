class InvalidPatientError(Exception):
    pass


class Hospital:
    def add_patient(self, name, age):
        try:
            if name.strip() == "":
                raise InvalidPatientError(
                    "Patient name cannot be empty."
                )

            if age <= 0 or age > 120:
                raise InvalidPatientError(
                    "Invalid patient age."
                )

            print("Patient added successfully.")
            print("Name:", name)
            print("Age:", age)

        except InvalidPatientError as e:
            print("Error:", e)


hospital = Hospital()

name = input("Enter patient name: ")

try:
    age = int(input("Enter patient age: "))
    hospital.add_patient(name, age)

except ValueError:
    print("Error: Enter a valid age.")
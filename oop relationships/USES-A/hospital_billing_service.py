class BillingService:
    def generate_bill(self, patient_name, amount):
        print(f"Generating bill for {patient_name}: ${amount:.2f}")


class Hospital:
    def __init__(self, name):
        self.name = name
        self.billing_service = BillingService()

    def bill_patient(self, patient_name, amount):
        self.billing_service.generate_bill(patient_name, amount)


def run_demo():
    hospital = Hospital("Green Valley Hospital")
    print("Hospital -> BillingService example")
    hospital.bill_patient("Emma White", 1200.50)
    print()

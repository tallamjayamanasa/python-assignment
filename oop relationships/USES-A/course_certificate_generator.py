class CertificateGenerator:
    def generate_certificate(self, course):
        print(f"Generating certificate for {course.student_name} in {course.course_name}.")


class Course:
    def __init__(self, course_name, student_name):
        self.course_name = course_name
        self.student_name = student_name
        self.certificate_generator = CertificateGenerator()

    def award_certificate(self):
        self.certificate_generator.generate_certificate(self)


def run_demo():
    course = Course("Python Fundamentals", "Anna Brown")
    print("Course -> CertificateGenerator example")
    course.award_certificate()
    print()

from student_printer import run_demo as student_printer_demo
from bank_account_payment_service import run_demo as bank_account_demo
from shopping_cart_payment_gateway import run_demo as shopping_cart_demo
from employee_report_generator import run_demo as employee_demo
from student_notification_service import run_demo as student_notification_demo
from order_email_service import run_demo as order_email_demo
from library_search_service import run_demo as library_demo
from hospital_billing_service import run_demo as hospital_demo
from food_order_delivery_service import run_demo as food_order_demo
from course_certificate_generator import run_demo as course_demo


def main():
    student_printer_demo()
    bank_account_demo()
    shopping_cart_demo()
    employee_demo()
    student_notification_demo()
    order_email_demo()
    library_demo()
    hospital_demo()
    food_order_demo()
    course_demo()


if __name__ == "__main__":
    main()

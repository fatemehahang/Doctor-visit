import unittest
from controller.payment_controller import PaymentController

class TestPaymentController(unittest.TestCase):

    def test_save_payment(self):
        status, message = PaymentController.save("income", "cash", "2024/02/03", 5, 1000000, 1, "Payment description")
        self.assertTrue(status)
        self.assertIn("Saved Successfully", message)

    def test_find_all_payments(self):
        status, payment_list = PaymentController.find_all()
        self.assertTrue(status)
        self.assertIsInstance(payment_list, list)

    def test_find_by_id(self):
        status, message = PaymentController.save("", "", "", "", "", "")
        if status:
            status, payment_list = PaymentController.find_all()
            if payment_list:
                payment_id = payment_list[-1].id
                status, payment = PaymentController.find_by_id(payment_id)
                self.assertTrue(status)
                self.assertIsNotNone(payment)

    def test_update_payment(self):
        status, message = PaymentController.save("income", "check", "2024/01/03", 1, 300000, 1, "Before")
        if status:
            status_all, payment_list = PaymentController.find_all()
            if payment_list:
                payment_id = payment_list[-1].payment_id
                status, message = PaymentController.update(payment_id, "income", "cash", "2025/01/10", 1, 450000, 1,
                                                           "After")
                self.assertTrue(status)

    def test_delete_payment(self):
        status, message = PaymentController.save("expense", "cash", "2024/01/05", 2, 100000, 2, "To delete")
        if status:
            status_all, payment_list = PaymentController.find_all()
            if payment_list:
                payment_id = payment_list[-1].payment_id
                status, message = PaymentController.delete(payment_id)
                self.assertTrue(status)
                self.assertIn("Deleted Successfully", message)

    def test_find_by_transaction_type(self):
        status, payment_list = PaymentController.find_by_transaction_type("income")
        self.assertTrue(status)
        self.assertIsInstance(payment_list, list)

    def test_find_by_payment_type(self):
        status, payment_list = PaymentController.find_by_payment_type("cash")
        self.assertTrue(status)
        self.assertIsInstance(payment_list, list)

    if __name__ == "__main__":
        unittest.main()
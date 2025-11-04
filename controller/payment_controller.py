from model.entity.payment import Payment
from model.service.payment_service import PaymentService
from tools.logging import Logger

class PaymentController:
    @classmethod
    def save(cls, transaction_type, payment_type, date_time, patient_id, total_amount, description):
        try:
            payment = Payment(None, transaction_type, payment_type, date_time, patient_id, total_amount, description)
            payment.validate()
            payment = PaymentService.save(payment)
            Logger.info(f"Payment {payment} saved successfully")
            return True, f"Payment Saved Successfully"
        except Exception as e:
            Logger.error(f"Payment save Error: {e}")
            return False, e

    @classmethod
    def update(cls, payment_id, transaction_type, payment_type, date_time, patient_id, total_amount, description):
        try:
            payment = Payment(payment_id, transaction_type, payment_type, payment_id, date_time, patient_id, total_amount, description)
            payment.validate()
            payment = PaymentService.update(payment)
            Logger.info(f"Payment {payment} updated successfully")
            return True, f"Payment Updated Successfully"
        except Exception as e:
            Logger.error(f"Payment update Error: {e}")
            return False, e

    @classmethod
    def delete(cls, payment_id):
        try:
            payment = PaymentService.delete(payment_id)
            Logger.info(f"Payment {payment} deleted successfully")
            return True, f"Payment Deleted Successfully"
        except Exception as e:
            Logger.error(f"Payment delete Error: {e}")
            return False, e

    @classmethod
    def find_all(cls):
        try:
            payment_list = PaymentService.find_all()
            Logger.info(f"Payments found successfully")
            return True, payment_list
        except Exception as e:
            Logger.error(f"Payments FindAll Error: {e}")
            return False, e

    @classmethod
    def find_by_id(cls, payment_id):
        try:
            payment = PaymentService.find_by_id(payment_id)
            Logger.info(f"Payments FindById {payment_id}")
            return True, payment
        except Exception as e:
            Logger.error(f"Payments FindById Error: {payment_id}")
            return False, e

    @classmethod
    def find_by_transaction_type(cls, transaction_type):
        try:
            payment_list = PaymentService.find_by_transaction_type(transaction_type)
            Logger.info(f"Payments FindByTransactionType {transaction_type}")
            return True, payment_list
        except Exception as e:
            Logger.error(f"Payments FindByTransactionType Error: {transaction_type}")
            return False, e

    def find_by_payment_type(self, payment_type):
        try:
            payment_list = PaymentService.find_by_payment_type(payment_type)
            Logger.info(f"Payments FindByPaymentType {payment_type}")
            return True, payment_list
        except Exception as e:
            Logger.error(f"Payments FindByPaymentType Error: {payment_type}")
            return False, e

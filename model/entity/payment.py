from tools.payment_validator import *
from model.service.visit_service import VisitService

class Payment:
    def __init__(self, payment_id, transaction_type, payment_type, date_time, patient_id, total_amount, description):
        self.payment_id = payment_id
        self.transaction_type = transaction_type
        self.payment_type = payment_type
        self.date_time = date_time
        self.patient_id = patient_id
        self.total_amount = total_amount
        self.description = description

    def validate(self):
        transaction_type_validator(self.transaction_type)
        payment_type_validator(self.payment_type)
        date_time_validator(self.date_time)
        patient_id_validator(self.patient_id)
        total_amount_validator(self.total_amount)
        description_validator(self.description)

    def __repr__(self):
        return f"{self.__dict__}"

    def to_tuple(self):
        patient = VisitService.find_by_id(self.patient_id)
        return tuple((self.payment_id, self.transaction_type, self.payment_type, self.date_time, patient.full_name(),
                     self.total_amount, self.description))
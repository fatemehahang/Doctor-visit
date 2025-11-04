from tools.visit_validator import *


class Visit:
    def __init__(self, patient_id, first_name, last_name, phone_number, doctor_name,
                 date_time, description=None):

        self.patient_id = patient_id
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.doctor_name = doctor_name
        self.date_time = date_time
        self.description = description

    def validate(self):
        first_name_validator(self.first_name)
        last_name_validator(self.last_name)
        phone_number_validator(self.phone_number)
        doctor_name_validator(self.doctor_name)
        datetime_validator(self.date_time)
        description_validator(self.description)

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __repr__(self):
        return f"{self.__dict__}"

    def to_tuple(self):
        return tuple(
            (self.patient_id, self.first_name, self.last_name, self.phone_number,
             self.doctor_name, self.date_time, self.description))

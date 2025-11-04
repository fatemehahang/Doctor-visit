from os.path import exists

import db
from model import *
from model.entity.visit import Visit
from model.service import *
from model.repository.visit_repository import exists_visit_at_time
from model.service.visit_service import VisitService
from tools.logging import Logger

class VisitController:
    @classmethod
    def save(cls, first_name, last_name, phone_number, doctor_name, date_time, description):
        try:
            visit = Visit(None, first_name, last_name, phone_number, doctor_name, date_time, description)
            if exists_visit_at_time(date_time):
                return False
            visit.validate()
            visit = VisitService.save(visit)
            Logger.info(f"Visit {visit} Saved")
            return True, f"Visit Saved Successfully"
        except Exception as e:
            Logger.error(f"Visit Save Error: {e}")
            return False, e

    @classmethod
    def update(cls, patient_id, first_name, last_name, phone_number, doctor_name, date_time, description):
        try:
            visit = Visit(patient_id, first_name, last_name, phone_number, doctor_name, date_time, description)
            visit.validate()
            visit = VisitService.update(visit)
            Logger.info(f"Visit {visit} Updated")
            return True, f"Visit Updated Successfully"
        except Exception as e:
            Logger.error(f"Visit Update Error: {e}")
            return False, e

    @classmethod
    def delete(cls, patient_id):
        try:
            visit = VisitService.delete(patient_id)
            Logger.info(f"Visit {visit} Deleted")
            return True, f"Visit Deleted Successfully"
        except Exception as e:
            Logger.error(f"Visit Delete Error: {e}")
            return False, e

    @classmethod
    def find_all(cls):
        try:
            visit_list = VisitService.find_all()
            Logger.info(f"Visit FoundAll")
            return True, visit_list
        except Exception as e:
            Logger.error(f"Visit FindAll Error: {e}")
            return False, e

    @classmethod
    def find_by_id(cls, patient_id):
        try:
            visit = VisitService.find_by_id(patient_id)
            Logger.info(f"Visit FindById {patient_id}")
            return True, visit
        except Exception as e:
            Logger.error(f"Visit FindById Error {patient_id}")
            return False, e

    @classmethod
    def find_by_firstname_and_lastname(cls, first_name, last_name):
        try:
            visit_list = VisitService.find_by_firstname_and_lastname(first_name, last_name)
            Logger.info(f"Visit FoundByFirstnameAndLastname {first_name} {last_name}")
            return True, visit_list
        except Exception as e:
            Logger.error(f"Visit FindByFirstnameAndLastname Error: {e}")
            return False, e

    @classmethod
    def find_by_phone_number(cls, phone_number):
        try:
            visit_list = VisitService.find_by_phone_number(phone_number)
            Logger.info(f"Visit FoundByPhoneNumber {phone_number}")
            return True, visit_list
        except Exception as e:
            Logger.error(f"Visit FindByPhoneNumber Error: {e}")
            return False, e
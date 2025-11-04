from model.repository.visit_repository import VisitRepository

class VisitService:
    visit_repository = VisitRepository()

    @classmethod
    def save(cls, visit):
        return cls.visit_repository.save(visit)

    @classmethod
    def update(cls, visit):
        visit_result = cls.visit_repository.find_by_id(visit.patient_id)
        if visit_result :
            return cls.visit_repository.update(visit)
        else:
            raise Exception("Visit not found !!")

    @classmethod
    def delete(cls, patient_id):
        visit = cls.visit_repository.find_by_id(patient_id)
        if visit :
            cls.visit_repository.delete(patient_id)
            return visit
        else:
            raise Exception("Visit not found !!")

    @classmethod
    def find_all(cls):
        return cls.visit_repository.find_all()

    @classmethod
    def find_by_id(cls, patient_id):
        visit = cls.visit_repository.find_by_id(patient_id)
        if visit :
            return visit
        else:
            raise Exception("Visit not found !!")

    @classmethod
    def find_by_firstname_and_lastname(cls, firstname, lastname):
        return cls.visit_repository.find_by_firstname_and_lastname(firstname, lastname)

    @classmethod
    def find_by_phone_number(cls, phone_number):
        return cls.visit_repository.find_by_phone_number(phone_number)

import sqlite3
from model.entity.visit import Visit

class VisitRepository:
    def connect(self):
        self.connection = sqlite3.connect('./db/visit_db')
        self.cursor = self.connection.cursor()

    def disconnect(self):
        self.cursor.close()
        self.connection.close()

    def save(self, visit):
        self.connect()
        self.cursor.execute("insert into visit (first_name, last_name, phone_number, doctor_name, date_time, description) values (?,?,?,?,?,?)",
                            [visit.first_name, visit.last_name, visit.phone_number, visit.doctor_name, visit.date_time, visit.description])
        visit.patient_id = self.cursor.lastrowid
        self.connection.commit()
        return visit

    def update(self, visit):
        self.connect()
        self.cursor.execute("update visit set first_name=?, last_name=?, phone_name=?, doctor_name=?, date_time=?, description=? where id=?",
                            [visit.first_name, visit.last_name, visit.phone_number, visit.doctor_name, visit.date_time, visit.description])
        self.connection.commit()
        self.disconnect()
        return visit

    def delete(self, id):
        self.connect()
        self.cursor.execute("delete from visit where id=?",[id])
        self.connection.commit()
        self.disconnect()

    def find_all(self):
        self.connect()
        self.cursor.execute("select * from visit")
        visit_list = [Visit(*visit) for visit in self.cursor.fetchall()]
        self.disconnect()
        return visit_list

    def find_by_id(self, patient_id):
        self.connect()
        self.cursor.execute("select * from visit where id=?",[patient_id])
        visit = self.cursor.fetchone()
        if visit:
            return Visit(*visit)
        return None

    def find_by_firstname_and_lastname(self, firstname, lastname):
        self.connect()
        self.cursor.execute("select * from visit where first_name=? and last_name=?",[firstname, lastname])
        visit_list = [Visit(*visit) for visit in self.cursor.fetchall()]
        self.disconnect()
        return visit_list

    def find_by_phone_number(self, phone_number):
        self.connect()
        self.cursor.execute("select * from visit where phone_number=?",[phone_number])
        visit_list = [Visit(*visit) for visit in self.cursor.fetchall()]
        self.disconnect()
        return visit_list

def exists_visit_at_time(self, patient_id, date_time):
    self.connect()
    self.cursor.execute("select * from visit where {patient_id} and date_time={date_time}")
    self.disconnect()
    return
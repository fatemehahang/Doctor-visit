import sqlite3
from model.entity.payment import Payment

class PaymentRepository:
    def connect(self):
        self.connection = sqlite3.connect("./db/payment_db")
        self.cursor = self.connection.cursor()

    def disconnect(self):
        self.connection.close()
        self.cursor.close()

    def save(self, payment):
        self.connect()
        self.cursor.execute("insert into payment (transaction_type, payment_type, date_time, patient_id, total_amount, description) values (?, ?, ?, ?, ?, ?)",
                            [payment.transaction_type, payment.payment_type, payment.date_time, payment.total_amount, payment.payment_id, payment.description])
        payment.payment_id = self.cursor.lastrowid
        self.connection.commit()
        return payment

    def update(self, payment):
        self.connect()
        self.cursor.execute("update payment set transaction_type=?, payment_type, date_time=?, patient_id=?, total_amount=?, description=? where id=?",
                            [payment.transaction_type, payment.payment_type, payment.date_time, payment.total_amount, payment.payment_id, payment.description])
        self.connection.commit()
        self.disconnect()
        return payment

    def delete(self, id):
        self.connect()
        self.cursor.execute("delete from payment where id=?", [id])
        self.connection.commit()
        self.disconnect()

    def find_all(self):
        self.connect()
        self.cursor.execute("select * from payment")
        payment_list = [Payment(*payment) for payment in self.cursor.fetchall()]
        self.disconnect()
        return payment_list

    def find_by_id(self, payment_id):
        self.connect()
        self.cursor.execute("select * from payment where id=?", [payment_id])
        payment = self.cursor.fetchone()
        self.disconnect()
        if payment:
            return Payment(*payment)
        return None

    def find_by_transaction_type(self, transaction_type):
        self.connect()
        self.cursor.execute("select * from payment where transaction_type=?", [transaction_type])
        payment_list = [Payment(*payment) for payment in self.cursor.fetchall()]
        self.disconnect()
        return payment_list

    def find_by_payment_type(self, payment_type):
        self.connect()
        self.cursor.execute("select * from payment where payment_type=?", [payment_type])
        payment_list = [Payment(*payment) for payment in self.cursor.fetchall()]
        self.disconnect()
        return payment_list

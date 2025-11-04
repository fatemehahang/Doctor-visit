import unittest
from controller.visit_controller import VisitController


class TestVisitController(unittest.TestCase):

    def test_save_visit(self):
        status, message = VisitController.save("Fatemeh", "Mohammadi", "09124589617", "AliRezaei", "1404/02/10", "jdlekjrfclerlkejbvkjebrufkjfk")
        self.assertTrue(status)
        self.assertIn("Saved successfully", message)

    def test_update_visit(self):
        status, message = VisitController.save("Fatemeh", "Mohammadi", "09124589617", "AliRezaei", "1404/02/10", "jdlekjrfclerlkejbvkjebrufkjfk")
        if status:
            status_all, visit_list = VisitController.find_all()
            if visit_list:
                patient_id = visit_list[-1].patient_id
                status, message = VisitController.update("Fatemeh", "ahang", "09124589617", "AliRezaei", "1404/02/10", "jdlekjrfclerlkejbvkjebrufkjfk")
                self.assertTrue(status)

    def test_delete_visit(self):
        status, message = VisitController.save("", "", "", "", "", "")
        if status:
            status_all, visit_list = VisitController.find_all()
            if visit_list:
                patient_id = visit_list[-1].patient_id
                status, message = VisitController.delete(patient_id)
                self.assertTrue(status)
                self.assertIn("Deleted successfully", message)

    def test_find_all_visits(self):
        status, visit_list = VisitController.find_all()
        self.assertTrue(status)
        self.assertIsInstance(visit_list, list)

    def test_find_by_id(self):
        status, message = VisitController.save("fatemeh", "akbari", "09127865914", "AliRazaei", "1404/02/10")
        if status:
            status_all, visit_list = VisitController.find_all()
            if visit_list:
                patient_id = visit_list[-1].patient_id
                status, patient = VisitController.find_by_id(patient_id)
                self.assertTrue(status)
                self.assertIsInstance(patient)

    def test_find_by_firstname_and_lastname(self):
        status, visit_list = VisitController.find_by_firstname_and_lastname("", "")
        self.assertTrue(status)
        self.assertIsInstance(visit_list, list)

    def test_find_by_phone_number(self):
        status, visit_list = VisitController.find_by_phone_number("")
        self.assertTrue(status)
        self.assertIsInstance(visit_list, list)

if __name__ == '__main__':
    unittest.main()

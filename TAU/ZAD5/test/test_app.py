import unittest
import requests

BASE_URL = "http://127.0.0.1:5000"

class TestUserAPI(unittest.TestCase):
    def test_get_users(self):
        response = requests.get(f"{BASE_URL}/users")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)

    def test_get_user_by_id_success(self):
        response = requests.get(f"{BASE_URL}/users/1")
        self.assertEqual(response.status_code, 200)
        self.assertIn("name", response.json())
        self.assertIn("email", response.json())

    def test_get_user_by_id_not_found(self):
        response = requests.get(f"{BASE_URL}/users/999")
        self.assertEqual(response.status_code, 404)

    def test_create_user_success(self):
        new_user = {"name": "Katarzyna Wiśniewska", "email": "kasia@wisniewska.pl"}
        response = requests.post(f"{BASE_URL}/users", json=new_user)
        self.assertEqual(response.status_code, 201)
        self.assertIn("id", response.json())
        self.assertEqual(response.json()["name"], new_user["name"])

    def test_create_user_invalid_data(self):
        invalid_user = {"name": "No Email"}
        response = requests.post(f"{BASE_URL}/users", json=invalid_user)
        self.assertEqual(response.status_code, 400)

    def test_update_user_success(self):
        updated_user = {"name": "Updated Name", "email": "updated@example.com"}
        response = requests.put(f"{BASE_URL}/users/1", json=updated_user)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["name"], updated_user["name"])

    def test_update_user_not_found(self):
        updated_user = {"name": "Updated Name", "email": "updated@example.com"}
        response = requests.put(f"{BASE_URL}/users/999", json=updated_user)
        self.assertEqual(response.status_code, 404)

    def test_delete_user_success(self):
        response = requests.delete(f"{BASE_URL}/users/1")
        self.assertEqual(response.status_code, 204)

        # Verify user is deleted
        response = requests.get(f"{BASE_URL}/users/1")
        self.assertEqual(response.status_code, 404)

    def test_delete_user_not_found(self):
        response = requests.delete(f"{BASE_URL}/users/999")
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()
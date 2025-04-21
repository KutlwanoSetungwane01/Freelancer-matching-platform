import unittest
from creational_patterns.simple_factory.UserFactory import UserFactory
from creational_patterns.simple_factory.UserTypes import Freelancer, Employer

class TestUserFactory(unittest.TestCase):
    def test_create_freelancer(self):
        user = UserFactory.create_user("freelancer", 1, "Lebo", "lebo@example.com")
        self.assertIsInstance(user, Freelancer)
        self.assertEqual(user.role, "freelancer")
        self.assertEqual(user.name, "Lebo")

    def test_create_employer(self):
        user = UserFactory.create_user("employer", 2, "Sarah", "sarah@example.com")
        self.assertIsInstance(user, Employer)
        self.assertEqual(user.role, "employer")
        self.assertEqual(user.email, "sarah@example.com")

    def test_invalid_user_type(self):
        with self.assertRaises(ValueError):
            UserFactory.create_user("admin", 3, "Mike", "mike@example.com")

if __name__ == "__main__":
    unittest.main()

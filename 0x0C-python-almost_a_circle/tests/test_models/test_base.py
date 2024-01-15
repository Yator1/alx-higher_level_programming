from models.base import Base
import unittest

class TestBase(unittest.TestCase):
    def test_idAssignement(self):
        """
        check auto incrementind id assignement
        test explicit id assignment
        """
        b1 = Base()
        b2 = Base()
        b3 = Base(9)

        self.assertEqual(b1.id, 2)
        self.assertEqual(b2.id, 3)
        self.assertEqual(b3.id, 9)

    def test_PrivateAttribute(self):
        """ attempt to access private attribute"""
        b1 = Base()

        with self.assertRaises(AttributeError):
            b1.__nb_objects

    def test_invalidIdType(self):
        """ test if TypeError is raised if id is not integer"""
        b1 = Base()
        with self.assertRaises(TypeError):
            b1("id")

    def test_existingId(self):
        """ Test id with same id """
        b1 = Base(1)
        b2 = Base(1)

        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 1)

    def test_to_jsonString(self):
        dict_list = [{'id': 3, 'name': 'John'}, {'id': 2, 'name' : 'Ben'}]
        json_str = Base.to_json_string(dict_list)
        expected_list = '[{"id": 3, "name": "John"}, {"id": 2, "name": "Ben"}]'
        self.assertEqual(json_str, expected_list)

        empty_list = []
        json_str = Base.to_json_string(empty_list)
        self.assertEqual(json_str, '[]')

    def test_from_json_string(self):
        json_str = '[{"id": 3, "name": "John"}, {"id": 2, "name": "Ben"}]'
        dict_list = Base.from_json_string(json_str)
        expected_list = [{"id": 3, "name": "John"}, {"id": 2, "name": "Ben"}]
        self.assertEqual(dict_list, expected_list)

        empty_json = ''
        dict_list = Base.from_json_string(empty_json)
        self.assertEqual(dict_list, [])

    


if __name__ == '__main__':
    unittest.main()

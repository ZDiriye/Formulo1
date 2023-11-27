import sqlalchemy as db
import unittest
from unittest.mock import patch

# connects to database


def get_database_engine():
    return db.create_engine('sqlite:////Users/zakariyediriye/Formulo1/FORMULA1.db')

class TestDatabaseEngine(unittest.TestCase):
    @patch('sqlalchemy.create_engine')
    def test_engine(self, mock_create_engine):
        expected_db_url = 'sqlite:////Users/zakariyediriye/Formulo1/FORMULA1.db'

        # set up the mock return value for create_engine
        mock_create_engine.return_value = "Mocked Engine"

        result = get_database_engine()

        mock_create_engine.assert_called_once_with(expected_db_url)
        self.assertEqual(result, "Mocked Engine")

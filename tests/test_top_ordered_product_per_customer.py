# pylint: disable-all
import os
import sqlite3
from nbresult import ChallengeResultTestCase

class TestTopOrderedProductPerCustomer(ChallengeResultTestCase):
    db_path = os.path.join(os.path.dirname(__file__), '../data/ecommerce.sqlite')

    def query_db(self, query, *args):
        conn = sqlite3.connect(self.db_path)
        db = conn.cursor()
        db.execute(query, args)
        results = db.fetchall()
        return results

    def test_length_results(self):
        results = self.query_db(self.result.query)
        self.assertEqual(len(results), 5)

    expected = [
        (4, 6, 5876),
        (2, 5, 2791.6),
        (1, 6, 1909.7),
        (3, 3, 1200),
        (5, 6, 1175.2)
    ]

    def test_result_type(self):
        results = self.query_db(self.result.query)
        self.assertIsInstance(results, list)
        self.assertIsInstance(results[0], tuple)

    def test_result_length(self):
        results = self.query_db(self.result.query)
        self.assertEqual(len(results), len(self.expected))

    def test_result_values(self):
        results = self.query_db(self.result.query)
        self.assertEqual(results[0], self.expected[0])
        self.assertEqual(results[-1], self.expected[-1])

import unittest

import HtmlTestRunner

from p8_api_testing.requests_folder.simple_books_requests import SimpleBooksRequests
from p8_api_testing.tests.test_delete_order import TestDeleteOrder
from p8_api_testing.tests.test_get_all_books import TestGetAllBooks
from p8_api_testing.tests.test_submit_order import TestSubmitOrder
from p8_api_testing.tests.test_update_order import TestUpdateOrder


class TestSuite(unittest.TestCase):

    def test_suite(self):

        suita_teste = unittest.TestSuite()

        # adaugam testele in suita
        suita_teste.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(SimpleBooksRequests),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestGetAllBooks),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestSubmitOrder),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestUpdateOrder),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestDeleteOrder)
        ])

        runner = HtmlTestRunner.HTMLTestRunner(
            combine_reports=True,
            report_title="API test report",
            report_name="Books API Test Results"
        )

        runner.run(suita_teste)
import pytest
import pytest_mock
from service.customer_service import CustomerService
from dao.customer_dao import CustomerDao
from model.customer import Customer

def test_get_customers(mocker):
    def mock_get_customers(self):
        return[
            Customer(1, 'test_first_name_1', 'test_last_name_1', 'test_mobile_phone_1', 'test_email_1'),
            Customer(2, 'test_first_name_2', 'test_last_name_2', 'test_mobile_phone_2', 'test_email_2'),
            Customer(3, 'test_first_name_3', 'test_last_name_3', 'test_mobile_phone_3', 'test_email_3')
        ]

    mocker.patch('dao.customer_dao.CustomerDao.get_customers', mock_get_customers)
    customer_service = CustomerService()
    actual = customer_service.get_customers()

    assert actual == [
        {
            "id": 1,
            "first_name": "test_first_name_1",
            "last_name": "test_last_name_1",
            "mobile_phone": "test_mobile_phone_1",
            "email": "test_email_1"
        },
        {
            "id": 2,
            "first_name": "test_first_name_2",
            "last_name": "test_last_name_2",
            "mobile_phone": "test_mobile_phone_2",
            "email": "test_email_2",
        },
        {
            "id": 3,
            "first_name": "test_first_name_3",
            "last_name": "test_last_name_3",
            "mobile_phone": "test_mobile_phone_3",
            "email": "test_email_3"
        }
    ]





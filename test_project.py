import pytest
import os
import csv
from unittest.mock import patch, MagicMock
from datetime import datetime


from rental import load_apartments, save_apartments, Apartment


TEST_FILE = "test_rental.csv"


@pytest.fixture(scope="module")
def setup_test_file():

    with open(TEST_FILE, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Apartment Number", "Tenant Name", "Rent Date", "Rental End Date", "Duration (months)", "Price", "Remaining Payment", "Apartment Type", "Apartment Features"])
        writer.writerow([1, "Test Tenant", "12/15/2024", "12/15/2025", 12, 12000, 12000, "Studio", "Includes: 1 room with combined bedroom, small kitchen, and bathroom"])

    yield  


    os.remove(TEST_FILE)


@pytest.fixture
def mock_input():
    with patch("builtins.input", side_effect=["1", "Test Apartment", "12/15/2024", "1", "1", "12", "1000"]):
        yield


def test_load_apartments(setup_test_file):
    apartments = load_apartments()
    assert len(apartments) == 1
    assert apartments[1].name == "Test Tenant"
    assert apartments[1].price == 12000


def test_save_apartments(setup_test_file):
    apartments = load_apartments()
    apartments[2] = Apartment(num=2, name="New Tenant", month=12, day=15, year=2024, months=12, price=15000, type="1-Bedroom", payment=15000, remaining_payment=15000, features="Includes: 1 bedroom, living room, kitchen, and bathroom")
    save_apartments(apartments)


    apartments = load_apartments()
    assert len(apartments) == 2
    assert apartments[2].name == "New Tenant"
    assert apartments[2].price == 15000


def test_rent_apartment(mock_input):
    apartments = load_apartments()
    apartment = Apartment()
    apartment.rent_apartment(apartments)
    
    assert apartment.num in apartments
    assert apartment.name == "Test Apartment"
    assert apartment.type == "Studio"


def test_update_rental(mock_input):
    apartments = load_apartments()
    apartment = apartments[1]
    original_name = apartment.name
    apartment.update_rental()
    
    assert apartment.name != original_name  
    assert apartment.num == 1


def test_end_rent(mock_input):
    apartments = load_apartments()
    apartment = apartments[1]
    apartment.end_rent(apartments)

    assert apartment.num not in apartments  

if __name__ == "__main__":
    pytest.main()


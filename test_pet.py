from jsonschema import validate
import pytest
import schemas
import api_helpers
from hamcrest import assert_that, contains_string, is_

# TODO: xxxx
def test_valid_pet_id():
    test_endpoint = "/pet/1"

# TODO: Fix this test, which has an incorrect schema
def test_pet_schema():
    test_endpoint = "/pet/1"

    response = api_helpers.get_api_data(test_endpoint)

    assert response.status_code == 200
    validate(instance=response.json(), schema=schemas.pet)


# TODO: Create a new test that validates the response for 'Pet Not Found'
def test_invalid_pet_id():
    test_endpoint = ""


if __name__ == "__main__":
    pytest.main()
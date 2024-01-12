from jsonschema import validate
import pytest
import schemas
import api_helpers
from hamcrest import assert_that, contains_string, is_

'''
TODO: Finish this test by...
1) Troubleshooting and fixing the test failure
'''
def test_get_pet_schema():
    test_endpoint = "/pet/1"

    response = api_helpers.get_api_data(test_endpoint)

    assert response.status_code == 200

    # Validate the response schema against the defined schema in schemas.py
    validate(instance=response.json(), schema=schemas.pet)

'''
TODO: Finish this test by...
1) Extending the parameterization to include each available status
2) Validate the appropriate response code
3) Validate the 'status' property in the response is equal to the expected status
4) Validate the schema for each object in the response
'''
@pytest.mark.parametrize("status", [("available")])
def test_get_find_by_status_200(status):
    test_endpoint = "/pet/findByStatus"
    params = {
        "status": status
    }

    # Get the response
    response = api_helpers.get_api_data(test_endpoint, params)

'''
TODO: Finish this test by...
1) Testing and validating the appropriate 400 response for /pet/findByStatus
2) Parameterizing the test for any edge cases
'''
def test_get_find_by_status_400():
    test_endpoint = "/pet/findByStatus"
    
from jsonschema import validate
import pytest
import schemas
import api_helpers
from hamcrest import assert_that, contains_string, is_

'''
TODO: Finish this test by...
1) Creating a function to test the PATCH request /store/order/{order_id}
2) *Optional* Consider using @pytest.fixture to create unique test data for each run
2) *Optional* Consider creating an 'Order' model in schemas.py and validating it in the test
3) Validate the response codes and values
4) Validate the response message "Order and pet status updated successfully"
'''
def test_patch_order_by_id():
    order_id = 1
    new_order = {'id': order_id, 'pet_id': 0}
    # orders[order_id] = new_order

    # Send a PATCH request to update the order status
    test_endpoint = f"/store/order/{order_id}"
    update_data = {'status': 'pending'}  # Update the status to 'pending' for testing
    response = api_helpers.patch_api_data(test_endpoint, data=update_data)

    # Check if the response status code is 200
    assert response.status_code == response.status_code, f"Expected status code 200 for order ID {order_id}, but got {response.status_code}"

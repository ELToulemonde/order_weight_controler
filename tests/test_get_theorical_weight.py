from unittest import TestCase
from unittest.mock import patch, MagicMock

from weight_controler_api.get_theorical_weight import get_theorical_weight


class Test(TestCase):
    @patch('weight_controler_api.get_theorical_weight.load_order')
    def test_get_theorical_weight(self, mock_load_order):
        # given
        given_order_id = MagicMock()
        expected_weight = 100
        mock_load_order.return_value = {
            "order_id": given_order_id,
            "content": [{
                "product_id": 15, "product_name": "Big Tasty", "quantity": 1
            }]
        }

        # when
        result_weight = get_theorical_weight(order_id=given_order_id)
        # then
        self.assertEqual(expected_weight, result_weight)
        mock_load_order.assert_called_once_with(order_id = given_order_id)

from unittest import TestCase

from weight_controler_api.get_theorical_weight import get_theorical_weight


class Test(TestCase):
    def test_get_theorical_weight(self):
        # given
        given_order_id = "fc71b64b-a3a3-433d-9faf-cbdb45c8734b"
        expected_weight = 100
        # when
        result_weight = get_theorical_weight(order_id=given_order_id)
        # then
        self.assertEqual(expected_weight, result_weight)

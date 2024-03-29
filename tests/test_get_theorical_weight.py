from weight_controler_api.get_theorical_weight import get_theorical_weight


def test_get_theorical_weight():
    # given
    given_order_id = "fc71b64b-a3a3-433d-9faf-cbdb45c8734b"
    expected_weight = 100

    # when
    result = get_theorical_weight(order_id=given_order_id)

    # then
    assert result == expected_weight

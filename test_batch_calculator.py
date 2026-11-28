from batch_calculator import process_calculation


def test_addition_returns_success():
    assert process_calculation("add", "7", "5") == ("OK", 12, "")

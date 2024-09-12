# test_utils.py
import copy


def test_case(func, input_data, expected_output):
    original_input = copy.deepcopy(input_data)  # Orijinal girdiyi kopyalayarak sakla

    try:
        assert func(*input_data) == expected_output
        print(f"Success: {func.__name__}({original_input}) == {expected_output}")
    except AssertionError:
        print(f"Fail: {func.__name__}({original_input}) != {expected_output}, expected {expected_output}")


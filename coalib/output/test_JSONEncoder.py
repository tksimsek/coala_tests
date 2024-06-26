from JSONEncoder import create_json_encoder, branch_coverage
from datetime import datetime
import re

def test_create_json_encoder_branch_coverage():
    encoder = create_json_encoder()

    # Test cases to cover each branch
    test_cases = [
        (CustomObjectWithJsonMethod(), {
            "create_json_encoder_1": True,  # hasattr(obj, '__json__')
        }),
        ([1, 2, 3], {
            "create_json_encoder_2": True,  # isinstance(obj, collections.Iterable)
        }),
        (datetime.now(), {
            "create_json_encoder_3": True,  # isinstance(obj, datetime)
        }),
        ({'key': 'value'}, {
            "create_json_encoder_4": True,  # hasattr(obj, '__getitem__') and hasattr(obj, 'keys')
        }),
        (CustomClass(), {
            "create_json_encoder_5": True,  # hasattr(obj, '__dict__')
        }),
        (re.compile(r'\d+'), {
            "create_json_encoder_6": True,  # isinstance(obj, re._pattern_type)
        }),
        (123, {
            "create_json_encoder_7": True,  # default fallback
        }),
    ]

    for i, (obj, expected_coverage) in enumerate(test_cases):
        result = encoder.default(obj)
        
        # Check branch coverage
        for branch_name, expected_status in expected_coverage.items():
            assert branch_coverage[branch_name] == expected_status, f"Branch {branch_name} not covered as expected."

    print("Final branch coverage:", branch_coverage)

# Example custom classes for testing
class CustomObjectWithJsonMethod:
    def __json__(self):
        return {'custom': 'data'}

class CustomClass:
    def __init__(self):
        self.attribute = 'value'

if __name__ == "__main__":
    test_create_json_encoder_branch_coverage()

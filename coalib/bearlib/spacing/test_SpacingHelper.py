from SpacingHelper import TextProcessor, branch_coverage

def test_replace_spaces_with_tabs_branch_coverage():
    processor = TextProcessor(tab_width=4)

    # Test cases to cover each branch
    test_cases = [
        (" ", " ", {
            "replace_spaces_with_tabs_1": True,
        }),
        ("\t", "\t", {
            "replace_spaces_with_tabs_2": True,
        }),
        ("a", "a", {
            "replace_spaces_with_tabs_3": True,
        }),
        ("    ", "\t", {
            "replace_spaces_with_tabs_1": True,
            "replace_spaces_with_tabs_7": True,
        }),
        ("  a", "  a", {
            "replace_spaces_with_tabs_1": True,
            "replace_spaces_with_tabs_3": True,
        }),
        ("", "", {
            "replace_spaces_with_tabs_3": True,
        }),
    ]

    for i, (input_str, expected_output, expected_coverage) in enumerate(test_cases):
        # Reset branch coverage before each test case
        reset_branch_coverage(branch_coverage)

        result = processor.replace_spaces_with_tabs(input_str)
        assert result == expected_output, f"Test case {i+1} failed: {result} != {expected_output}"

        # Check branch coverage
        for branch_name, expected_status in expected_coverage.items():
            assert branch_coverage[branch_name] == expected_status, f"Branch {branch_name} not covered as expected in test case {i+1}"

    print("Final branch coverage:", branch_coverage)

def reset_branch_coverage(branch_coverage):
    for key in branch_coverage:
        branch_coverage[key] = False

if __name__ == "__main__":
    test_replace_spaces_with_tabs_branch_coverage()

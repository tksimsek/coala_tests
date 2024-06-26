from SpacingHelper import TextProcessor, branch_coverage

def test_replace_spaces_with_tabs_branch_coverage():
    processor = TextProcessor(tab_width=4)

    # Test cases to cover each branch
    test_cases = [
        (" ", " ", {
            "replace_spaces_with_tabs_1": True,  # First if statement (char == ' ')
        }),
        ("\t", "\t", {
            "replace_spaces_with_tabs_2": True,  # First elif statement (char == '\t')
        }),
        ("a", "a", {
            "replace_spaces_with_tabs_3": True,  # Else branch (neither space nor tab)
        }),
        ("    ", "\t", {
            "replace_spaces_with_tabs_4": True,  # If statement for tab alignment (tabless_position % self.tab_width == 0)
            "replace_spaces_with_tabs_5": True,  # If nested in tab alignment (currspaces == 1 and char == ' ')
        }),
        ("  a", "\t  a", {
            "replace_spaces_with_tabs_4": True,  # If statement for tab alignment (tabless_position % self.tab_width == 0)
            "replace_spaces_with_tabs_5": True,  # If nested in tab alignment (currspaces == 1 and char == ' ')
        }),

        ("", "", {
            "replace_spaces_with_tabs_7": True,  # Final appending of remaining spaces
        }),
    ]


    for i, (input_str, expected_output, expected_coverage) in enumerate(test_cases):
        result = processor.replace_spaces_with_tabs(input_str)
        print(f"DEBUG: Result {i+1} = '{result}', Expected = '{expected_output}'")
        assert result == expected_output, f"Test case {i+1} failed: {result} != {expected_output}"

        # Check branch coverage
        for branch_name, expected_status in expected_coverage.items():
            assert branch_coverage[branch_name] == expected_status, f"Branch {branch_name} not covered as expected."

    print("Final branch coverage:", branch_coverage)

if __name__ == "__main__":
    test_replace_spaces_with_tabs_branch_coverage()

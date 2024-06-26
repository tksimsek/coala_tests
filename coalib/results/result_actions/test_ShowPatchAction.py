import ShowPatchAction
from ShowPatchAction import branch_coverage, print_beautified_diff
from unittest.mock import Mock

def print_coverage():
    for branch, hit in branch_coverage.items():
        if hit:
            print(f"{branch} was hit")
        else:
            print(f"{branch} was not hit")

def reset_branch_coverage(branch):
    for key in branch:
        branch[key] = False

def test_print_beautified_diff():
    reset_branch_coverage(branch_coverage)

    # Create a mock printer object
    mock_printer = Mock()

    # Test cases to cover different branches in print_beautified_diff
    print_beautified_diff(['@@ -1,3 +1,3 @@', '- old_line', '+ new_line'], mock_printer)
    print_beautified_diff(['@@ -0,0 +1 @@', '+ new_line'], mock_printer)
    print_beautified_diff(['--- file1.txt', '+++ file2.txt'], mock_printer)
    print_beautified_diff(['+ added_line'], mock_printer)
    print_beautified_diff(['- removed_line'], mock_printer)
    print_beautified_diff(['unmatched_line'], mock_printer)

    # Assert that all branches in branch_coverage are True
    assert all(branch_coverage.values()), "Not all branches covered"

    # Print branch coverage percentage
    print_coverage()

if __name__ == "__main__":
    test_print_beautified_diff()

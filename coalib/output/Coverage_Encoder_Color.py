from ConsoleInteraction import color_letter, branch_coverage
from Interactions import fail_acquire_settings, branch_coverage2

def test_color_letter():
    print("Testing branch coverage for color_letter() ... \n")
    reset_branch_coverage(branch_coverage)
    
    color_letter(ConsolePrinterMock(), "No parentheses")
    color_letter(ConsolePrinterMock(), "Letter (Content)[Warning]")
    color_letter(ConsolePrinterMock(), "Letter (Content) Warning")
    color_letter(ConsolePrinterMock(), "[a")

    print_coverage(branch_coverage)
    print_coverage_percentage(branch_coverage)

class ConsolePrinterMock:
    def print(self, text, color=None, end='\n'):
        pass  # Mock implementation of print method for testing purposes
    
def test_fail_acquire_settings():
    print("Testing branch coverage for fail_acquire_settings() ... \n")
    reset_branch_coverage(branch_coverage2)
    
    try:
        fail_acquire_settings(ConsolePrinterMock(), "not_a_dict")
    except TypeError:
        pass  # Expected exception, no need to handle further
    
    try:
        fail_acquire_settings(ConsolePrinterMock(), {})
    except AssertionError:
        pass  # Expected exception, no need to handle further
    
    try:
        fail_acquire_settings(ConsolePrinterMock(), {"setting1": ["description1", "bear1"]})
    except (TypeError, AssertionError):
        pass  # Expected exceptions, no need to handle further

    print_coverage(branch_coverage2)
    print_coverage_percentage(branch_coverage2)

def calculate_coverage_percentage(branch):
    total_branches = len(branch)
    hit_branches = sum(branch.values())
    coverage_percentage = (hit_branches / total_branches) * 100
    return coverage_percentage

def print_coverage_percentage(branch):
    coverage_percentage = calculate_coverage_percentage(branch)
    print("Branch coverage is {:.2f}% \n".format(coverage_percentage))
    
def print_coverage(branch):
    for i, hit in branch.items():
        if hit:
            print("{} was hit".format(i))
        else:
            print("{} was not hit".format(i))

def reset_branch_coverage(branch):
    for i in branch:
        branch_coverage[i] = False

#Check if file is being ran directly
if __name__ == "__main__":
    test_color_letter()
    test_fail_acquire_settings()
    
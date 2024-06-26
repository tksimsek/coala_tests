from Globbing import _end_of_set_index, branch_coverage, reset_branch_coverage, print_coverage

def test_end_of_set_index():
    reset_branch_coverage()
    
    _end_of_set_index("vu", 1)
    _end_of_set_index("vu]", 1)
    _end_of_set_index("!vu]", 0)
    _end_of_set_index("vu]!", 10)

    print_coverage()

def calculate_coverage_percentage():
    total_branches = len(branch_coverage)
    hit_branches = sum(branch_coverage.values())
    coverage_percentage = (hit_branches / total_branches) * 100
    return coverage_percentage

def print_coverage_percentage():
    coverage_percentage = calculate_coverage_percentage()
    print("Branch coverage is {:.2f}%".format(coverage_percentage))

#Check if file is being ran directly
if __name__ == "__main__":
    test_end_of_set_index()
    print_coverage_percentage()
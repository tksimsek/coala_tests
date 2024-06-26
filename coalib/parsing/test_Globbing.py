from Globbing import _end_of_set_index, translate, branch_coverage, branch_coverage_2

def test_end_of_set_index():
    print("Testing branch coverage for _end_of_set_index() ... \n")
    reset_branch_coverage(branch_coverage)
    
    _end_of_set_index("vu", 1)
    _end_of_set_index("vu]", 1)
    _end_of_set_index("!vu]", 0)
    _end_of_set_index("vu]!", 10)

    print_coverage(branch_coverage)
    print_coverage_percentage(branch_coverage)
    
def test_translate():
    print("Testing branch coverage for translate() ... \n")
    reset_branch_coverage(branch_coverage_2)
    
    translate("*vrije")
    translate("vrije**")
    translate("*vr?je")
    translate("[vrije")
    translate(".vrije]")
    translate(" ")
    translate("![vrije]")
    translate("![!!!]")
    translate("^[^^^]")
    translate("^[vrije]")
    translate("v/r<*!?]")

    print_coverage(branch_coverage_2)
    print_coverage_percentage(branch_coverage_2)

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
    test_end_of_set_index()
    test_translate()
    
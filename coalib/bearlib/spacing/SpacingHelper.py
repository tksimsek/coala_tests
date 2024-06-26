branch_coverage = {
    "replace_spaces_with_tabs_1": False,  # First if statement (char == ' ')
    "replace_spaces_with_tabs_2": False,  # First elif statement (char == '\t')
    "replace_spaces_with_tabs_3": False,  # Else branch (neither space nor tab)
    "replace_spaces_with_tabs_4": False,  # If statement for tab alignment (tabless_position % self.tab_width == 0)
    "replace_spaces_with_tabs_5": False,  # If nested in tab alignment (currspaces == 1 and char == ' ')
    "replace_spaces_with_tabs_6": False,  # Else nested in tab alignment
    "replace_spaces_with_tabs_7": False,  # Final appending of remaining spaces
}

class TextProcessor:
    def __init__(self, tab_width):
        self.tab_width = tab_width

    def replace_spaces_with_tabs(self, line: str):
        global branch_coverage

        result = ''
        currspaces = 0
        tabless_position = 0

        for char in line:
            if char == ' ':
                branch_coverage["replace_spaces_with_tabs_1"] = True
                currspaces += 1
                tabless_position += 1
            elif char == '\t':
                branch_coverage["replace_spaces_with_tabs_2"] = True
                result += ' ' * currspaces
                currspaces = 0
                result += '\t'
                tabless_position = 0  # reset for tab alignment
            else:
                if currspaces == 1 and tabless_position % self.tab_width == 1:
                    result += '\t'
                    branch_coverage["replace_spaces_with_tabs_5"] = True
                elif currspaces > 1 and tabless_position % self.tab_width == 0:
                    result += '\t'
                    branch_coverage["replace_spaces_with_tabs_4"] = True
                else:
                    result += ' ' * currspaces
                    branch_coverage["replace_spaces_with_tabs_6"] = True
                currspaces = 0
                result += char
                tabless_position += 1

            if tabless_position % self.tab_width == 0 and currspaces:
                if currspaces == 1:
                    result += ' '
                    branch_coverage["replace_spaces_with_tabs_5"] = True
                else:
                    result += '\t'
                    branch_coverage["replace_spaces_with_tabs_7"] = True
                currspaces = 0

        result += ' ' * currspaces
        branch_coverage["replace_spaces_with_tabs_3"] = True

        return result

from coalib.bearlib.abstractions.SectionCreatable import SectionCreatable
from coala_utils.decorators import enforce_signature


class SpacingHelper(SectionCreatable):
    DEFAULT_TAB_WIDTH = 4

    def __init__(self, tab_width: int = DEFAULT_TAB_WIDTH):
        """
        Creates a helper object for spacing operations.

        :param tab_width: The number of spaces which visually equals a tab.
        """
        SectionCreatable.__init__(self)
        if not isinstance(tab_width, int):
            raise TypeError("The 'tab_width' parameter should be an integer.")

        self.tab_width = tab_width

    @enforce_signature
    def get_indentation(self, line: str):
        """
        Checks the lines indentation.

        :param line: A string to check for indentation.
        :return:     The indentation count in spaces.
        """
        count = 0
        for char in line:
            if char == ' ':
                count += 1
                continue

            if char == '\t':
                count += self.tab_width - (count % self.tab_width)
                continue

            break

        return count

    @enforce_signature
    def replace_tabs_with_spaces(self, line: str):
        """
        Replaces tabs in this line with the appropriate number of spaces.

        Example: " \t" will be converted to "    ", assuming the tab_width is
        set to 4.

        :param line: The string with tabs to replace.
        :return:     A string with no tabs.
        """
        for t_position, t_length in sorted(self.yield_tab_lengths(line),
                                           reverse=True):
            line = line[:t_position] + t_length * ' ' + line[t_position+1:]

        return line

    @enforce_signature
    def yield_tab_lengths(self, input: str):
        """
        Yields position and size of tabs in a input string.

        :param input: The string with tabs.
        """
        tabless_position = 0
        for index, char in enumerate(input):
            if char == '\t':
                space_count = (self.tab_width - tabless_position
                               % self.tab_width)
                yield index, space_count
                tabless_position += space_count
                continue

            tabless_position += 1

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

    @enforce_signature
    def replace_spaces_with_tabs(self, line: str):
        """
        Replaces spaces with tabs where possible. However in no case only one
        space will be replaced by a tab.

        Example: " \t   a_text   another" will be converted to
        "\t   a_text\tanother", assuming the tab_width is set to 4.

        :param line: The string with spaces to replace.
        :return:     The converted string.
        """
        global branch_coverage
        
        currspaces = 0
        result = ''
        # Tracking the index of the string isn't enough because tabs are
        # spanning over multiple columns
        tabless_position = 0
        for char in line:
            if char == ' ':
                currspaces += 1
                tabless_position += 1
                branch_coverage["replace_spaces_with_tabs_1"] = True
            elif char == '\t':
                space_count = (self.tab_width - tabless_position % self.tab_width)
                currspaces += space_count
                tabless_position += space_count
                branch_coverage["replace_spaces_with_tabs_2"] = True
            else:
                result += currspaces * ' ' + char
                currspaces = 0
                tabless_position += 1
                branch_coverage["replace_spaces_with_tabs_3"] = True

            # tabless_position is now incremented to point _after_ the current
            # char
            if tabless_position % self.tab_width == 0 and currspaces:
                branch_coverage["replace_spaces_with_tabs_4"] = True
                if currspaces == 1 and char == ' ':
                    result += ' '
                    branch_coverage["replace_spaces_with_tabs_5"] = True
                else:
                    result += '\t'
                    branch_coverage["replace_spaces_with_tabs_6"] = True

                currspaces = 0

        result += currspaces * ' '
        branch_coverage["replace_spaces_with_tabs_7"] = True

        return result

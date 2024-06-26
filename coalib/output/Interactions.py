import logging


branch_coverage2 = {
    "not_dict": False,          # Branch for TypeError if settings_names_dict is not a dictionary
    "required_settings": False, # Branch for AssertionError if required settings are not provided
    "no_issues": False,         # Branch for no issues found (hidden else for required_settings)
    "no_exception": False       # Branch for no exception raised (hidden else for not_dict)
}

def fail_acquire_settings(log_printer, settings_names_dict):
    """
    This method throws an exception if any setting needs to be acquired.

    :param log_printer:         Printer responsible for logging the messages.
    :param settings_names_dict: A dictionary with the settings name as key and
                                a list containing a description in [0] and the
                                name of the bears who need this setting in [1]
                                and following.
    :raises AssertionError:     If any setting is required.
    :raises TypeError:          If ``settings_names_dict`` is not a
                                dictionary.
    """
    global branch_coverage2
    
    if not isinstance(settings_names_dict, dict):
        branch_coverage2["not_dict"] = True
        raise TypeError('The settings_names_dict parameter has to be a '
                        'dictionary.')
    else:
        branch_coverage2["no_exception"] = True

    required_settings = settings_names_dict.keys()
    if len(required_settings) != 0:
        branch_coverage2["required_settings"] = True
        msg = ('During execution, we found that some required '
               'settings were not provided. They are:\n')

        for name, setting in settings_names_dict.items():
            msg += f'{name} (from {setting[1]}) - {setting[0]}'

        logging.error(msg)
        raise AssertionError(msg)
    else:
        branch_coverage2["no_issues"] = True
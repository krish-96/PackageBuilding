# Module Constants
AUTHOR = "Gopi Krishna Belamkonda"
AUTHOR_FIRST_NAME = "Gopi"
AUTHOR_LAST_NAME = "Belamkonda"
AUTHOR_MIDDLE_NAME = "Krishna"
AUTHOR_FULL_NAME = AUTHOR_FIRST_NAME + AUTHOR_MIDDLE_NAME + AUTHOR_LAST_NAME


def get_author_name() -> str:
    """ Return the author name """
    return AUTHOR


def get_author_full_name() -> str:
    """ Return the author full name """
    return AUTHOR_FULL_NAME


def get_author_first_name() -> str:
    """ Return the author first name """
    return AUTHOR_FIRST_NAME


def get_author_last_name() -> str:
    """ Return the author last name """
    return AUTHOR_LAST_NAME


def get_author_middle_name() -> str:
    """ Return the author middle name """
    return AUTHOR_MIDDLE_NAME

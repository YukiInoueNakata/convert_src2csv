import re


def is_number(text):
    return re.fullmatch("[0-9]+", text)


def is_start_and_end_time(text):
    s_t_time = re.compile(
        r"[0-9]{2}:[0-9]{2}:[0-9]{2},[0-9]+ --> [0-9]{2}:[0-9]{2}:[0-9]{2},[0-9]+"
    )
    return s_t_time.fullmatch(text)


def is_speaker(text):
    return re.fullmatch(r"SPEAKER_[0-9]+", text)


def is_caption(text):
    if is_number(text) or is_start_and_end_time(text) or is_speaker(text):
        return False
    elif len(text) == 0:
        return False
    else:
        return True


def teach_category(text):
    """This function return columns name.
    There are "number", "start_and_end_time" or "caption".

    Args:
        text (str): text of srt file.

    Returns:
        columns type: str
    """
    if is_number(text):
        return "number"
    elif is_start_and_end_time(text):
        return "start_and_end_time"
    elif is_caption(text):
        return "speaker_and_caption"
    else:
        return False

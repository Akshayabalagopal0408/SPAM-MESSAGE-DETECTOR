import re

def automata_detect(message):
    spam_patterns = [
        r"(free|win|prize|lottery)",
        r"(urgent|limited|offer|click|claim)",
        r"(http[s]?://|www\.)",
        r"congratulations"
    ]
    for pattern in spam_patterns:
        if re.search(pattern, message.lower()):
            return True
    return False

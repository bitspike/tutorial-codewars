import re

def validate_code(code):
    return re.match('^[123]', str(code)) is not None
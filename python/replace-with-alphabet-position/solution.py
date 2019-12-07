import re

def alphabet_position(text):
    alpha = {chr(x):str(x-96) for x in range(97,123)}
    return " ".join([alpha[x] for x in text.lower() if x in alpha])

import re

def calc(expression):
    import collections
    valid_chars = '@#$%^&*()_{}[]'

    def string_evaluation(strng,conditions):
        counts = collections.Counter(strng)
        return [evaluate(counts, condition) for condition in conditions]
        
    def evaluate(counts, condition):
        # Parse condition
        operantA = condition[0]
        operantB = condition[-1]
        operator = condition[1:-1]
        
        # Evaluate condition
        operantA = int(operantA) if operantA.isnumeric() else counts[operantA]
        operantB = int(operantB) if operantB.isnumeric() else counts[operantB]
        return eval( '%d %s %d' % (operantA, operator, operantB))
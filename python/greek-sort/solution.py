import re

letter_rank = {letter:rank for rank,letter in enumerate(('alpha', 'beta', 'gamma', 'delta', 'epsilon', 'zeta', 
    'eta', 'theta', 'iota', 'kappa', 'lambda', 'mu', 
    'nu', 'xi', 'omicron', 'pi', 'rho', 'sigma',
    'tau', 'upsilon', 'phi', 'chi', 'psi', 'omega'))}

def greek_comparator(lhs, rhs):
    return letter_rank[lhs] - letter_rank[rhs]



def highest_prod(array):
    m = len(array)
    n = len(array[0]) if m > 0 else 0
    max_prod = 0

    curr_prod = None
    prod_count = 0
    for i in range(m):
        for j in range(n):
            v = array[i][j]
            if v != 0:
                prod_count += 1
                if curr_prod is None:
                    curr_prod = v
                else:
                    curr_prod *= v
            if v == 0 or j+1 >= n:
                if prod_count > 1 and curr_prod > max_prod:
                    max_prod = curr_prod
                curr_prod = None
                prod_count = 0

    curr_prod = None
    prod_count = 0
    for j in range(n):
        for i in range(m):
            v = array[i][j]
            if v != 0:
                prod_count += 1
                if curr_prod is None:
                    curr_prod = v
                else:
                    curr_prod *= v
            if v == 0 or i+1 >= m:
                if prod_count > 1 and curr_prod > max_prod:
                    max_prod = curr_prod
                curr_prod = None
                prod_count = 0


    return max_prod
import functools
import time

precalcs = {}

def prodsum_dynamic(k):
    global precalcs
    if k in precalcs:
        return precalcs[k]
    n_set = [1] * k
    last_n = None
    last_check = None


    while True:
        # Increase set
        for i in range(k):
            if i == k-1 or n_set[i] < n_set[i+1]:
                n_set[i] += 1
                n_set[0:i] = [1]*i
                p = functools.reduce(lambda a,b: a*b, n_set)
                s = sum(n_set)
                if p > s: 
                    last_check = 1
                elif p < s: 
                    last_check = -1
                    break
                else: 
                    last_check = 0
                    break

        # Update last_n
        if last_check == 0:
            n = s
            if last_n is None:
                last_n = n
            else:
                last_n = min(last_n, n)
            # print(f'k: {k} N: {last_n} set: {n_set}')
        
        # Exit condition
        if i == k-1 and last_n and p >= last_n:
            # print(f'k: {k} N: {last_n}')
            precalcs[k] = last_n
            return last_n

def prodsum_recursive(prod, sum, factors, start, kmax, n_lst):
    k = prod - sum + factors  
    '''
    For this set of (prod, sum, factors) find the k-set whose prod number would 
    the N number. We are practically calculating the size (k) of the following
    set "{a1,a2,...,1,1,1,1}" 
                    ^-----^--< len() = factors
    Note that this set has product = prod and sum = (sum+factors).
    '''

    if k < kmax:
        if prod < n_lst[k]: 
            n_lst[k] = prod
        for i in range(start, 2*kmax//prod + 1):
            '''
            kmax//prod*2 + 1 : The upper value of this loop is defined through
            the following logic. 
                - In the body of this look we are going to calculate the next
                    prodcut number to be checked. This will be "prod*i"
                - Since the new products will be checked if they are N numbers.
                    There is no point to check products which are bigger than 
                    2*kmax (as explained in the comment of n_lst variable in 
                    productsum function)
                - So we have the following rule for the new products 
                    "(prod*i) <= 2*kmax" => i <= 2*kmax/prod (1)
                - But since we are dealing with integers rule (1) decomes
                    i < 2*kmax//prod + 1
            '''
            prodsum_recursive(prod*i, sum+i, factors+1, i, kmax, n_lst)



def productsum(n):
    # return sum({prodsum_dynamic(x) for x in range(2, n+1)})

    n += 1
    n_lst = [2*n] * n  
    # This is true because for every k-set the set {k, 2, 1, ..., 1}
    #                                                     ^-------^--< '1' * k-2
    # has a sum of 2*k and a product of 2*k.

    # But since we do not know if the sum-products in n_lst are minimal we will
    # try to minimize them in the following call.
    prodsum_recursive(
        prod=1,       # 1 is neutral operan for product
        sum=0,        # 0 is neutral operan for sum
        factors=0,    # We assume the initial values are for the 0-set
        start=2,      # Lower boundary from the definition of the problem
        kmax=n,       # Upper boundary from the definition of the problem
        n_lst=n_lst)  # Share the list with our N number to allow the function to edit it

    
    return sum(set(n_lst[2:])) # Eliminate duplicates and sum

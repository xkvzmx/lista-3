from scipy import special
import math

############## ZAD. 1 ################

def probability_binom(n, k, p):
    prob = 0
    count_mult = 0
    for i in range(k+1):
        prob += special.binom(n,i) * p**i * (1-p)**(n-i)
        count_mult += 3*n+2
    return (prob, count_mult)

def probability(n, k, p):
    prob = 0
    count_mult = 0
    ℯ = math.e
    λ = n*p
    const = ℯ**λ
    count_mult += int(λ)
    for i in range(k+1):
        prob += λ**i / math.factorial(i)
        count_mult += 2*i-1
    prob /= const
    count_mult += 1
    return (prob, count_mult)

############## ZAD. 2 ################

def ordinary_polynomial_value_calc(coeff, arg):
    
    count_mult, count_add = 0, 0
    value = 0
    tab_x = [1 for _ in coeff]
    for i in range(1, len(coeff)):
        tab_x[i] = tab_x[i-1] * arg
        count_mult += 1
    components = [tab_x[i] * coeff[i] for i in range(len(coeff))]
    count_mult += len(coeff)
    for i in range(len(coeff)):
        value += components[i]
        count_add += 1
        
    return value, count_mult, count_add


def smart_polynomial_value_calc(coeff, arg):
    
    coeff.reverse()
    value = coeff[0]
    count_mult, count_add = 0, 0
    for i in range(1,len(coeff)):
        value = value * arg + coeff[i]
        count_mult += 1
        count_add += 1

    return value, count_mult, count_add


############## ZAD. 3 ################

def counting_chars_without_ifs(filename):
    file_ref = open(filename, 'r')
    text = file_ref.read()
    char_count = {}
    for c in text:
        try:
            char_count[c] += 1
        except:
            char_count[c] = 1
    for i in [' ','\t','\n']: #usuń znaki białe
            try:
                char_count.pop(i)
            except:
                pass
    for i in range(65,91): #duże litery licz jako małe
        try:
            char_count[chr(i+32)] = char_count.get(chr(i)) + char_count.get(chr(i+32))
            char_count.pop(chr(i)) #usuń duże po kluczach ze słownika
        except:
            pass
    return char_count
'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''

# import re

def count_th(word, cache=0):
    
    n = len(word)

    if n <= 1:
           return cache

    if word[0] == "t":
        if word[1] == "h":
            return count_th(word[2:], cache + 1 )
        else:
            return count_th(word[1:], cache)
    else:
        return count_th(word[1:], cache)

    # instances = re.findall(word, 'th')
    

# count_th("")
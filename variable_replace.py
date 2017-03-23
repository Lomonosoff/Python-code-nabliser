import random
import string
import keyword


def what_to_do(text, i, do_something, reason):
    urgent = {'"', "'", '#', '\n'}
    if text[i] in urgent:
        if text[i] == '#':
            if do_something:
                do_something = False
                reason = '#'
        elif text[i] == '\n' and reason == '#':
            do_something = True
        elif text[i] == '"':
            if do_something:
                reason = '"'
                do_something = False
            elif not do_something and reason == '"':
                do_something = True
        elif text[i] == "'":
            if text[i:i+3] == "'''":
                if do_something:
                    do_something = False
                    reason = "'''"
                elif not do_something and reason == "'''":
                    do_something = True
            elif text[i:i+3] != "'":
                if do_something:
                    do_something = False
                    reason = "'"
                elif not do_something and reason == "'":
                    do_something = True
    return do_something, reason


def get_variables_info(text):
    special = set(string.punctuation) | {'\n', ' ', '\t', '\v'}
    keywords = set(keyword.kwlist) | {'self', 'other'}
    special.remove('_')
    info = {}
    text = ' ' + text
    do_something = True
    reason = None
    for i in range(len(text)):
        (do_something, reason) = what_to_do(text, i, do_something, reason)
        if do_something:
            if text[i] not in special and text[i-1] in special:
                ind = i
                end = i
                for j in range(i+1, len(text)):
                    if text[j] not in special:
                        end += 1
                    else:
                        var = text[ind:end + 1]
                        if (var in info and var not in keywords and not var.isdigit()
                                and not text[end+1] == '('):
                            info[var].add(ind - 1)
                        else:
                            if (var not in keywords and not var.isdigit()
                                    and not text[end+1] == '('):
                                info[var] = {ind - 1}
                        break
    return info


def get_random_var(var, used):
    a = random.choice([0, 1, 2])
    while True:
        newvar = var
        if a == 0:
            newvar = one_symbol()
        elif a == 1:
            newvar = upper_lower(var)
        elif a == 2:
            newvar = halfword(var)
        if newvar not in used:
            used.add(newvar)
            return newvar, used


def one_symbol():
    return random.choice(list('QWERTYUIPASDFGHJKLZXCVBNMqwertyuipasdfghjklzxcvbnm'))


def upper_lower(var):
    if var.islower():
        return var.upper()
    else:
        return var.lower()


def halfword(var):
        newvar = var[:(len(var)//2 + 1)]
        if newvar.isdigit():
            return one_symbol()
        else:
            return newvar


def permutatio(text, info):
    text = list(text)
    used = set()
    for var in info:
        newvar, used = get_random_var(var, used)
        for i in info[var]:
            if len(var) == len(newvar):
                text[i:i+len(var)] = list(newvar)
            else:
                new = list(newvar)
                dif = len(var) - len(new)
                for k in range(dif):
                    new.append('')
                text[i:i + len(new)] = new[:]
    return ''.join(text)

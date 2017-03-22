import random
import string
import pydoc
import keyword

def is_in_string(text, ind):
    r1 = text[:ind].count("'") % 2
    r2 = text[:ind].count('"') % 2
    r3 = text[:ind].count("'''") % 2
    if 1 in (r1, r2, r3):
        return True
    else:
        return False

def get_variables_info(text):
    special = set(string.punctuation)
    keywords = set(keyword.kwlist)
    for x in ({'\n', ' ', '\t', '\v'}):
        special.add(x)
    special.remove('_')
    info = {}
    text = ' ' + text
    for i in range(len(text)):
        if text[i] not in special and text[i-1] in special:
            ind = i
            end = i
            for j in range(i+1, len(text)):
                if text[j] not in special:
                    end += 1
                else:
                    try:
                        var = text[ind:end + 1]
                        Help = pydoc.render_doc(var, "Help on %s")
                        break
                    except:
                        var = text[ind:end + 1]
                        if var in info and var not in keywords and not var.isdigit() and not text[ind-1] == '.' and not text[end+1] == '(' and not is_in_string(text, ind):
                            info[var].add(ind - 1)
                        else:
                            if var not in keywords and not var.isdigit() and not text[ind-1] == '.' and not text[end+1] == '(' and not is_in_string(text, ind):
                                info[var] = {ind - 1}
                        break
    return info

def get_random_var(var):
    a = random.choice([0, 1, 2])
    if a == 0:
        return one_symbol()
    if a == 1:
        return upper_lower(var)
    if a == 2:
        return halfword(var)

def one_symbol():
    return random.choice(list('QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm'))

def upper_lower(var):
    if var.islower():
        return var.upper()
    else:
        return var.lower()

def halfword(var):
    return var[len(var)//2:]

def permutatio(text, info):
    text = list(text)
    for var in info:
        newar = get_random_var(var)
        for i in info[var]:
            if len(var) == len(newar):
                text[i:i+len(var)] = list(newar)
            else:
                new = list(newar)
                dif = len(var) - len(new)
                for k in range(dif):
                    new.append('')
                text[i:i + len(new)] = new[:]
    return ''.join(text)

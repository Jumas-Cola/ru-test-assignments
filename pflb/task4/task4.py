def check_compare(s1, s2):
    n = 0
    while n < len(s1):
        if s1[n] != s2[n]:
            if s2[n] == '*':
                s = s2[n + 1: s2.find('*', n + 1)]
                n = s1.rfind(s)
                if n < 0:
                    return False
                n += len(s)
            else:
                return False
        n += 1
    return True


str1 = 'aaabb'
str2 = '*a*bb*'


print(not str2.replace('*', '') or all((check_compare(str1, str2), check_compare(str1[::-1], str2[::-1]))))

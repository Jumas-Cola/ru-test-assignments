import sys
import pip

def import_or_install(package):
    try:
        __import__(package)
    except ImportError:
        pip.main(['install', package])  

import_or_install('sympy')
from sympy.solvers import solve
from sympy import Symbol

def set_quotes(s):
    s = ''.join([i + '"' if i.isalpha() and n + 1 < len(s) and not s[n + 1].isalpha() else i for n, i in enumerate(s)])
    return ''.join(['"' + i if i.isalpha() and n - 1 >= 0 and not s[n - 1].isalpha() else i for n, i in enumerate(s)])


def get_args(s):
    i = s.find('line')
    j = s[i:].find('}') + 1
    line = eval(s[i:i + j].translate(str.maketrans('{}', '[]'))[5:])
    
    i = s.find('sphere')
    j = s[i:].find('}') + 1
    sphere = eval(set_quotes(s[i:i + j][7:]))

    return {'sphere':sphere, 'line': line}



def get_collisions(param_dict):
    a = param_dict['sphere']['center'][0]
    b = param_dict['sphere']['center'][1]
    c = param_dict['sphere']['center'][2]
    R = param_dict['sphere']['radius']
    t = Symbol('t', real=True)
    point1 = param_dict['line'][0]
    point2 = param_dict['line'][1]
    x1, y1, z1 = point1[0], point1[1], point1[2]
    x2, y2, z2 = point2[0], point2[1], point2[2]
    
    x = (x2 - x1)*t + x1
    y = (y2 - y1)*t + y1
    z = (z2 - z1)*t + z1

    solitions = solve((x - a)**2 + (y - b)**2 + (z - c)**2 - R**2, t)
    
    if solitions:
        for sol in solitions:
            print((x2 - x1)*sol + x1, (y2 - y1)*sol + y1, (z2 - z1)*sol + z1)
    else:
        print('Коллизий не найдено')


def main():
    filepath = sys.argv[1]
    with open(filepath, encoding='utf8') as f:
        for line in f.readlines():
            get_collisions(get_args(line))

if __name__ == '__main__':
    """
        usage: task2.py <filepath>
    """
    main()
    

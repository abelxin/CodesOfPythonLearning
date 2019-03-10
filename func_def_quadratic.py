# -*- coding: utf-8 -*-

import math

def quadratic(a, b, c):
    if b**2 - 4*a*c >= 0:
        x1 = (-b + math.sqrt(b**2 - 4*a*c))/2*a
        x2 = (-b - math.sqrt(b**2 - 4*a*c))/2*a
        return x1,x2
    else:
        print('There is no RIGHT answer!\nPlease check your parameter!')
        return 
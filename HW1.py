# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 11:21:17 2021

@author: user
"""

"""
由系統亂數產生1-49之間6個不重複的整數，請遞增排序印出。
"""

import random

a=random.randint(1,50)
b=random.randint(1,50)
if a.count() == 0 and b.count() == 0:
    c=random.randint(1,50)
    if a.count() == 0 and b.count() == 0 and b.count() == 0:
        d=random.randint(1,50)
        if a.count() == 0 and b.count() == 0 and b.count() == 0 and b.count() == 0:
            e=random.randint(1,50)
            if a.count() == 0 and b.count() == 0 and b.count() == 0 and b.count() == 0 and b.count() == 0:
                f=random.randint(1,50)

print(a,b,c,d,e,f)

data = [a,b,c,d,e,f]
data.sort()
print('遞增排序:',data)
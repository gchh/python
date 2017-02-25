#!usr/bin/env python
#-- coding: utf-8 --
import os
def fine(pathx):
    for x in os.listdir(pathx):
        if os.path.isfile(os.path.join(pathx,x)) and target in x:
            print(os.path.basename(x),'=====>',pathx)
        elif os.path.isdir(os.path.join(pathx,x)):
            fine(os.path.join(pathx,x))
if __name__ == '__main__':
    target = input('input the searching str:')
    path = '.'
    fine(path)

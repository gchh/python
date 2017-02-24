#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'a greet somebody module '

__author__='gch'


def _private_1(name):
    print('Hello,%s'%name)

def _private_2(name):
    print('Hi,%s'%name)

def greeting():
    name=input('输入你的name:')
    if len(name)>3:
        return _private_1(name)
    else:
        return _private_2(name)

if __name__=='__main__':
    greeting()

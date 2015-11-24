#!/usr/bin/env python
#-*- encoding=utf-8 -*-

__author__="Alex Yean"
__date__="2015-10-24"

class Dict(dict):
    '''
    Simple dict but also support access as x.y style.

    #>>> d1 = Dict()
    #>>> d1['x'] = 100
    #>>> d1.x
    #100
    #>>> d1.y = 200
    #>>> d1['y']
    #200
    #>>> d2 = Dict(a=1, b=2, c='3')
    #>>> d2.c
    '''

    def __init__(self,**kw):
        super(Dict,self).__init__(**kw)

    def __getattr__(self,key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError("Dict Object has no attribute '%s'" % key)

    def __setattr(self,key,value):
        self[key]=value

if __name__=="__main__":
    import doctest
    doctest.testmod()

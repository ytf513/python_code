#!/usr/bin/env python
#-*- encoding=utf-8  -*-

import unittest
from mydict import Dict

class TestDict(unittest.TestCase):
    def test_init(self):
        d=Dict(a=1,b='test')
        self.assertEquals(d.a,1)
        self.assertEquals(d.b,'test')
        self.assertTrue(isinstance(d,dict))

    def test_key(self):
        d=Dict()
        d['key']='value'
        self.assertEquals(d.key,'value')

    def test_keyerror(self):
        d=Dict()
        with self.assertRaises(KeyError):
            value=d['empty'] 

if __name__=='__main__':
    unittest.main()

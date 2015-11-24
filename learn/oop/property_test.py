#!/usr/bin/env python
#-*- coding:utf-8 -*-

__author__="Alex Yean"
__date__='2015-10-22'

'@property的使用'

print "绑定属性时我们直接调用，虽然写起来简单，但是没办法做校验。为了限制该漏洞，可以用get/set方法"

class Student(object):
    def __init__(self,score=15):
        self.__score=score

    def get_score(self):
        return self.__score

    def set_score(self,score):
        if not isinstance(score,int):
            raise ValueError("score is not integer!")
        elif score<0 or score>100:
            raise ValueError("score is not in 1-100!")
        else:
            self.__score=score

a=Student()
print '__score属性的值a.get_score():',a.get_score()
a.set_score(30)
print '__score属性的值a.get_score():',a.get_score()

print "*"*40
#@property
class StudentN(object):
    @property
    def score(self):
        return self.__score
    @score.setter
    def score(self,score):
        if not isinstance(score,int):
            raise ValueError("score is not integer!")
        elif score<0 or score>100:
            raise ValueError("score is not in 1-100!")
        else:
            self.__score=score

b=StudentN()
b.score=5
print b.score

print '''除了装饰器之外，也可以用属性来设置。
area = property(___get_area, ___set_area,doc="""Gets or sets the area of the square.""")"
'''

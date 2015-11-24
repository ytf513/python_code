#!/usr/bin/env python
#-*- coding:utf-8 -*-

'oop 编程练习'
__author__='Alex Yean'
__date__='2015-10-22'

print "面向过程表示学生成绩，并打印成绩："
std1={'name':'bob','score':40}
print "%s：%s" % (std1['name'],std1['score'])

print "*"*40

print "oop的方法"
class Student(object):
    def __init__(self,name,score):
        self.name=name
        self.score=score
    
    def print_score(self):
        print "%s:%s" % (self.name,self.score)

    def __call__(self):
        print "my name is %s!" % (self.name)

std2=Student("bob2",50)
std2.print_score()	
std2.score=77
std2.print_score()
print "*"*40
print "和静态语言不同，python允许实例变量绑定任何数据，也就是两个实例变量所拥有的变量名可能不一样"
std2.age=13
print std2.age

print "类方法和普通方法的不同就是类方法第一个参数是self。起到了封装的作用"

print "*"*40
# 访问限制
print "外部代码可以正常的读取、修改实例的属性，为了控制权限可以："
print "在属性名称前面增加__，把其变为私有变量。但是仍然可以通过“_类名__属性名来访问”"

print "*"*40
#继承与多态

class Animal(object):
    def run(self):
        print "anmmal is running!"
    def run_three(self):
        self.run()
        self.run()
        self.run()

class Dog(Animal):
    def run(self):
        print "dog is running!"

class Cat(Animal):
    def run(self):
        print "cat is running!"

    def eat(self):
        print "cat is eating!"

animal=Animal()
dog=Dog()
cat=Cat()
animal.run()
dog.run()
cat.run()		
cat.eat()

print "*"*16,"多态","*"*16

def run_twice(aa):
    aa.run()
    aa.run()

run_twice(animal)
run_twice(Dog())
run_twice(Cat())
dog.run_three()
cat.run_three()
print type(cat)

print "*"*40
print "实例的属性可以自由的更改和访问，如何限制呢？"
print "定义class时，定义一个特殊的变量__slots__，来限制class能添加的属性"

__slots__=('name','age')

print "*"*40
print "为了使类能够实现多个分类，可以使用多重继承的功能。多重继承是mixin的一种常见设计。"
std2()
print std2.__repr__

print "*"*40
class Chain(object):
    def __init__(self,path=''):
        self._path=path

    def __getattr__(self,path):
        return Chain('%s/%s' % (self._path,path))

    def __str__(self):
        return self._path

print Chain().book.shell.python

print std2.__new__

#coding: utf-8
import os.path
import time


print "os.path.splitunc : ",
print os.path.splitunc('G:\child.of.light.hd')
"""
 os.path.splitunc(path) 
 把路径分割为挂载点和文件名
"""
print "os.path.ismount :",
print os.path.ismount('G:\child.of.light.hd')
""" 
os.path.ismount() 
指定路径是否存在且为一个挂载点，返回boolean
"""
print "os.path.abspath :",
print os.path.abspath('G:\child.of.light.hd')
print os.path.abspath('\Child of Light\_CommonRedist')

print "os.path.basename :",
print os.path.basename('G:\child.of.light.hd')
#返回文件路径的文件名部分

list=['G:\child.of.light.hd','G:\child.of.light.hd\Child of Light\_CommonRedist']
print "os.path.commonprefix :"
print os.path.commonprefix(list)
#返回共同的前缀

print "os.path.dirname :",
print os.path.dirname('G:\child.of.light.hd')

print "os.path.exists(path) :",
print os.path.exists('G:\child.of.light.hd')
print os.path.exists('D:\child.of.light.hd')



print "os.path.lexists(path) :",
print os.path.lexists('G:\child.of.light.hd')
print os.path.lexists('D:\child.of.light.hd')
#路径存在或者损坏都返回true

print "os.path.expanduser(path) :",
print os.path.expanduser('~\\name')
#把path中包含的"~"和"~user"转换成用户目录

print "os.path.expandvars(path) :",
print os.path.expandvars('D:\child.of.light.hd\${name}')
 #根据环境变量的值替换path中包含的”$name”和”${name}” ???

print "os.path.getatime(path) :",
print os.path.getatime('C:\Users\\asus\Desktop\python\\17.txt')
#返回上一次访问时间，浮点型

print "os.path.getmtime(path) :",
print os.path.getmtime('C:\Users\\asus\Desktop\python\\17.txt')
#返回上一次修改时间，浮点型

print "os.path.getctime(path) :",

print os.path.getctime('C:\Users\\asus\Desktop\python\\17.txt')
#返回值是炒年糕1970年1月1日算起的
print os.path.getctime('C:\Users\\asus\Desktop\python\\1.txt')


#转换为可理解形式
print time.ctime(os.path.getctime('C:\Users\\asus\Desktop\python\\1.txt'))
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 21:44:31 2019

@author: Kiran
"""

from os import path

def fileExists():

   print ("file exist:"+str(path.exists('Test.txt')))
   print ("File exists:" + str(path.exists('C:\logs\Test.txt')))
   print ("directory exists:" + str(path.exists('C:\logs')))

if __name__== "__main__":
   fileExists()
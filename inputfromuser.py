import sys
import random
import os
print("Say how you like your food")
food, temperature = input().split()
print('what is your name')
name = sys.stdin.readline()
print('what is your age')
age = sys.stdin.readline()
print('where do you stay')
home = input()

num1, num2 = input("do you like python: ").split()
print('Hello', name)
print('Your current age is', age)
print('Your current place of residence is', home)
print('you like your food when its', food)
print('\n')
print('and especially when its', temperature)
print("{} {}".format(num1, num2))


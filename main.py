from replit import clear
from art import *
def add(number1,number2):
  return number1+number2
def sub(number1,number2):
  return number1-number2
def mul(number1,number2):
  return number1*number2
def div(number1,number2):
  return number1/number2
operator_dict ={}
operator_dict["+"]=add
operator_dict["-"]=sub
operator_dict["*"]=mul
operator_dict["/"]=div

def calculator():
  print(logo)
  Flag=0
  while True:
    if Flag==0:
      number1 = float(input("enter a number "))
    for symbol in operator_dict:
      print(symbol)
    operator = input("enter the operation you wanna perform: ")
    number2 = float(input("enter the other number"))
    output= operator_dict[operator](number1,number2)
    print(output)
    continue_val = input('''do you wanna continue operations on same number type "y" if yes or else type"no"''')
    
    if continue_val=="y":
      number1 =output
      Flag=1
      
    else:
      clear()
      calculator()
    
calculator() 

  



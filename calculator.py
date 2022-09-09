def add(n1,n2):
  return n1+n2
def subtract(n1,n2):
  return n1-n2
def multiply(n1,n2):
  return n1*n2
def divide(n1,n2):
  return n1/n2
operations={"+":add,
           "-":subtract,
           "*":multiply,
           "/":divide}




def calculator():
  for i in operations:
    
     print(i)
  should_ontinue=True
  operand1=int(input("enter"))
  
  while should_ontinue:
    
    operand2=int(input("enter"))
    sign=input("enter operation")
    function=operations[sign]
    answer=function(operand1,operand2)
    print(f"{operand1}{sign}{operand2}={answer}")
    
    
    if input("enter y to continue and n for fresh")=="y":
      
      operand1=answer
    else :
      should_ontinue=False
      calculator()
calculator() 
    
    
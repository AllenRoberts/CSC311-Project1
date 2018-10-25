from Stack import ArrayStack

S = ArrayStack()
def postfixEval(x):
    for i in range(len(x)):
        if(x[i]>='0' and x[i]<='9'): #Checks if character in string is a number
            S.push(int(x[i]))
        elif x[i] == "+":   #Checks if character is a addition operator
            S.push(S.pop()+S.pop())  #Adds the two numbers most recently added to the stack
        elif x[i] == "-":   #Checks if character is a subtraction operator
            t = S.pop()     #Stored the top value in to to subtract correctly
            S.push(S.pop() - t)   #Subtracts the two numbers most recently added to the stack
        elif x[i] == "*":    #Checks if character is a multiplication operator
            S.push(S.pop()*S.pop())   #Multiplies the two numbers most recently added to the stack
        elif x[i] == "/":   #Checks if character is a Division operator
            t = S.pop()     #Stored the top value in to to divide correctly
            S.push(S.pop()/t)   #Divides the two numbers most recently added to the stack
    return S.top()  #returns the expressions answer

T = "12+3*6+23+/"
print(T+" =",postfixEval(T))







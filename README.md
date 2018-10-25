ReadMe file for Postfix evaluation using a Stack in Python 3.7.

== Description ==

Postfix notation is a way for an expression to be written without using parentheses. So (Ex1) operator (Ex2) in postfix notation is ex1 ex2 operator. This program was designed to be able to evaluate an expression after it has been reoriented into postfix notation using a stack. The program first checks if a character in the string is a number and if so it pushes it onto the stack. If the the character in the string is not a number the program then checks if it is any of the four operators. Once it finds an operator in the takes the two most recent values added to the stack and calculates them by the found operator. In the case of subtraction and division the most recently added value pushed onto the stack is stored in a temporary variable to divide or subtract it correctly from the value before it. Once the loop has finished the top value of the stack is returned which is the answer to the expression that was inputted.


== Instructions ==

Download the zip and extract and open PostfixNot.py and Stack.py in any python IDE.

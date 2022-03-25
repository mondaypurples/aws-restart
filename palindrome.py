"""
Palindrome
A palindrome is nothing but any number or a string which remains unaltered when reversed
"""

string=input(("Enter a string:"))
if(string==string[::-1]):
      print("The string is a palindrome")
else:
      print("Not a palindrome")
      
"""
Explanation: In the above program, first take input from the user (using input OR raw_input() method) to check for palindrome. 
Then using slice operation [start:end:step], check whether the string is reversed or not. 
Here, step value of -1 reverses a string. If yes, it prints a palindrome else, not a palindrome.
"""
      
n=int(input("Enter number:"))
temp=n
rev=0
while(n>0):
    dig=n%10
    rev=rev*10+dig
    n=n//10
if(temp==rev):
    print("The number is a palindrome!")
else:
    print("The number isn't a palindrome!")

"""
Program Explanation
1. User must first enter the value of the integer and store it in a variable.
2. The value of the integer is then stored in another temporary variable.
3. The while loop is used and the last digit of the number is obtained by using the modulus operator.
4. The last digit is then stored at the one’s place, second last at the ten’s place and so on.
5. The last digit is then removed by truly dividing the number with 10.
6. This loop terminates when the value of the number is 0.
7. The reverse of the number is then compared with the integer value stored in the temporary variable.
8. If both are equal, the number is a palindrome.
9. If both aren’t equal, the number isn’t a palindrome.
10. The final result is then printed.
"""
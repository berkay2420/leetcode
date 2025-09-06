# # num1 - (2^a + num2) - ..... -  (2^b + num2) = 0 --> this is the main equation
# # Let's say the number of minimum operations is "K". This means we are going to 
# # execute the main formula K times
# # num1 - (2^a + 2^b + ...... {K times}) - K * num2 = 0
# # (2^a + 2^b + ...... {K times}) = num1 - K * num2  Goal is the finding minimum K
# # This means for the K to work the result of num1 - K * num2 must be representable by powers of 2
# # For example if num1 - K * num2 = 5 this means K is either wrong or its impossible to make num1 0
# # Because 5 can't be representable with usin powers of 2

num1 = 3
num2 = -2
def makeIntegerZero(num1, num2):
  k = 1
  x = num1 - k*num2
  while x>=0:
    if bin(x).count("1") <= k <= x:
      ## bin(x).count("1") gives the minimum number of powers of 2 needed to represent x
      ## if the binary rep. of a number is bigger than K this means we can't get that number using K
      ## For example if the k=1 and the x=5, the binary rep of 5 is "101" there is two "ones". This means
      ## We need at least 2 powers of 2 to get this number but the K is 1 so this would'nt work we need
      ## to change the k   
      return k
    k += 1
    x = num1 - k * num2
  return - 1
  












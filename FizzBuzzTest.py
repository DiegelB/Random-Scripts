# fizz buzz. count 1-100 but multiples of 3 print fizz and multiples of 5 print buzz. both; print fizzbuzz
# i read online that many interviewers will do a fizzbuzz test and a lot of applicants will fail
# those people who fail should not be programmers 

def fizzBuzzLoop():
  for i in range(1,101):
    if (i % 3 == 0 and i % 5 == 0):
      print("FizzBuzz")
    elif (i % 5 == 0):
      print("Buzz")
    elif (i % 3 == 0):
      print("Fizz")
    else:
      print(i)
fizzBuzzLoop()

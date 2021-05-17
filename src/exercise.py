def main():
    #write your code below this line
    answer = greatest(2, 7, 9)
    print("Greatest: " + str(answer))

def greatest(number1, number2, number3):
  if (number1 > number2) and (number1 > number3):
    return number1
  elif (number2 > number1 ) and (number2 > number3):
    return number2
  else:
    return number3

if __name__ == '__main__':
    main()

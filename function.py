 #!/usr/bin/python

def sayHello( msg ):
  print ( str(type(msg )) + ' ==>' + str( msg ))

def doMathOperations (val1, val2):
    sum = val1 + val2
    diff = val1 - val2
    product = val1 * val2
    division = val1 / val2

    return sum, diff, product, division

def main():
    sayHello( 'Hello Python!' )
    sayHello( 10 )
    sayHello( 1.0 )

    num1 = 25
    num2 = 5

    result1, result2, result3, result4 = doMathOperations(num1, num2)

    print ( 'Addition of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(result1) )
    print ( 'Subtraction of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(result2) )
    print ( 'Multiplication of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(result3) )
    print ( 'Division of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(result4) )

main()     

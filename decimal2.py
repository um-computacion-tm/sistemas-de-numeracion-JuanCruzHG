import unittest
from binario import binario2hexadecimal, binario2octal


def decimal2binario(decimal):
    decimal = int(decimal)
    final = ""
    while decimal >= 2:
        final = final + str(decimal%2)
        decimal = decimal//2
    final = final + str(decimal)
    final = final[:: -1]
    return(final)

def decimal2hexadecimal(decimal):
   binario = decimal2binario(decimal)
   return(binario2hexadecimal(binario))

def decimal2octal(decimal):
   binario = decimal2binario(decimal)
   return(binario2octal(binario))

if __name__ == '__main__':
    unittest.main()
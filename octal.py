import unittest
from binario import  binario2decimal, binario2hexadecimal
DiccionarioOctal = {
    '0' : "000",
    '1' : "001",
    '2' : "010",
    '3' : "011",
    '4' : "100",
    '5' : "101",
    '6' : "110",
    '7' : "111",
}

def octal2binario(octa):
    octal = ""
    octa = str(octa)
    for digito in octa:
      octal += str(DiccionarioOctal[digito])
    return(octal)

def octal2decimal(octa):
   binario = octal2binario(octa)
   total=(binario2decimal(binario))
   return(total)

def octal2hexadecimal(octa):
   binario = octal2binario(octa)
   final=(binario2hexadecimal(binario))
   return(final)

if __name__ == '__main__':
    unittest.main()
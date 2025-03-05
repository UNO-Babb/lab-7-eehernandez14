from NumberTests import isPrime
from NumberTests import getFactor

def main():
  number = 13195
  factors = getFactor(number)
  print(factors)

  for f in factors:
    if isPrime(f):
      print(f)
if __name__ == '__main__':
  main()
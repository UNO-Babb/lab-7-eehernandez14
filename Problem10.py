from NumberTests import isPrime
from NumberTests import getFactor

def sumPrime(limit):
  total = 0 
  for number in range(2, limit):
    if isPrime(number):
      total += number
  return total
def main():
  number = 10
  limit = 2_000_000
  total_sum = sumPrime(limit)
  print(total_sum)
  
if __name__ == '__main__':
  main()
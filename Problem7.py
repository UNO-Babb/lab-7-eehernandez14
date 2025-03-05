from NumberTests import isPrime
from NumberTests import isEven

def main():
    count = 0
    num = 1
    while count < 10001:
       num += 1
       if isPrime(num):
          count += 1
    print(count)
   
if __name__ == '__main__':
  main()
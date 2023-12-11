def isPrime(n):
  if n == 2 or n == 3:
    return True
  if n == 1 or n % 2 == 0 or n % 3 == 0:
    return False
  i = 5
  w = 2
  while i*i <= n:
    if n % i == 0:
      return False
    i += w
    w = 6-w
  return True
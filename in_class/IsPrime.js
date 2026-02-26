function isPrime(n) {
  if (n <= 1) {
    return false;
  }
  if (n <= 3) {
    return true;
  }

  if (n % 2 === 0 || n % 3 === 0) {
    return false;
  }

  for (let i = 5; i * i < n; i += 6) {
    if (n % i === 0 || (n + 2) % i === 0) {
      return false;
    }
  }

  return true;
}

tests = [1, 2, 3, 4, 7, 8, 9, 11, 12, 14, 95959];
for (test of tests) {
  console.log(`${test} ${isPrime(test) ? "is prime" : "is not prime"}.`);
}

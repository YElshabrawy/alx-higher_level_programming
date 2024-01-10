#!/usr/bin/node
const fact = (n) => {
  if (!n) return 1;
  return fact(n - 1) * n;
};

console.log(fact(parseInt(process.argv[2])));

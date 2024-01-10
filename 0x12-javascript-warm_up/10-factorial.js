#!/usr/bin/node
function fact (n) {
  if (!n) return 1;
  return fact(n - 1) * n;
}

console.log(fact(parseInt(process.argv[2])));

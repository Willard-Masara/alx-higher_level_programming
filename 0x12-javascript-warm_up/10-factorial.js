#!/usr/bin/node
const arg = process.argv[2];
function factorial(n) {
    if (isNaN(n)) {
        return 1;
    }
    n = parseInt(n);
    if (n === 0 || n === 1) {
        return 1;
    } else {
        return n * factorial(n - 1);
    }
}
const result = factorial(arg);
console.log(result);

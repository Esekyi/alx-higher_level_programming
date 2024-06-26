#!/usr/bin/node

const args = process.argv;
const integer = parseInt(args[2]);

function factorial (num) {
  if (isNaN(num) || num <= 1) {
    return 1;
  }
  return num * factorial(num - 1);
}

console.log(factorial(integer));

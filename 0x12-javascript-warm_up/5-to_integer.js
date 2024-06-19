#!/usr/bin/node

const args = process.argv;
const toInteger = parseInt(args[2]);

if (toInteger) {
  console.log(`My number: ${toInteger}`);
} else {
  console.log('Not a number');
}

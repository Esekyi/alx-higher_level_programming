#!/usr/bin/node

const args = process.argv;
const phrase = 'C is fun';

if (args[2] === undefined) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < args[2]; i++) {
    console.log(phrase);
  }
}

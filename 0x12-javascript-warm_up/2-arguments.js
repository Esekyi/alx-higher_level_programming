#!/usr/bin/node
const args = process.argv;
const numArgs = args.length;

if (numArgs <= 0) {
  console.log('No argument');
} else if (numArgs === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}

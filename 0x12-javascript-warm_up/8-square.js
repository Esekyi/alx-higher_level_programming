#!/usr/bin/node

const args = process.argv;

if (args[2] === undefined || (isNaN(args[2])) || args[2] < 0) {
  console.log('Missing size');
} else {
  for (let i = 0; i < args[2]; i++) {
    console.log('X'.repeat(args[2]));
  }
}

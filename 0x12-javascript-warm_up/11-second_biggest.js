#!/usr/bin/env node

const args = process.argv.slice(2).map(Number);

if (args.length <= 2) {
  console.log(0);
} else {
  const setArgs = [...new Set(args)];
  setArgs.sort((a, b) => b - a);
  console.log(setArgs[1]);
}

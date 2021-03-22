#!/usr/bin/node
const arg = process.argv[2];
if (arg == null) {
  console.log('No arguments');
} else {
  console.log(arg);
}

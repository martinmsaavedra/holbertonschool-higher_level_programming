#!/usr/bin/node
const arg = process.argv[2];
if (isNaN(arg) === true) {
  console.log('Not a Number');
} else {
  const res = parseInt(arg);
  console.log('My number: ' + res);
}

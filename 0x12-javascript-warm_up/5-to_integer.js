#!/usr/bin/node
const arg = process.argv[2];
const res = parseInt(arg);
if (isNaN(res) === true) {
  console.log('Not a Number');
} else {
  console.log('My number: ' + res);
}

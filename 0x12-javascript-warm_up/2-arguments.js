#!/usr/bin/node
const lenArr = process.argv.length;
if (lenArr === 2) {
  console.log('No argument');
} else if (lenArr === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}

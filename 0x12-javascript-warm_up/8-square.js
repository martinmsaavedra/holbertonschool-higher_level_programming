#!/usr/bin/node
const size = parseInt(process.argv[2]);
if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (let x = 0; x < size; x++) {
    let x = '';
    for (let y = 0; y < size; y++) x += 'X';
    console.log(x);
  }
}

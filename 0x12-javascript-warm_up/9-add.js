#!/usr/bin/node

function add (a, b) {
  if (isNaN(a) || isNaN(b)) { return NaN; }
  return parseInt(a) + parseInt(b);
}

const suma = add(process.argv[2], process.argv[3]);
console.log(suma);

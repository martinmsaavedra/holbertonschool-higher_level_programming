#!/usr/bin/node
const dict = require('./101-data').dict;
newDict = {};
for (const key in dict) {
  val = dict[key];
  if (newDict[val] === undefined) {
    newDict[val] = [key];
  } else {
    newDict[val].push(key);
  }
}
console.log(newDict);

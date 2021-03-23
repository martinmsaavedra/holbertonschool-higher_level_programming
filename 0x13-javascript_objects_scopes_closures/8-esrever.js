#!/usr/bin/node
exports.esrever = function (list) {
  const arr = [];
  const len = list.length - 1;
  for (let i = len; i >= 0; i--) {
    arr.push(list[i]);
  }
  return (arr);
};

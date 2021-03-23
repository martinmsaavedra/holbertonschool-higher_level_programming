#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let occurrences = 0;
  list.forEach(element => {
    if (element === searchElement) {
      occurrences += 1;
    }
  });
  return occurrences;
};

#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let nb_occurrences = 0;
  for (let i = 0; i < list.length; i++) {
    if (searchElement === list[i]) {
      nb_occurrences++;
    }
  }
  return nb_occurrences;
};

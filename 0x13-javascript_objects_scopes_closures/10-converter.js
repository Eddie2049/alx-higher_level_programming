#!/usr/bin/node
exports.converter = function (base) {
  // function that converts a no. from base 10 to another base passed as argument.
  return function (num) {
    return num.toString(base);
  };
};

#!/usr/bin/node
exports.esrever = function (list) {
  return list.reduceRight(function (array, crnt) {
    array.push(crnt);
    return array;
  }, []);
};

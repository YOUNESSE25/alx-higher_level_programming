#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  return list.reduce((cont, crnt) => crnt === searchElement ? cont + 1 : cont, 0);
};

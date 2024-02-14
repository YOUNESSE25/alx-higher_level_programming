#!/usr/bin/node
const dict = require('./101-data').dict;

const tList = Object.entries(dict);
const valus = Object.values(dict);
const valusUniq = [...new Set(valus)];
const nDict = {};
for (const m in valusUniq) {
  const List = [];
  for (const n in tList) {
    if (tList[n][1] === valusUniq[m]) {
      List.unshift(tList[n][0]);
    }
  }
  nDict[valusUniq[m]] = List;
}
console.log(nDict);

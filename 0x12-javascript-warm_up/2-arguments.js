#!/usr/bin/node
const conteur = process.argv.length;
console.log(conteur === 2 ? 'No argument' : conteur === 3 ? 'Argument found' : 'Arguments found');

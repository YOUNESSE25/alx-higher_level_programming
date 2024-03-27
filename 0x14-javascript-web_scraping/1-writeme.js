#!/usr/bin/node

const fs = require('fs');
const f = process.argv[2];
const s = process.argv[3];
fs.writeFile(f, s, 'utf-8', function (err) {
  if (err) console.log(err);
});

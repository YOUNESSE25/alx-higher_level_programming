#!/usr/bin/node

const req = require('request');
const url = process.argv[2];
req(url, function (err, response) {
  if (err) {
    console.log(err);
  } else {
    console.log('code: ' + response.statusCode);
  }
});

#!/usr/bin/node
const req = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
let def = {};
req(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    const n = JSON.parse(body);
    n.characters.forEach(function (item, index, array) {
      req(item, function (error, response, content) {
        if (error) {
          console.log(error);
        } else {
          def = JSON.parse(content);
          console.log(def.name);
        }
      });
    });
  }
});

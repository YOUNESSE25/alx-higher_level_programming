#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
let def = {};
request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    const n = JSON.parse(body);
    n.characters.forEach(function (item, index, array) {
      request(item, function (error, response, content) {
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

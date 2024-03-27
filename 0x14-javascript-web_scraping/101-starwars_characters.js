#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
request(url, function (err, response, body) {
  if (!err) {
    const characters = JSON.parse(body).characters;
    Characters_print(characters, 0);
  }
});

function Characters_print (characters, indx) {
  request(characters[indx], function (err, response, body) {
    if (!err) {
      console.log(JSON.parse(body).name);
      if (indx + 1 < characters.length) {
        Characters_print(characters, indx + 1);
      }
    }
  });
}

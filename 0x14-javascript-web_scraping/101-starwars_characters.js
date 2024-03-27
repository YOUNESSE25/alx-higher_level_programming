#!/usr/bin/node
const req = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
req(url, function (err, response, body) {
  if (!err) {
    const characters = JSON.parse(body).characters;
    Characters_print(characters, 0);
  }
});

function Characters_print (characters, index) {
  req(characters[index], function (error, response, body) {
    if (!error) {
      console.log(JSON.parse(body).name);
      if (index + 1 < characters.length) {
        Characters_print(characters, index + 1);
      }
    }
  });
}

#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

function characters_printer (characters, idx) {
  request(characters[index], function (error, response, body) {
    if (!error) {
      console.log(JSON.parse(body).name);
      if (idx + 1 < characters.length) {
        characters_printer(characters, idx + 1);
      }
    }
  });
}
request(url, function (err, response, body) {
  if (!err) {
    const characters = JSON.parse(body).characters;
    characters_printer(characters, 0);
  }
});

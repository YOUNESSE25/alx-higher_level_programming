#!/usr/bin/node

const req = require('request');
const url = process.argv[2];
req(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    const films = JSON.parse(body).results;
    let cont = 0;
    for (const filmIndex in films) {
      const Charsfilm = films[filmIndex].characters;
      for (const Indexchar in Charsfilm) {
        if (Charsfilm[Indexchar].includes('18')) {
          cont++;
        }
      }
    }
    console.log(cont);
  } else {
    console.log('An error occured. Status code: ' + response.statusCode);
  }
});

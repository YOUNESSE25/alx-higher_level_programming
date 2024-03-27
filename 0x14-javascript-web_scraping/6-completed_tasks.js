#!/usr/bin/node
const req = require('request');
req(process.argv[2], function (err, response, body) {
  if (!err) {
    const TODOS = JSON.parse(body);
    const FINISH = {};
    TODOS.forEach((TODO) => {
      if (TODO.FINISH && FINISH[TODO.userId] === undefined) {
        FINISH[TODO.userId] = 1;
      } else if (TODO.FINISH) {
        FINISH[TODO.userId] += 1;
      }
    });
    console.log(FINISH);
  }
});

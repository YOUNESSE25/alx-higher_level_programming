#!/usr/bin/node
const req = require('request');
req(process.argv[2], function (err, response, body) {
  if (!err) {
    const TODOS = JSON.parse(body);
    const completed = {};
    TODOS.forEach((TODO) => {
      if (TODO.completed && completed[TODO.userId] === undefined) {
        completed[TODO.userId] = 1;
      } else if (TODO.completed) {
        completed[TODO.userId] += 1;
      }
    });
    console.log(completed);
  }
});

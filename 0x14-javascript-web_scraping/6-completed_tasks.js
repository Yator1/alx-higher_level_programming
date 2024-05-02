#!/usr/bin/node

/*
 * a script that computes the number of tasks completed by user id.
 */

const request = require('request');

const url = process.argv[2];

request.get(url, (error, response, body) => {
  if (error) {
    return console.log(error);
  } else {
    const data = JSON.parse(body);
    const dict = {};
    for (const value of data) {
      if (value.completed) {
        dict[value.userId] = (dict[value.userId] || 0) + 1;
      }
    }
    console.log(dict);
  }
});

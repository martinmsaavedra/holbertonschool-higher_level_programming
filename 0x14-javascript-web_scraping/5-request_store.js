#!/usr/bin/node

const request = require('request');
const fs = require('fs');

const url = process.argv[2];
request(url, function (error, response, body) {
  if (error) {
    console.error(error);
  }
  fs.writeFile(process.argv[3], body, 'utf-8', function (error) {
    if (error) throw error;
  });
});

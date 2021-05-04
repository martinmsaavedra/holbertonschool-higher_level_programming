#!/usr/bin/node


const request = require('request');
const url = process.argv[2].slice(0,-5) + "people/18";
request(url, function (error, response, body) {
  if (error) {
    console.error(error);
  }
  array = JSON.parse(body).films;
  console.log(array.length)
  
});


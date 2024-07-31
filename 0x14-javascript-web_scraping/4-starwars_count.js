#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
const wedgeAntilles = 18;
const characterUrl = 'https://swapi-api.alx-tools.com/api/people/1/';

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {

  }
});

#!/usr/bin/node

const request = require('request');
const movieID = process.argv[2];
const endpoint = 'https://swapi-api.alx-tools.com/api/films/';
const url = endpoint + movieID;

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const data = JSON.parse(body);
    console.log(data.title);
  }
});

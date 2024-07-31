#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
const wedgeAntilles = 18;
// const characterUrl = 'https://swapi-api.alx-tools.com/api/people/1/';

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const data = JSON.parse(body);
    const movies = data.results;
    const count = movies.filter(movie =>
      movie.characters.some(character => character.includes(`/api/people/${wedgeAntilles}/`)));
    console.log(count.length);
  }
});

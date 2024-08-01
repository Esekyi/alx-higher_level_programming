#!/usr/bin/env node

const request = require('request');
const movieId = process.argv[2];
const baseUrl = 'https://swapi-api.alx-tools.com/api/';

const movieUrl = `${baseUrl}films/${movieId}`;

request(movieUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const movieData = JSON.parse(body);
    const characters = movieData.characters;
    characters.forEach((characterUrl) => {
      request(characterUrl, (error, response, body) => {
        if (error) {
          console.error(error);
          return;
        }
        const characterData = JSON.parse(body);
        console.log(characterData.name);
      });
    });
  }
});

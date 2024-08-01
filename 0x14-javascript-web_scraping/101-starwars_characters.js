#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const baseUrl = 'https://swapi-api.alx-tools.com/api/';

const movieUrl = `${baseUrl}films/${movieId}`;

request(movieUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  }
  const movieData = JSON.parse(body);
  const characters = movieData.characters;
  const fetchCharacter = (url, callback) => {
    request(url, (error, response, body) => {
      if (error) {
        console.error(error);
        return;
      }

      const characterData = JSON.parse(body);
      callback(characterData.name);
    });
  };
  const printCharacters = (index) => {
    if (index >= characters.length) return;
    fetchCharacter(characters[index], (name) => {
      console.log(name);
      printCharacters(index + 1);
    });
  };
  printCharacters(0);
});

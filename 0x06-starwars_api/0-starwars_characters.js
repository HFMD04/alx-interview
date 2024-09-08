#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const url = `https://swapi.dev/api/films/${movieId}/`;

request(url, async (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  }
  const movie = JSON.parse(body);
  const characters = movie.characters;
  for (let i = 0; i < characters.length; i += 1) {
    await new Promise((resolve, reject) => {
      request(characters[i], (error, response, body) => {
        if (error) {
          console.log(error);
        }
        console.log(JSON.parse(body).name);
        resolve();
      });
    });
  }
});

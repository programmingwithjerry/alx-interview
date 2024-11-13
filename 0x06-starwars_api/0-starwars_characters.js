#!/usr/bin/node

const request = require('request');
const API_URL = 'https://swapi-api.hbtn.io/api';

if (process.argv.length > 2) {
  const movieId = process.argv[2];
  
  // Request the movie details from the SWAPI /films endpoint
  request(`${API_URL}/films/${movieId}/`, (err, _, body) => {
    if (err) {
      console.error(err);
      return;
    }

    const charactersURL = JSON.parse(body).characters;

    // Map each character URL to a promise that retrieves the character's name
    const characterPromises = charactersURL.map(url => 
      new Promise((resolve, reject) => {
        request(url, (error, __, characterBody) => {
          if (error) {
            reject(error);
          } else {
            resolve(JSON.parse(characterBody).name);
          }
        });
      })
    );

    // Resolve all promises and print each character's name in order
    Promise.all(characterPromises)
      .then(names => console.log(names.join('\n')))
      .catch(err => console.error(err));
  });
}

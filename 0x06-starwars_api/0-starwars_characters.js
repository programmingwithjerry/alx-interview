#!/usr/bin/node

const request = require('request'); // Import the request module to make HTTP requests
const API_BASE_URL = 'https://swapi-api.hbtn.io/api'; // Define the base URL for the Star Wars API

// Check if a Movie ID argument was provided
if (process.argv.length > 2) {
  const movieId = process.argv[2]; // The movie ID passed as a command-line argument

  // Make a request to the API for the specified movie
  request(`${API_BASE_URL}/films/${movieId}/`, (error, _, responseBody) => {
    if (error) {
      console.error(error); // Log any error that occurs during the movie request
      return;
    }

    // Parse the response to get the array of character URLs
    const characterUrls = JSON.parse(responseBody).characters;

    // Map each character URL to a Promise that fetches the character's name
    const characterNamePromises = characterUrls.map(
      url => new Promise((resolve, reject) => {
        request(url, (characterRequestError, __, characterResponseBody) => {
          if (characterRequestError) {
            reject(characterRequestError); // Reject the promise if there's an error
          } else {
            const characterName = JSON.parse(characterResponseBody).name;
            resolve(characterName); // Resolve the promise with the character's name
          }
        });
      })
    );

    // Wait until all character names are fetched, then print each name
    Promise.all(characterNamePromises)
      .then(characterNames => console.log(characterNames.join('\n'))) // Print each character's name on a new line
      .catch(fetchError => console.error(fetchError)); // Log any error in fetching character names
  });
}

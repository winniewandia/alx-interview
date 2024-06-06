#!/usr/bin/node

const request = require('request');
const util = require('util');
const requestPromise = util.promisify(request); // Convert callback-based request to return a Promise
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

async function getCharactersInOrder (url) {
  const response = await requestPromise(url);
  const characters = JSON.parse(response.body).characters;

  for (const characterUrl of characters) {
    const characterResponse = await requestPromise(characterUrl);
    console.log(JSON.parse(characterResponse.body).name);
  }
}

getCharactersInOrder(url).catch(console.error);

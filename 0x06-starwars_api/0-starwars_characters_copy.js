#!/usr/bin/node
/*
Write a script that prints all characters of a Star Wars movie:

The first positional argument passed is the Movie
ID - example: 3 = “Return of the Jedi”
Display one character name per line in the same order as the “characters”
list in the /films/ endpoint
You must use the Star wars API
You must use the bent module
*/

const bent = require('bent');
const getJSON = bent('json');
const getBuffer = bent('buffer')
const fs = require('fs')

const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

async function getCharacter (charactersUrl) {
  const character = await getJSON(charactersUrl);
  return character.name;
}

async function main () {
  const characters = await getJSON(url);
  for (const character of characters.characters) {
    console.log(await getCharacter(character));
  }
}

main();

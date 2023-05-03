# 0x06-starwars_api

## Description
This project is about using an API to get information about Star Wars characters.

## General
- How to use NodeJS request module
- How to read and write a file using fs module
- How to use request module API
- How to use Star Wars API
- How to export a module
- How to import a module
- How to use ```async``` and ```await``` in NodeJS

## Tasks
### 0. Star Wars Characters

Write a script that prints all characters of a Star Wars movie:

- The first positional argument passed is the Movie ID - example: 3 = “Return of the Jedi”

- Display one character name per line in the same order as the “characters” list in the /films/ endpoint

- You must use the Star wars API

- You must use the request module

```sh
$ ./0-starwars_characters.js 3
Darth Vader
R2-D2
Luke Skywalker
Han Solo
Leia Organa
Chewbacca
Palpatine
Obi-Wan Kenobi
Jabba Desilijic Tiure
Wedge Antilles
Yoda
Boba Fett
Ackbar
Arvel Crynyd
Mon Mothma
Nien Nunb
Wicket Systri Warrick
Bib Fortuna
C-3PO
Lando Calrissian
```
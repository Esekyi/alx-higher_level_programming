#!/usr/bin/node

const dict = require('./101-data').dict;

const occurrencesById = {};

for (const [userId, occurrence] of Object.entries(dict)) {
  if (!occurrencesById[occurrence]) {
    occurrencesById[occurrence] = [];
  }
  occurrencesById[occurrence].push(userId);
}

console.log(occurrencesById);

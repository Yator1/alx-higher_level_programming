#!/usr/bin/node

/*
 * A script that imports a dictionary of occurrences by user id and
 * computes a dictionary of user ids by occurrence.
 */
const { dict } = require('./101-data');

const newUserDict = {};

for (const userId in dict) {
  const occurrences = dict[userId];
  if (!newUserDict[occurrences]) {
    newUserDict[occurrences] = [userId];
  } else {
    newUserDict[occurrences].push(userId);
  }
}

console.log(newUserDict);

#!/usr/bin/node

/*
 * Script that searches for the second biggest integer in the list of arguments
 */
const { argv } = require('process');

function secondLargest (nums) {
  if (nums.length <= 1) {
    return (0);
  }

  const largest = Math.max(...nums);
  let secondLargestNo = -Infinity;

  for (const no of nums) {
    if (no !== largest && no > secondLargestNo) {
      secondLargestNo = no;
    }
  }

  return (secondLargestNo);
}

const argumentsList = argv.slice(2).map(Number);
const secondLargestInList = secondLargest(argumentsList);
console.log(secondLargestInList);

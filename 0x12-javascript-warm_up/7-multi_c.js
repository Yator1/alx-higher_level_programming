#!/usr/bin/node

// Script that prints x times 'C is fun'
const { argv } = require('process');

if (!argv[2] || isNaN(argv[2])) {
  console.log('Missing number of occurrences');
} else {
  let x = Number(argv[2]);
  while (x > 0) {
    console.log('C is fun');
    x--;
  }
}

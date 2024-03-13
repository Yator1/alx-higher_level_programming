#!/usr/bin/node

/*
 * Script that prints a message depending on the number of arguments
 * Prints either no arguments or argument found
 */
const { argv } = require('process');

const argLen = argv.length;

if (argLen <= 2) {
  console.log('No argument');
} else if (argLen === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}

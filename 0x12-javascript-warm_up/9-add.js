#!/usr/bin/node

/*
 * Script that prints the addition of 2 integers
 * 1st argument is 1st int and
 * 2nd argument is the 2nd int
 */
const { argv } = require('process');

function add (a, b) {
  return (a + b);
}

const sum1 = add(Number(argv[2]), Number(argv[3]));
console.log(sum1);

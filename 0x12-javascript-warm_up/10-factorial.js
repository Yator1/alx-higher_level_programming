#!/usr/bin/node

// Script that computes the factorial of a number
const { argv } = require('process');

function factorial (No) {
  if (isNaN(No)) {
    return (1);
  } else if (No <= 1) {
    return (1);
  } else {
    return (No * factorial(No - 1));
  }
}
const no = Number(argv[2]);
const x = factorial(no);
console.log(x);

#!/usr/bin/node

/*
 * A script that prints a square
 * 1st arg is the size,
 * if cannot be converted to int it prints 'Missing size',
 * print the square using character x
 */
const { argv } = require('process');

if (!argv[2] || isNaN(argv[2])) {
  console.log('Missing size');
} else {
  const numberOfX = Number(argv[2]);

  for (let i = 0; i < numberOfX; i++) {
    console.log('X'.repeat(numberOfX));
  }
}

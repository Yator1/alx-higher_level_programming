#!/usr/bin/node

/*
 * A script that prints three lines using an array of strings and a loop
 */

const array1 = ['C is fun', 'Python is cool', 'JavaScript is amazing'];

let i = 0;
while (i < array1.length) {
  console.log(array1[i]);
  i++;
}

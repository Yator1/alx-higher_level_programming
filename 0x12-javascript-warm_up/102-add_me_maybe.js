#!/usr/bin/node

// A function that increments and calls a function

function addMeMaybe (number, theFunction) {
  // Increment the number
  number++;

  // Call function with the incremented number as an argument
  theFunction(number);
}

// Making the function visible from outside
module.exports.addMeMaybe = addMeMaybe;

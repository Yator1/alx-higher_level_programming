#!/usr/bin/node

// A function that increments and calls a function

function addMeMaybe (number, theFunction) {
	// Increment the number
	number++;

	// calling the function with incremenred number
	theFunction(number);
}

// make it visible from outside
module.exports.addMeMaybe = addMeMaybe;

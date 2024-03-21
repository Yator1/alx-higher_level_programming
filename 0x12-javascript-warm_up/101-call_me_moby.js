#!/usr/bin/node

// a function that executes x times a function.

function callMeMoby (x, theFunction) {
  for (let i = 0; i < x; i++) {
    theFunction();
  }
}

// making the function visible
module.exports.callMeMoby = callMeMoby;

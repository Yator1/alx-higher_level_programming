#!/usr/bin/node

/*
 * A script that reads and prints contents of a file
 */

const fs = require('fs');

fs.readFile(process.argv[2], 'utf8', (err, data) => {
	if (err) {
		return console.log(err);
	}
	console.log(data);
});

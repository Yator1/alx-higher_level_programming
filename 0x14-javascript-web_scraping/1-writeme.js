#!/usr/bin/node

/*
 * A script that writes content to a file
 */

const fs = require('fs');

const content = process.argv[3];

fs.writeFile(process.argv[2], content, 'utf8', (err) => {
	if (err) {
		return console.log(err);
	}
});

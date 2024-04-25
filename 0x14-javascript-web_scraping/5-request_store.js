#!/usr/bin/node

/*
 * a script that gets the contents of a webpage and stores it in a file.
 */

const fs = require('fs');
const request = require('request');

url = process.argv[2];
file = process.argv[3];

request.get(url, (error, response, body) => {
	if (error) {
		console.log(error);
		return;
	}

	fs.writeFile(file, body, 'utf-8', err => {
		if (err) {
			console.log(err);
		}
	});
});

#!/usr/bin/node

/*
 * A script that displays the status code of a GET URL
 */

const request = require('request');
const URL = process.argv[2];

request(URL, function(err, response, body) {
	if (err) {
		return console.log(err);
	}

	console.log('code: ' + response.statusCode);
});

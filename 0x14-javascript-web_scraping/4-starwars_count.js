#!/usr/bin/node

const request = require('request');
const URL = process.argv[2];


request(URL, function(err, response, body) {
	if (err) {
		return console.log(err);
	} else {
		let moviesWithWedge = 0;
		const data = JSON.parse(body);
		for (const val of data.results) {
			for (const val2 of val.characters) {
				if (val2.search('18/') > 0) {
					moviesWithWedge++;
				}
			}
		}
		console.log(moviesWithWedge);
	}
});

#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const data = JSON.parse(body);
    const completedTasks = {};
	  data.forEach((item) => {
      if (item.completed) {
		  if (!completedTasks[item.userId]) {
		    completedTasks[item.userId] = 0;
		  }
        completedTasks[item.userId]++;
      }
    });
    console.log(completedTasks);
  }
});

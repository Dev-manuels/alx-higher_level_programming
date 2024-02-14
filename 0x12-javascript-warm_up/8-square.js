#!/usr/bin/node
const number = Number(process.argv[2]);
if (isNaN(number)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < number; i++) {
    let row = '';
    for (let j = 0; j <number; j++) {
      row += 'x';
    }
    console.log(row);
  }
}

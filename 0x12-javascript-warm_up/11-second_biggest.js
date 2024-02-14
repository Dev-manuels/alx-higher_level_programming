#!/usr/bin/node

const maxLength = process.argv.length;
if (maxLength <= 3) {
  console.log(0);
} else {
  let sum = 0;
  for (let i = 2; i < maxLength; i++) {
    sum += Number(process.argv[i]);
  }
  console.log(sum);
}

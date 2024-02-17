#!/usr/bin/node

const maxLength = process.argv.length;
if (maxLength <= 3) {
  console.log(0);
} else {
  let largest = process.argv[2];
  for (let i = 2; i < maxLength; i++) {
    if (process.argv[i] >= largest) {
      largest = process.argv[i];
    }
  }
  console.log(largest);
}

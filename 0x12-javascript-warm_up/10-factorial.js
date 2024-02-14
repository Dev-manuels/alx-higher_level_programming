#!/usr/bin/node
function factorial (number) {
  if (number === 1) {
    return (1);
  } else {
    return (number * factorial(number - 1));
  }
}

const number = Number(process.argv[2]);
if (isNaN(number)) {
  console.log(1);
} else {
  console.log(factorial(number));
}

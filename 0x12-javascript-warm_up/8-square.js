#!/usr/bin/node
const size = Math.floor(Number(process.argv[2]));
if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (let h = 0; h < size; h++) {
    let row = '';
    for (let w = 0; w < size; w++) row += 'X';
    console.log(row);
  }
}

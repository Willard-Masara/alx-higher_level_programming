#!/usr/bin/node
const args = process.argv.slice(2).map(Number);
function findSecondLargest(arr) {
    if (arr.length < 2) {
        return 0;
    }
    let firstMax = Math.max(...arr);
    arr.splice(arr.indexOf(firstMax), 1);
    let secondMax = Math.max(...arr);
    return secondMax;
}
const result = findSecondLargest(args);
console.log(result);

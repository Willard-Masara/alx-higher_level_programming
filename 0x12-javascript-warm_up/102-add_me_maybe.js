#!/usr/bin/env node
function incrementAndCall(number, theFunction) {
    const incrementedNumber = number + 1;
    theFunction(incrementedNumber);
}

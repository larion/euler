"use strict"

const _  = require('lodash');

const MAX = 28123;

const isAbundant = n => {
    let sum=1, i;
    for(i=2;i<=Math.sqrt(n);i++) {
            sum += (n%i === 0)
               ? n/i === i
                   ? i
                   : n/i + i
               : 0;
            if(sum > n) return true;
    }}

const abundants    = _.range(MAX).filter(isAbundant);
const abundantsSet = _.mapKeys(abundants, (val, key) => val);

console.log(
    _.range(MAX).filter( n =>
        abundants.slice(0, _.sortedLastIndex(abundants, n/2))
                 .every(a => !(n-a in abundantsSet))
    ).reduce((a, b) => a + b)
);

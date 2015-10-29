/**
 * @param {string} s
 * @return {number}
 */
/**
 * Error 1: did not consider no repetition: 'c' should return 1
 * Error 2: new start should update the location stored in the dict: 'umvejcuuk' should return 6
 */
var lengthOfLongestSubstring = function(s) {
    d = {};
    len = 0;
    start = 0;
    var i = 0;
    var newlen = 0;
    while (i < s.length) {
        if (d[s[i]] === undefined) {
            d[s[i]] = i;
            i++;
            newlen++;
        } else {
            if (newlen > len) {
                len = newlen;
            }
            for (var j = start; j < d[s[i]]; j++) {
                delete d[s[j]];
                newlen--;
            }
            start = d[s[i]] + 1;
            d[s[i]] = i;
            i++;
        }
    }
    return newlen > len ? newlen : len;
};

console.log(lengthOfLongestSubstring('abcdbcdcad'));

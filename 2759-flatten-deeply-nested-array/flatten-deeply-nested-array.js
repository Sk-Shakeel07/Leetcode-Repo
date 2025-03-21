/**
 * @param {Array} arr
 * @param {number} n
 * @return {Array}
 */
var flat = function (arr, n) {
    function helper(array, depth) {
        let result = [];
        for (let item of array) {
            if (Array.isArray(item) && depth < n) {
                result.push(...helper(item, depth + 1));
            } else {
                result.push(item);
            }
        }
        return result;
    }
    return helper(arr, 0);
};

console.log(flat([1, 2, 3, [4, 5, 6], [7, 8, [9, 10, 11], 12], [13, 14, 15]], 0));
console.log(flat([1, 2, 3, [4, 5, 6], [7, 8, [9, 10, 11], 12], [13, 14, 15]], 1));
console.log(flat([[1, 2, 3], [4, 5, 6], [7, 8, [9, 10, 11], 12], [13, 14, 15]], 2));
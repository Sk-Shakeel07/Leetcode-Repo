/**
 * @param {Object|Array} obj
 * @return {boolean}
 */
var isEmpty = function(obj) {
    if (Array.isArray(obj)) {
        return obj.length === 0;
    } else if (typeof obj === 'object' && obj !== null) {
        return Object.keys(obj).length === 0;
    }
    return false; // In case input is neither an object nor an array
};

console.log(isEmpty({"x": 5, "y": 42})); 
console.log(isEmpty({}));               
console.log(isEmpty([null, false, 0])); 
console.log(isEmpty([]));               
console.log(isEmpty(null));             
console.log(isEmpty(42));               

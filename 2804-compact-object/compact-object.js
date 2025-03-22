/**
 * @param {Object|Array} obj
 * @return {Object|Array}
 */
var compactObject = function(obj) {
    if (Array.isArray(obj)) {
        return obj.filter(Boolean).map(compactObject);
    } else if (typeof obj === "object" && obj !== null) {
        return Object.fromEntries(
            Object.entries(obj)
                .filter(([_, value]) => Boolean(value))
                .map(([key, value]) => [key, compactObject(value)])
        );
    }
    return obj;
};

console.log(compactObject([null, 0, false, 1])); 
console.log(compactObject({"a": null, "b": [false, 1]})); 
console.log(compactObject([null, 0, 5, [0], [false, 16]])); 

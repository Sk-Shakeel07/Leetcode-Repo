/**
 * @param {Function} fn
 * @param {number} t
 * @return {Function}
 */
var timeLimit = function(fn, t) {
    return async function(...args) {
        return new Promise((resolve, reject) => {
            // Set a timeout to reject with "Time Limit Exceeded"
            const timer = setTimeout(() => reject("Time Limit Exceeded"), t);
            
            // Execute the original function
            fn(...args)
                .then((res) => {
                    clearTimeout(timer); // Clear timeout if function resolves in time
                    resolve(res);
                })
                .catch((err) => {
                    clearTimeout(timer); // Clear timeout if function rejects
                    reject(err);
                });
        });
    };
};
/**
 * const limited = timeLimit((t) => new Promise(res => setTimeout(res, t)), 100);
 * limited(150).catch(console.log) // "Time Limit Exceeded" at t=100ms
 */
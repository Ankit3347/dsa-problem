/**
 * @param {Object} context
 * @param {...any} args
 * @return {null|boolean|number|string|Array|Object}
 */
Function.prototype.callPolyfill = function (context, ...args) {
    const uniqueKey = Symbol();

    // Attach the function to the object
    context[uniqueKey] = this;

    // Call the function with the given arguments
    const result = context[uniqueKey](...args);

    // Clean up
    delete context[uniqueKey];

    return result;
};

/**
 * function increment() { this.count++; return this.count; }
 * increment.callPolyfill({count: 1}); // 2
 */
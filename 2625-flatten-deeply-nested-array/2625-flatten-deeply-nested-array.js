/**
 * @param {Array} arr
 * @param {number} depth
 * @return {Array}
 */
var flat = function (arr, depth) {
    const result = [];

    function dfs(array, currentDepth) {
        for (const item of array) {
            if (Array.isArray(item) && currentDepth < depth) {
                dfs(item, currentDepth + 1);
            } else {
                result.push(item);
            }
        }
    }

    dfs(arr, 0);
    return result;
};
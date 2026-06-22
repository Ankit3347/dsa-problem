/**
 * @param {*} obj
 * @param {*} classFunction
 * @return {boolean}
 */
var checkIfInstanceOf = function(obj, classFunction) {
    if (obj === null || obj === undefined) return false;
    if (typeof classFunction !== "function") return false;

    try {
        return Object(obj) instanceof classFunction;
    } catch {
        return false;
    }
};
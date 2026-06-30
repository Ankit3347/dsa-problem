/**
 * @param {number} rowsCount
 * @param {number} colsCount
 * @return {Array<Array<number>>}
 */
Array.prototype.snail = function(rowsCount, colsCount) {

    if (rowsCount * colsCount !== this.length) {
        return [];
    }

    const result = Array.from(
        { length: rowsCount },
        () => Array(colsCount)
    );

    let index = 0;

    for (let col = 0; col < colsCount; col++) {

        if (col % 2 === 0) {
            // Top -> Bottom
            for (let row = 0; row < rowsCount; row++) {
                result[row][col] = this[index++];
            }
        } else {
            // Bottom -> Top
            for (let row = rowsCount - 1; row >= 0; row--) {
                result[row][col] = this[index++];
            }
        }
    }

    return result;
};

/**
 * const arr = [1,2,3,4];
 * arr.snail(1,4); // [[1,2,3,4]]
 */
/**
 * @param {Generator} generator
 * @return {[Function, Promise]}
 */
var cancellable = function (generator) {
    let cancelled = false;

    const cancel = () => {
        cancelled = true;
    };

    const promise = new Promise((resolve, reject) => {

        function step(method, value) {
            let result;

            try {
                result = generator[method](value);
            } catch (err) {
                reject(err);
                return;
            }

            const { value: yielded, done } = result;

            if (done) {
                resolve(yielded);
                return;
            }

            Promise.resolve(yielded)
                .then((val) => {
                    if (cancelled) {
                        step("throw", "Cancelled");
                    } else {
                        step("next", val);
                    }
                })
                .catch((err) => {
                    if (cancelled) {
                        step("throw", "Cancelled");
                    } else {
                        step("throw", err);
                    }
                });
        }

        step("next");
    });

    return [cancel, promise];
};
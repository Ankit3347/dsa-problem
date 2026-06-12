class Foo {
private:
    mutex mtx;
    condition_variable cv;
    bool firstDone = false;
    bool secondDone = false;

public:
    Foo() {}

    void first(function<void()> printFirst) {
        printFirst();

        {
            lock_guard<mutex> lock(mtx);
            firstDone = true;
        }
        cv.notify_all();
    }

    void second(function<void()> printSecond) {
        unique_lock<mutex> lock(mtx);
        cv.wait(lock, [this] { return firstDone; });

        printSecond();

        secondDone = true;
        cv.notify_all();
    }

    void third(function<void()> printThird) {
        unique_lock<mutex> lock(mtx);
        cv.wait(lock, [this] { return secondDone; });

        printThird();
    }
};
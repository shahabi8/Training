// here idea is to use multiset which balanced binary tree. 
// I have access to reference of each item in multiset
// now iterator should move when length of array is odd
// when size is 1 it = 1, sz = 2, it = 1, sz = 3, it = 2 ...
class MedianFinder {
public:
    std::multiset<int> data;
    std::multiset<int>::iterator it;
    MedianFinder() {

    }
    
    void addNum(int num) {
        data.insert(num);
        auto sz = data.size();
        // when length is one initialize the iterator
        if (data.size() == 1){
            it = data.begin();
        }
        // when num is smaller than it, so it goes before ir
        else if (num < *it) {
            // if size is even move back it else keep it
            it = (sz % 2 == 0) ? --it : it;
        }
        else {
            // if sz is even keep it as num is placed after it, else move it one forward
            it = (sz % 2 == 0) ? it : ++it;
        }
    }
    
    double findMedian() {
        if (data.size() % 2 == 1) {
            return static_cast<double>(*it);
        }
        auto cp = it;
        return (static_cast<double>(*cp) + static_cast<double>(*(++cp))) * 0.5;
    }
};
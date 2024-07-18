#include <sstream>
#include <string>
auto tp = std::string{};
auto path = std::string{"/path/to/file"}
std::stringstream ss{path};

while (getline(ss, tp, '/')) {
    if (tp.empty()) continue;
    if (tp == "..") {
        if (!output_vec.empty()) output_vec.pop_back();
    } else if (tp == ".") {
        continue;
    } else {
        output_vec.push_back(tp);
    }
}

// This function compares the elements of two sequences and determines if one is lexicographically smaller than the other.
bool isLexicographicallySmaller(const std::vector<std::string>& list1, const std::vector<std::string>& list2) {
    return std::lexicographical_compare(list1.begin(), list1.end(), list2.begin(), list2.end());
}
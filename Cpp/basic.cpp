#include <sstream>
#include <string>
#include <algorithm> // for std::max_element
#include <list>
#include <vector>
#include <unordered_map>

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

int main() {
    std::string str1 = "apple";
    std::string str2 = "banana";

    if (str1 < str2) {
        std::cout << str1 << " is lexicographically smaller than " << str2 << std::endl;
    } else if (str1 > str2) {
        std::cout << str1 << " is lexicographically greater than " << str2 << std::endl;
    } else {
        std::cout << str1 << " is equal to " << str2 << std::endl;
    }

    return 0;
}

// giving unordered_map iterator of list so that map can keep track of 
// items in list
std::unordered_map<int, std::list<std::pair<int, int>>::iterator> cache;
std::list<std::pair<int, int>> lruList;
// splice to move items in list
lruList.splice(lruList.begin(), lruList, cache[key]);

std::list<int> list1 = {1, 2, 3};
std::list<int> list2 = {4, 5, 6};

// Splice the element '5' from list2 to list1
auto it = list2.begin();
std::advance(it, 1); // Point to the element '5'
list1.splice(list1.end(), list2, it);

// list1: 1 2 3 5 
// list2: 4 6 


std::vector<int> numbers = {3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5};

// Find the maximum element
auto max_it = std::max_element(numbers.begin(), numbers.end());

std::vector<std::tuple<int, int>> points = {{1, 2}, {3, 4}, {5, 1}, {2, 9}};

// Find the point with the maximum y-coordinate
auto max_it = std::max_element(points.begin(), points.end(),
                                [](const auto& a, const auto b) {
                                    return std::get<1>(a) < std::get<1>(b);
                                });

// max int in C++
int max_int = std::numeric_limits<int>::max();

// slicing string 
string newWord = word.substr(0, i) + '*' + word.substr(i + 1, L);
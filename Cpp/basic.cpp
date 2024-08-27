#include <sstream>
#include <string>
#include <algorithm> // for std::max_element
#include <list>
#include <vector>
#include <unordered_map>
#include <iostream>
#include <queue>
#include <memory>
#include <cctype>

//  move semantics are primarily beneficial for types that manage resources 
// (e.g., dynamically allocated memory), not for primitive types.
// size = other.size;
// other.size = 0;

// Create a unique_ptr to manage a single int
std::unique_ptr<int> ptr = std::make_unique<int>(10);

// Create a unique_ptr to manage a dynamic array of ints with size 5
std::unique_ptr<int[]> ptr = std::make_unique<int[]>(5);
// Create a shared_ptr to manage a dynamic array of ints with a custom deleter
std::shared_ptr<int[]> ptr(new int[5], std::default_delete<int[]>());

int n = 5; // Size of the array
int* arr = new int[n]; // Dynamically allocating memory for the array
// Dynamically allocate memory for a 2D array
int rows = 3;
int cols = 4;
int** arr = new int*[rows];
for (int i = 0; i < rows; i++) {
    arr[i] = new int[cols];
}
// static array
std::array<int, 5> arr = {1, 2, 3, 4, 5};
// 2D array using nested std::array
std::array<std::array<int, cols>, rows> arr = {{
    {1, 2, 3, 4},
    {5, 6, 7, 8},
    {9, 10, 11, 12}
}};
// 2D vector
std::vector<std::vector<int>> arr(rows, std::vector<int>(cols));

// Provides a non-owning reference to a resource managed by std::shared_ptr, 
// useful for avoiding circular references and managing non-owning relationships.
void useWeakPtr(std::weak_ptr<int> weakPtr) {
    if (auto sharedPtr = weakPtr.lock()) {
        std::cout << "Inside function, value: " << *sharedPtr << std::endl;
    } else {
        std::cout << "Object no longer exists" << std::endl;
    }
}

// Avoid multiple shared_ptr for one resource,
// you'll get multiple deletion error 
auto sharedPtr = std::make_shared<int>(42);
std::weak_ptr<int> weakPtr = sharedPtr;

// avoid doing below 
// Manually create a raw pointer
int* rawPtr = new int(42);

// Create the first shared_ptr from the raw pointer
std::shared_ptr<int> sharedPtr1(rawPtr);

// Create the second shared_ptr from the same raw pointer
std::shared_ptr<int> sharedPtr2(rawPtr);

useWeakPtr(weakPtr);  // Object exists, value is printed


//Passing std::unique_ptr to Functions
void takeOwnership(std::unique_ptr<MyClass> ptr) {
    // Function now owns the ptr
}

// if pointer goes out of scope somewhere else
// we will have dangling reference in this function
void useButDontTakeOwnership(const std::unique_ptr<MyClass>& ptr) {
    // Access the object pointed by ptr not owning
}

void processSharedPtr(std::shared_ptr<int> ptr) {
    // increase ownership counts
}

void takeOwnership(std::shared_ptr<int>&& ptr) {
    // doesn't increase ownership counts
    // this function is owner, caller loses its ownership
    std::cout << "Inside function, value: " << *ptr << std::endl;
}

// if pointer goes out of scope somewhere else
// we will have dangling reference
void readSharedPtr(const std::shared_ptr<int>& ptr) {
    // doesn't increase ownership counts
    std::cout << "Inside function, value: " << *ptr << std::endl;
}

void modifySharedPtr(std::shared_ptr<int>& ptr) {
    // doesn't increase ownership counts
    ptr = std::make_shared<int>(84);
}

// double linklist with shared pointer
// we cannot use 2 shared pointer because life of 
// two objects will depend on each other and
// this cyclic reference causes memory leak
// two weak pointer would work but in connecting
// curent node to next node you need to make sure
// next node life is same as current node
//     void append(int value) {
//         auto newNode = std::make_shared<Node>(value);
//         newNode->prev = tail;
//         tail->next = newNode;
//         tail = newNode;
//     }
// in this append function newNode goes out of scope as function exists
// and newNode resource will be removed unless there is another shared_ptr
// owning this resource so that's why next must be a shared_ptr.
class Node {
public:
    int value;
    std::shared_ptr<Node> next;
    std::weak_ptr<Node> prev;  // Use weak_ptr to avoid cyclic reference

    Node(int val) : value(val) {
        std::cout << "Node constructed with value " << value << std::endl;
    }

    ~Node() {
        std::cout << "Node destroyed with value " << value << std::endl;
    }
};

auto node = std::make_shared<Node>(1);
auto node2 = std::make_shared<Node>(2);
node->next = node2;
node2->prev = node;

// shared_from_this and enable_shared_from_this
// enable_shared_from_this let us to get shared_ptr
// to itself from within class member function

// Move Constructor and Move Assignment Operator
class MyClass : public std::enable_shared_from_this<MyClass> {
public:
    std::unique_ptr<int[]> data;
    size_t size;
    std::vector<std::shared_ptr<MyClass>> registry;
    // Move constructor
    // Transfer ownership of resources from other to this
    MyClass(MyClass&& other) noexcept : data{std::move(other.data)}, size{other.size}{
        other.size = 0;
    }

    MyClass& operator=(MyClass&& other) noexcept { // Move assignment operator
        if (this != &other) {
            // Release any resources this object owns
            // Transfer ownership of resources from other to this
            data = std::move(other.data);
            size = other.size;
            other.size = 0;
        }
        return *this;
    }
    // Disable copy constructor and copy assignment operator
    // In fact, std::unique_ptr is specifically designed to enforce unique ownership,
    // meaning it cannot be copied by default. Instead, you manage resource ownership through move semantics.
    MyClass(const MyClass& other) = delete;
    MyClass& operator=(const MyClass& other) = delete;
    // get shared pointer of same resource
    std::shared_ptr<MyClass> getShared() {
        return shared_from_this();
    }
    void registerSelf() {
        // This is incorrect and will cause issues
        // std::shared_ptr<Node> self(this);
        auto self = shared_from_this();
        registry.push_back(self);  // Register itself
    }
};

// usage
// auto sharedPtr1 = std::make_shared<MyClass>(42);
// auto sharedPtr2 = sharedPtr1->getShared();
// since we're outside of class this also works
// auto sharedPtr2 = sharedPtr1;

// Copy Constructor and Copy Assignment Operator
class MyClass {
public:
    std::unique_ptr<int[]> data;
    size_t size;
    MyClass(const MyClass& other) { // Copy constructor
        // Create a copy of other's resources
    }

    MyClass& operator=(const MyClass& other) { // Copy assignment operator
        if (this != &other) {
            // Release any resources this object owns
            // Create a copy of other's resources
        }
        return *this;
    }
};

// string in C++
auto s = std::string{};
// append another string
s.append("!");
// push back character
s.push_back('!');
// c_str(): Returns a pointer to a null-terminated C-string equivalent to the string.
const char* cstr = s.c_str();
// Returns a pointer to the character array used internally by the string.
const char* data = s.data();
//substr(size_t pos, size_t len): Returns a substring starting at pos of length len.
std::string sub = s.substr(0, 5);
// find(const std::string& str, size_t pos = 0): Finds the first occurrence of str starting from position pos.
size_t pos = s.find("World");

std::transform(s.begin(), s.end(), s.begin(), ::tolower);

if (isspace(c)) {
    std::cout << "The character is a whitespace." << std::endl;
}
if (isdigit(c)) {
    std::cout << "The character is a digit." << std::endl;
}
if (isalpha(c)) {
    std::cout << "The character is an alphabetic letter." << std::endl;
}
if (isalnum(c)) {
    std::cout << "The character is alphanumeric." << std::endl;
}
if (ispunct(c)) {
    std::cout << "The character is a punctuation mark." << std::endl;
}
if (islower(c)) {
    std::cout << "The character is a lowercase letter." << std::endl;
}
if (isupper(c)) {
    std::cout << "The character is an uppercase letter." << std::endl;
}

int num = 123;
std::string str = std::to_string(num);

std::string str = "456";
int num = std::stoi(str);

// int to string through stringstream
int num = 789;
std::stringstream ss;
ss << num;
std::string str = ss.str();

// string to int through stringstream
std::string str = "321";
std::stringstream ss(str);
int num;
ss >> num;

std::string str = "9223372036854775807";  // Maximum value for int64_t
int64_t num = std::stoll(str);

std::string str = "123.45";
float num = std::stof(str);

std::string str = "123.456789";
double num = std::stod(str);

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

// set in C++
auto it = s.lower_bound(10);
auto it = s.upper_bound(10);
// equal_range(const T& value): Returns a pair of iterators representing 
// the range of elements that are equivalent to the given value.
auto range = s.equal_range(10);

// Check if set2 is a subset of set1
if (std::includes(set1.begin(), set1.end(), set2.begin(), set2.end())) {
    std::cout << "set2 is a subset of set1" << std::endl;
}

std::set<int> intersection;
std::set_intersection(set1.begin(), set1.end(), set2.begin(), set2.end(),
                        std::inserter(intersection, intersection.begin()));

// Union
std::set<int> unionSet;
std::set_union(set1.begin(), set1.end(), set2.begin(), set2.end(),
                std::inserter(unionSet, unionSet.begin()));
        
// Difference (set1 - set2)
std::set<int> difference;
std::set_difference(set1.begin(), set1.end(), set2.begin(), set2.end(),
                    std::inserter(difference, difference.begin()));
// giving unordered_map iterator of list so that map can keep track of 
// items in list
std::unordered_map<int, std::list<std::pair<int, int>>::iterator> cache;
// another example to use ::iterator
unordered_map<int, list<pair<int, int>>> frequencies;
// key: original key, value: pair of frequency and the iterator corresponding key int the
// frequencies map's list.
unordered_map<int, pair<int, list<pair<int, int>>::iterator>> cache;


void insert(int key, int frequency, int value) {
    frequencies[frequency].push_back({key, value});
    cache[key] = {frequency, --frequencies[frequency].end()};
}



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

// sorting
std::vector<std::tuple<int, int>> vec = {
    {1, 4},
    {2, 3},
    {3, 2},
    {4, 1}
};

// Sort the vector by the second item in the tuple
std::sort(vec.begin(), vec.end(), [](const auto& a, const auto& b) {
    return std::get<1>(a) < std::get<1>(b);
});

auto it = std::find(vec.begin(), vec.end(), 3);
std::reverse(vec.begin(), vec.end());
int count = std::count(vec.begin(), vec.end(), 3);
std::transform(vec.begin(), vec.end(), vec.begin(), [](int x) { return x * 2; });

// max int in C++
int max_int = std::numeric_limits<int>::max();

// slicing string 
std::string newWord = word.substr(0, i) + '*' + word.substr(i + 1, L);

// pass function to function in C++
int add(int a, int b) {
    return a + b;
}

struct Add {
    int operator()(int a, int b) {
        return a + b;
    }
};

// Function that takes a functor as a parameter
template<typename Func>
void applyFunction(Func func, int x, int y) {
    std::cout << "Result: " << func(x, y) << std::endl;
}

// Function that takes a function pointer as a parameter
void applyFunction(int (*func)(int, int), int x, int y) {
    std::cout << "Result: " << func(x, y) << std::endl;
}

// Function that takes an std::function as a parameter
void applyFunction(std::function<int(int, int)> func, int x, int y) {
    std::cout << "Result: " << func(x, y) << std::endl;
}

applyFunction(add, 5, 3);

Add add;
applyFunction(add, 5, 3);

// heap in C++

std::priority_queue<int> maxHeap;
std::priority_queue<int, std::vector<int>, std::greater<int>> minHeap;
minHeap.push(3);
minHeap.push(5);
minHeap.push(1);
minHeap.push(8);

// Print and remove elements
while (!minHeap.empty()) {
    std::cout << minHeap.top() << " "; // Prints the smallest element
    minHeap.pop(); // Removes the smallest element
}

// Custom comparator for the heap
struct CustomCompare {
    bool operator()(const int& lhs, const int& rhs) const {
        return lhs > rhs; // Otherwise, sort in descending order
    }
};

// Create a custom heap using priority_queue with CustomCompare
std::priority_queue<int, std::vector<int>, CustomCompare> customHeap;
auto customCompare = [](const int& lhs, const int& rhs) {
    return lhs > rhs; // Otherwise, sort in descending order
};
std::priority_queue<int, std::vector<int>, decltype(customCompare)> customHeap(customCompare);

// generate random number netween min and max
std::srand(static_cast<unsigned int>(std::time(0)));

// Define the range [min, max]
int min = 10;
int max = 20;

// Generate a random number in the range [min, max]
int random_number = min + rand() % (max - min + 1);
// Generate a random floating-point number between 0.0 and 1.0
auto randnum = static_cast<float>(std::rand()) / RAND_MAX;

// C++ static method can return instance of class
class Pizza {
public:
    // Constructor is private to force the use of factory methods
    Pizza(const std::vector<std::string>& ingredients) : ingredients_(ingredients) {}

    // Static factory method for Margherita pizza
    static std::shared_ptr<Pizza> margherita() {
        return std::make_shared<Pizza>(std::vector<std::string>{"mozzarella", "tomatoes"});
    }

    // Static factory method for Pepperoni pizza
    static std::shared_ptr<Pizza> pepperoni() {
        return std::make_shared<Pizza>(std::vector<std::string>{"mozzarella", "tomatoes", "pepperoni"});
    }

    // Static factory method for custom pizza
    static std::shared_ptr<Pizza> custom(const std::vector<std::string>& ingredients) {
        return std::make_shared<Pizza>(ingredients);
    }

    // Function to print ingredients
    void print() const {
        std::cout << "Pizza with ";
        for (const auto& ingredient : ingredients_) {
            std::cout << ingredient << " ";
        }
        std::cout << std::endl;
    }

private:
    std::vector<std::string> ingredients_;
};

// reverse array in C++
std::vector<int> arr = {1, 2, 3, 4, 5, 6, 7};
// reverse whole array
std::reverse(arr.begin(), arr.end());
// reverse portion of array
std::reverse(arr.begin() + 2, arr.begin() + 6);

// move data from map vector and set to each other
std::map<int, std::string> myMap = {
    {1, "one"},
    {2, "two"},
    {3, "three"}
};

// Convert to a set of pairs
std::set<std::pair<int, std::string>> mySet(myMap.begin(), myMap.end());
// Convert to a set of keys
std::set<int> keySet;
for (const auto& pair : myMap) {
    keySet.insert(pair.first);
}

std::map<int, std::string> myMap = {
    {1, "one"},
    {2, "two"},
    {3, "three"}
};

// Convert to a vector of pairs
std::vector<std::pair<int, std::string>> myVector(myMap.begin(), myMap.end());
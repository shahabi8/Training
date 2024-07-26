#include <iostream>
#include <memory>

// Node class
class Node {
public:
    int data;
    std::unique_ptr<Node> next;

    Node(int data) : data(data), next(nullptr) {}
};

// LinkedList class
class LinkedList {
public:
    std::unique_ptr<Node> head;

    LinkedList() : head(nullptr) {}

    void append(int data) {
        std::unique_ptr<Node> newNode = std::make_unique<Node>(data);
        if (!head) {
            head = std::move(newNode);
            return;
        }
        Node* lastNode = head.get();
        while (lastNode->next) {
            lastNode = lastNode->next.get();
        }
        lastNode->next = std::move(newNode);
    }

    int length() const {
        int count = 0;
        Node* current = head.get();
        while (current) {
            count++;
            current = current->next.get();
        }
        return count;
    }

    bool operator<(const LinkedList& other) const {
        return this->length() < other.length();
    }

    bool operator<=(const LinkedList& other) const {
        return this->length() <= other.length();
    }

    bool operator==(const LinkedList& other) const {
        return this->length() == other.length();
    }

    bool operator!=(const LinkedList& other) const {
        return !(*this == other);
    }

    bool operator>(const LinkedList& other) const {
        return this->length() > other.length();
    }

    bool operator>=(const LinkedList& other) const {
        return this->length() >= other.length();
    }

    friend std::ostream& operator<<(std::ostream& os, const LinkedList& list);
};

// Overload the << operator to print the LinkedList
std::ostream& operator<<(std::ostream& os, const LinkedList& list) {
    Node* current = list.head.get();
    while (current) {
        os << current->data;
        if (current->next) {
            os << " -> ";
        }
        current = current->next.get();
    }
    return os;
}

// Example usage
int main() {
    LinkedList ll1;
    ll1.append(1);
    ll1.append(2);
    ll1.append(3);

    LinkedList ll2;
    ll2.append(4);
    ll2.append(5);

    LinkedList ll3;
    ll3.append(6);
    ll3.append(7);
    ll3.append(8);

    std::cout << "LinkedList 1: " << ll1 << std::endl;
    std::cout << "LinkedList 2: " << ll2 << std::endl;
    std::cout << "LinkedList 3: " << ll3 << std::endl;

    std::cout << "LinkedList 1 < LinkedList 2: " << (ll1 < ll2) << std::endl;
    std::cout << "LinkedList 1 <= LinkedList 2: " << (ll1 <= ll2) << std::endl;
    std::cout << "LinkedList 1 == LinkedList 3: " << (ll1 == ll3) << std::endl;
    std::cout << "LinkedList 1 != LinkedList 2: " << (ll1 != ll2) << std::endl;
    std::cout << "LinkedList 1 > LinkedList 2: " << (ll1 > ll2) << std::endl;
    std::cout << "LinkedList 1 >= LinkedList 3: " << (ll1 >= ll3) << std::endl;

    return 0;
}

// type conversion operator and operator overload
// operator TypeName() const;
// operator std::vector<char>() const {
//     return std::vector<char>(str, str + length);
// }
// ReturnType operator OperatorSymbol (ParameterList);
// Complex operator+(const Complex& other) const {
//     return Complex(real + other.real, imag + other.imag);
// }
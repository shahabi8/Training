#include <iostream>
#include <memory>
#include <vector>
#include <unordered_map>
#include <map>


// adapter
// Target Interface
class PrinterInterface {
public:
    virtual ~PrinterInterface() = default;
    virtual void print(const std::string &text) = 0;
};

// Adaptee
class OldPrinter {
public:
    void oldPrintMethod(const std::string &text) {
        std::cout << "Old Printer: " << text << std::endl;
    }
};

// Adapter
class PrinterAdapter : public PrinterInterface {
private:
    std::unique_ptr<OldPrinter> oldPrinter;

public:
    PrinterAdapter(std::unique_ptr<OldPrinter> printer) : oldPrinter(std::move(printer)) {}

    void print(const std::string &text) override {
        oldPrinter->oldPrintMethod(text);
    }
};

// usage
auto oldPrinter = std::make_unique<OldPrinter>();
auto adapter = PrinterAdapter{std::move(oldPrinter)};
adapter.print();
/////////////////////////////////////////////////////////////////////////////////////////////////////

// bridge design pattern
class DrawApi {
    public:
    virtual void draw(int x, int y, int radius) = 0;
    virtual ~DrawApi() = default;
};

class DrawApi1 : DrawApi {
    void draw(int x, int y, int radius) override {
        std::cout << "drawing api1 at center of " << x << "," << y << " with radious " << radius << std::endl;
    }
};

class DrawApi2 : DrawApi {
    void draw(int x, int y, int radius) override {
        std::cout << "drawing api2 at center of " << x << "," << y << " with radious " << radius << std::endl;
    }
};

class DrawCircle {
    DrawCircle(std::unique_ptr<DrawApi> api) : DrawApiImpl{std::move(api)} {}
    void draw(int x, int y, int radius) {
        DrawApiImpl->draw(x, y, radius);
    }
    private:
    std::unique_ptr<DrawApi> DrawApiImpl;
}

// client code
auto api = std::make_unique<DrawApi2>();
auto circle = DrawCircle{std::move(api)};
circle.draw(6,8,6);


// composite pattern with inheritance
class Component {
public:
    virtual ~Component() = default;
    virtual void operation() const = 0;
};

class Leaf : public Component {
public:
    void operation() const override {
        std::cout << "print from leaf" << std::endl;
    }
};

class Composite : public Component {
public:
    void add(std::shared_ptr<Component> component) {
        children.push_back(component);
    }

    void remove() {
        if (!children.empty()) {
            children.pop_back();
        }
    }

    void operation() const override {
        for (const auto& child : children) {
            child->operation();
        }
    }

private:
    std::vector<std::shared_ptr<Component>> children;
};

//composite pattern with composition
// class Leaf {
// public:
//     void operation() const override {
//         std::cout << "print from leaf" << std::endl;
//     }
// };

// template<typename T>
// class Composite {
// public:
//     void add(std::shared_ptr<T> component) {
//         children.push_back(component);
//     }

//     void remove() {
//         if (!children.empty()) {
//             children.pop_back();
//         }
//     }

//     void operation() const override {
//         for (const auto& child : children) {
//             child->operation();
//         }
//     }

// private:
//     std::vector<std::shared_ptr<T>> children;
// };

// // usage

// auto node1 = std::make_shared<leaf>();
// auto node2 = std::make_shared<leaf>();

// auto composition = std::make_shared<composite<leaf>>();
// composition->add(node1);
// composition->add(node2);
// composition->operation();


// decorator pattern

class text {
    text() = default;
    virtual void render(std::string& message) = 0;
};

class text_message : text {
    text_message(std::string& input) : message{input}{}
    void render() override {
        std::cout << message << std::endl;
    }
    private:
    std::string message;
};

class decorator : text {
    decorator(std::shared_ptr<text> input) : component{input}{}
    void render() override{
        component->render();
    }
    private:
        std::shared_ptr<text> component; 
};

class decorator2 : decorator {
    decorator2(std::shared_ptr<text> input) : decorator{input}{}
    void render() override {
        std::cout << "decorator2" + decorator::render() << std::endl;
    }
};

class decorator3 : decorator {
    decorator3(std::shared_ptr<text> input) : decorator{input}{}
    void render() override {
        std::cout << "decorator3" + decorator::render() << std::endl;
    }
};

std::shared_ptr<text> simpleText = std::make_shared<text_message>("Hello, World!");
std::cout << "Simple text: " << simpleText->render() << std::endl;

std::shared_ptr<text> decorator2Text = std::make_shared<decorator2>(simpleText);
std::cout << "Italic and Bold text: " << decorator2Text->render() << std::endl;

std::shared_ptr<text> decorator3Text = std::make_shared<decorator3>(decorator2Text);
std::cout << "Fully decorated text: " << decorator3Text->render() << std::endl;

// facade

class CPU {
    void freeze(){
        std::cout << "CPU freeze" << std::endl;
    }

    void jump(int position) {
        std::cout << position << std::endl;
    }

    void execute() {
        std::cout << "cpu execute" << std::endl; 
    }
};
class memory {
    void load(int position, const std::string& data) {
        std::cout << position << data << std::endl;
    }
};

class computerFacade {
    computerFacade(std::shared_ptr<memory> mem, std::shared_ptr<CPU> processor) : memory{mem}, cpu{processor} {}
    void startup() {
        cpu->freeze();
        memory->load(1, "startup");
        cpu->jump(1);
        cpu->execute();
    }
    private:
    std::shared_ptr<memory> memory;
    std::shared_ptr<CPU> cpu;
}

// flyweight
struct shared_state {
    std::string data;
    std::unordered_map<int, int> locations;
    // Define comparison operators for shared_state
    bool operator==(const shared_state& other) const {
        return data == other.data && locations == other.locations;
    }
};
struct unique_state{
    std::string color;
    std::string status;
};
class Flyweight {
    Flyweight(std::shared_ptr<shared_state> shared) : _shared{shared}{}
    void operation(std::shared_ptr<unique_state> _unique) {
        std::cout << _unique->status << ',' << _shared->data << std::endl;
    }

    private:
    std::shared_ptr<shared_state> _shared;
};

class FlyweightFactory {
    static std::map<shared_state, std::shared_ptr<Flyweight>> flyweights;
    std::shared_ptr<Flyweight>> get_flyweight(std::shared_ptr<shared_state> shared) {
        if (flyweights.count(*shared)) {
            return flyweights[*shared];
        }
        Flyweights[*shared] = make_shared<Flyweight>(shared)
        return Flyweights[shared];
    }
    void list_flyweights() const {
        std::cout << "FlyweightFactory: I have " << flyweights.size() << " flyweights:" << std::endl;
        for (const auto& pair : flyweights) {
            std::cout << "  " << pair.first.data << std::endl;
        }
    }
};

class context {
    context(std::shared_ptr<Flyweight> flyweight, std::shared_ptr<unique_state> unique_state) : _flyweight{flyweight}, _unique_state{unique_state} {}
    void operation() {
        return _flyweight->operation(_unique_state);
    }

    private:
    std::shared_ptr<Flyweight> _flyweight;
    std::shared_ptr<unique_state> _unique_state;
}

// factory pattern
// Base class
class Animal {
public:
    virtual ~Animal() = default;
    virtual std::string speak() const = 0;
};

// Derived class Dog
class Dog : public Animal {
public:
    std::string speak() const override {
        return "Woof!";
    }

    void fetch() const {
        std::cout << "Fetching!" << std::endl;
    }
};

// Derived class Cat
class Cat : public Animal {
public:
    std::string speak() const override {
        return "Meow!";
    }

    void scratch() const {
        std::cout << "Scratching!" << std::endl;
    }
};

// Factory class using templates
class AnimalFactory {
public:
    template <typename T>
    std::unique_ptr<T> createAnimal() const {
        return std::make_unique<T>();
    }
};
// usage
AnimalFactory factory;

auto dog = factory.createAnimal<Dog>();
dog->fetch();  // Output: Fetching!
auto cat = factory.createAnimal<Cat>();
cat->scratch();
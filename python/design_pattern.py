from abc import ABC, abstractmethod

# adapter
# The Adapter Pattern, also known as the Wrapper Pattern, is a structural design pattern 
# that allows objects with incompatible interfaces to work together. The adapter pattern 
# acts as a bridge between two incompatible interfaces by providing a way for classes to 
# interact that otherwise could not due to interface mismatches.
# Key Concepts

#     Target Interface: The interface that the client expects.
#     Adaptee: The existing interface that needs to be adapted.
#     Adapter: The class that bridges the gap between the Target 
#     and the Adaptee by implementing the Target interface and delegating 
#     calls to an instance of the Adaptee.
class TargetInterface(ABC):
    @abstractmethod
    def connect(self):
        pass

class EuropeanPlug:
    def plug_in(self):
        return "European plug connected"

class USASocket:
    def connect(self):
        return "USA socket connected"

class Adapter(TargetInterface):
    def __init__(self, plug):
        self.plug = plug

    def connect(self):
        return self.plug.plug_in()

# Usage
european_plug = EuropeanPlug()
adapter = Adapter(european_plug)
print(adapter.connect())  # Output: European plug connected


#Bridge Pattern
class DrawingAPI:
    def draw_circle(self, x, y, radius):
        pass

class DrawingAPI1(DrawingAPI):
    def draw_circle(self, x, y, radius):
        print(f"API1.circle at {x}:{y} radius {radius}")

class DrawingAPI2(DrawingAPI):
    def draw_circle(self, x, y, radius):
        print(f"API2.circle at {x}:{y} radius {radius}")

class Circle:
    def __init__(self, x, y, radius, drawing_api):
        self._x = x
        self._y = y
        self._radius = radius
        self._drawing_api = drawing_api

    def draw(self):
        self._drawing_api.draw_circle(self._x, self._y, self._radius)

    def scale(self, pct):
        self._radius *= pct

# Usage
circle1 = Circle(1, 2, 3, DrawingAPI1())
circle2 = Circle(5, 7, 11, DrawingAPI2())

circle1.draw()  # Output: API1.circle at 1:2 radius 3
circle2.draw()  # Output: API2.circle at 5:7 radius 11

# Composite Pattern
# component is good to have when we expect leaf class to have specific
# operation method implemented, however we can directly pass leaf to 
# composite methods
class Component(ABC):
    @abstractmethod
    def operation(self):
        pass

class Leaf(Component):
    def operation(self):
        print("Leaf")

class Composite(Component):
    def __init__(self):
        self._children = []

    def add(self, component: Component):
        self._children.append(component)

    def remove(self, component: Component):
        self._children.remove(component)

    def operation(self):
        for child in self._children:
            child.operation()

# Usage
leaf1 = Leaf()
leaf2 = Leaf()
composite = Composite()
composite.add(leaf1)
composite.add(leaf2)
composite.operation()


# Decorator Pattern
class Component:
    def operation(self):
        pass

class ConcreteComponent(Component):
    def operation(self):
        return "ConcreteComponent"

class Decorator(Component):
    def __init__(self, component: Component):
        self._component = component

    def operation(self):
        return self._component.operation()

class ConcreteDecoratorA(Decorator):
    def operation(self):
        return f"ConcreteDecoratorA({self._component.operation()})"

class ConcreteDecoratorB(Decorator):
    def operation(self):
        return f"ConcreteDecoratorB({self._component.operation()})"

# Usage
component = ConcreteComponent()
decorator1 = ConcreteDecoratorA(component)
decorator2 = ConcreteDecoratorB(decorator1)

print(decorator2.operation())  # Output: ConcreteDecoratorB(ConcreteDecoratorA(ConcreteComponent))


#facade
class CPU:
    def freeze(self):
        print("CPU freeze")

    def jump(self, position):
        print(f"CPU jump to {position}")

    def execute(self):
        print("CPU execute")

class Memory:
    def load(self, position, data):
        print(f"Memory load data at {position}")

class HardDrive:
    def read(self, lba, size):
        return "HardDrive data"

class ComputerFacade:
    def __init__(self):
        self.cpu = CPU()
        self.memory = Memory()
        self.hard_drive = HardDrive()

    def start(self):
        self.cpu.freeze()
        self.memory.load(0, self.hard_drive.read(0, 1024))
        self.cpu.jump(0)
        self.cpu.execute()

# Usage
computer = ComputerFacade()
computer.start()

# Singleton Pattern
class Singleton:
    _instance = None # class static attribute
    # cls can access class attributes
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

# Usage
singleton1 = Singleton()
singleton2 = Singleton()

print(singleton1 is singleton2)  # Output: True

# Factory Pattern
class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass
class Dog(Animal):
    def speak(self):
        return "Woof!"
    
    def fetch(self):
        return "Fetching!"

class Cat(Animal):
    def speak(self):
        return "Meow!"
    
    def scratch(self):
        return "Scratching!"

class AnimalFactory:
    def create_animal(self, animal_class):
        return animal_class()

# Usage
factory = AnimalFactory()
dog = factory.create_animal(Dog)
print(dog.speak())  # Output: Woof!
print(dog.fetch())  # Output: Fetching!

cat = factory.create_animal(Cat)
print(cat.speak())  # Output: Meow!
print(cat.scratch())  # Output: Scratching!

# Flyweight Pattern
# The Flyweight Pattern is a structural design pattern used to minimize 
# memory usage or computational expenses by sharing as much data as 
# possible with similar objects. It's particularly useful when a large 
# number of objects need to be created and managed.

# A common use case for the Flyweight Pattern is in graphical applications 
# where many similar objects need to be created, such as rendering a large 
# number of characters in a text editor or graphical shapes in a drawing application.
class Flyweight:
    def __init__(self, shared_state):
        self.shared_state = shared_state

    def operation(self, unique_state):
        print(f"Flyweight: Shared ({self.shared_state}) and unique ({unique_state}) state.")

class FlyweightFactory:
    _flyweights = {}

    @classmethod
    def get_flyweight(cls, shared_state):
        if shared_state not in cls._flyweights:
            cls._flyweights[shared_state] = Flyweight(shared_state)
        return cls._flyweights[shared_state]
    
class context:
    def __init__(self, flyweight, unique_state):
        self.flyweight = flyweight
        self.unique_state = unique_state
    
    def operation(self):
        self.flyweight.operation(self.unique_state)

# Usage
factory = FlyweightFactory()

flyweight1 = factory.get_flyweight("shared state 1")
flyweight2 = factory.get_flyweight("shared state 1")
flyweight3 = factory.get_flyweight("shared state 2")

# Proxy Pattern
class RealSubject:
    def request(self):
        print("RealSubject: Handling request.")

class Proxy:
    def __init__(self, real_subject):
        self._real_subject = real_subject

    def request(self):
        if self.check_access():
            self._real_subject.request()
            self.log_access()

    def check_access(self):
        print("Proxy: Checking access before firing a real request.")
        return True

    def log_access(self):
        print("Proxy: Logging the time of request.")

# Usage
real_subject = RealSubject()
proxy = Proxy(real_subject)
proxy.request()
# Output:
# Proxy: Checking access before firing a real request.
# RealSubject: Handling request.
# Proxy: Logging the time of request.

# observer

class Subject:
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self, message):
        for observer in self._observers:
            observer.update(message)

class Observer:
    def update(self, message):
        pass

class ConcreteObserver(Observer):
    def update(self, message):
        print(f"Observer received message: {message}")

# Usage
subject = Subject()
observer1 = ConcreteObserver()
observer2 = ConcreteObserver()

subject.attach(observer1)
subject.attach(observer2)

subject.notify("Hello Observers!")  # Output: Observer received message: Hello Observers! (twice)

# Strategy Pattern
class Strategy:
    def execute(self, data):
        pass

class ConcreteStrategyA(Strategy):
    def execute(self, data):
        print("Strategy A executed with", data)

class ConcreteStrategyB(Strategy):
    def execute(self, data):
        print("Strategy B executed with", data)

class Context:
    def __init__(self, strategy: Strategy):
        self._strategy = strategy

    def set_strategy(self, strategy: Strategy):
        self._strategy = strategy

    def execute_strategy(self, data):
        self._strategy.execute(data)

# Usage
context = Context(ConcreteStrategyA())
context.execute_strategy("some data")  # Output: Strategy A executed with some data

context.set_strategy(ConcreteStrategyB())
context.execute_strategy("other data")  # Output: Strategy B executed with other data


#command pattern
class Command:
    def execute(self):
        pass

class Light:
    def on(self):
        print("Light is ON")

    def off(self):
        print("Light is OFF")

class LightOnCommand(Command):
    def __init__(self, light: Light):
        self._light = light

    def execute(self):
        self._light.on()

class LightOffCommand(Command):
    def __init__(self, light: Light):
        self._light = light

    def execute(self):
        self._light.off()

class RemoteControl:
    def __init__(self):
        self._commands = {}

    def set_command(self, button, command: Command):
        self._commands[button] = command

    def press_button(self, button):
        if button in self._commands:
            self._commands[button].execute()

# Usage
light = Light()
light_on = LightOnCommand(light)
light_off = LightOffCommand(light)

remote = RemoteControl()
remote.set_command("ON", light_on)
remote.set_command("OFF", light_off)

remote.press_button("ON")   # Output: Light is ON
remote.press_button("OFF")  # Output: Light is OFF

#State Pattern:
class State:
    def handle(self):
        pass

class ConcreteStateA(State):
    def handle(self):
        print("State A handling request")

class ConcreteStateB(State):
    def handle(self):
        print("State B handling request")

class Context:
    def __init__(self, state: State):
        self._state = state

    def set_state(self, state: State):
        self._state = state

    def request(self):
        self._state.handle()

# Usage
state_a = ConcreteStateA()
state_b = ConcreteStateB()

context = Context(state_a)
context.request()  # Output: State A handling request

context.set_state(state_b)
context.request()  # Output: State B handling request

# Chain of Responsibility Pattern


#Interpreter Pattern
class AbstractExpression:
    def interpret(self, context):
        pass

class TerminalExpression(AbstractExpression):
    def __init__(self, value):
        self.value = value

    def interpret(self, context):
        return self.value

class NonTerminalExpression(AbstractExpression):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def interpret(self, context):
        return self.left.interpret(context) + self.right.interpret(context)

# Usage
context = {}
expression1 = TerminalExpression(1)
expression2 = TerminalExpression(2)
expression3 = NonTerminalExpression(expression1, expression2)
print(expression3.interpret(context))  # Output: 3


#Mediator Pattern
class Mediator:
    def notify(self, sender, event):
        pass

class ConcreteMediator(Mediator):
    def __init__(self, component1, component2):
        self._component1 = component1
        self._component1.mediator = self
        self._component2 = component2
        self._component2.mediator = self

    def notify(self, sender, event):
        if event == "A":
            print("Mediator reacts on A and triggers the following operations:")
            self._component2.do_c()
        elif event == "D":
            print("Mediator reacts on D and triggers the following operations:")
            self._component1.do_b()

class BaseComponent:
    def __init__(self, mediator=None):
        self._mediator = mediator

    @property
    def mediator(self):
        return self._mediator

    @mediator.setter
    def mediator(self, mediator):
        self._mediator = mediator

class Component1(BaseComponent):
    def do_a(self):
        print("Component 1 does A.")
        self.mediator.notify(self, "A")

    def do_b(self):
        print("Component 1 does B.")

class Component2(BaseComponent):
    def do_c(self):
        print("Component 2 does C.")

    def do_d(self):
        print("Component 2 does D.")
        self.mediator.notify(self, "D")

# Usage
c1 = Component1()
c2 = Component2()
mediator = ConcreteMediator(c1, c2)

print("Client triggers operation A.")
c1.do_a()
print("\nClient triggers operation D.")
c2.do_d()
# Output:
# Client triggers operation A.
# Component 1 does A.
# Mediator reacts on A and triggers the following operations:
# Component 2 does C.

# Client triggers operation D.
# Component 2 does D.
# Mediator reacts on D and triggers the following operations:
# Component 1 does B.

# Memento Pattern
class Memento:
    def __init__(self, state):
        self._state = state

    def get_state(self):
        return self._state

class Originator:
    def __init__(self, state):
        self._state = state

    def save(self):
        return Memento(self._state)

    def restore(self, memento):
        self._state = memento.get_state()

    def get_state(self):
        return self._state

    def set_state(self, state):
        self._state = state

class Caretaker:
    def __init__(self):
        self._mementos = []

    def add_memento(self, memento):
        self._mementos.append(memento)

    def get_memento(self, index):
        return self._mementos[index]

# Usage
originator = Originator("State1")
caretaker = Caretaker()
caretaker.add_memento(originator.save())

originator.set_state("State2")
caretaker.add_memento(originator.save())

originator.set_state("State3")

originator.restore(caretaker.get_memento(0))
print(originator.get_state())  # Output: State1

originator.restore(caretaker.get_memento(1))
print(originator.get_state())  # Output: State2


#Visitor Pattern
class Visitor:
    def visit(self, element):
        pass

class ConcreteVisitor1(Visitor):
    def visit(self, element):
        print("ConcreteVisitor1:", element.operation())

class ConcreteVisitor2(Visitor):
    def visit(self, element):
        print("ConcreteVisitor2:", element.operation())

class Element:
    def accept(self, visitor: Visitor):
        pass

class ConcreteElementA(Element):
    def accept(self, visitor: Visitor):
        visitor.visit(self)

    def operation(self):
        return "ConcreteElementA operation"

class ConcreteElementB(Element):
    def accept(self, visitor: Visitor):
        visitor.visit(self)

    def operation(self):
        return "ConcreteElementB operation"

# Usage
elements = [ConcreteElementA(), ConcreteElementB()]
visitor1 = ConcreteVisitor1()
visitor2 = ConcreteVisitor2()

for element in elements:
    element.accept(visitor1)
    element.accept(visitor2)
# Output:
# ConcreteVisitor1: ConcreteElementA operation
# ConcreteVisitor2: ConcreteElementA operation
# ConcreteVisitor1: ConcreteElementB operation
# ConcreteVisitor2: ConcreteElementB operation
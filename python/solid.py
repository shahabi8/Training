from abc import ABC, abstractmethod

# Single Responsibility Principle (SRP)
class Report:
    def __init__(self, title, content):
        self.title = title
        self.content = content

    def format(self):
        return f"{self.title}\n{self.content}"

class ReportPrinter:
    def print(self, report: Report):
        print(report.format())

# Usage
report = Report("Monthly Report", "This is the content of the monthly report.")
printer = ReportPrinter()
printer.print(report)

#Open/Closed Principle (OCP)
class Discount(ABC):
    @abstractmethod
    def apply_discount(self, amount):
        pass

class NoDiscount(Discount):
    def apply_discount(self, amount):
        return amount

class PercentageDiscount(Discount):
    def __init__(self, percentage):
        self.percentage = percentage

    def apply_discount(self, amount):
        return amount - (amount * self.percentage / 100)

# Usage
def calculate_price(amount, discount: Discount):
    return discount.apply_discount(amount)

amount = 100
no_discount = NoDiscount()
percentage_discount = PercentageDiscount(10)

#Liskov Substitution Principle
class Bird:
    def fly(self):
        print("Flying")

class Sparrow(Bird):
    def fly(self):
        print("Sparrow flying")

class Ostrich(Bird):
    def fly(self):
        raise Exception("Ostriches can't fly")

# Usage
def make_bird_fly(bird: Bird):
    bird.fly()

sparrow = Sparrow()
ostrich = Ostrich()
make_bird_fly(sparrow)  # Output: Sparrow flying
make_bird_fly(ostrich)  # Raises exception: Ostriches can't fly

class Workable(ABC):
    @abstractmethod
    def work(self):
        pass

class Eatable(ABC):
    @abstractmethod
    def eat(self):
        pass

class HumanWorker(Workable, Eatable):
    def work(self):
        print("Human working")

    def eat(self):
        print("Human eating")

class RobotWorker(Workable):
    def work(self):
        print("Robot working")

# Usage
def manage_worker(worker: Workable):
    worker.work()

human = HumanWorker()
robot = RobotWorker()

manage_worker(human)  # Output: Human working
manage_worker(robot)  # Output: Robot working

#Dependency Inversion Principle (DIP)

class Database(ABC):
    @abstractmethod
    def connect(self):
        pass

class MySQLDatabase(Database):
    def connect(self):
        print("Connecting to MySQL Database")

class Application:
    def __init__(self, database: Database):
        self.database = database

    def start(self):
        self.database.connect()

# Usage
mysql_db = MySQLDatabase()
app = Application(mysql_db)
app.start()  # Output: Connecting to MySQL Database
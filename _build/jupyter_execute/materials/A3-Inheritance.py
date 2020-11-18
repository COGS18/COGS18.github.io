# Expanding on Class Inheritance

In this example below, we see that when you pass a Parent class (`Animal()`) into a Child class (`Dog()` and `Cat()`), the children ***inherit the attributes and methods of the Parent class***.

class Animal():
    
    sound = 'Generic Animal Sound'
    
    def __init__(self, name):
        self.name = name
    
    def speak(self, n_times=2):
        return self.sound * n_times

# specify class inheritance by passing
# parent class in parentheses
class Dog(Animal):
    sound = 'Woof'

class Cat(Animal):
    sound = "Meow"

# demonstrating inheritance...
my_dog = Dog('Ruffus')
print('child class attribute:', my_dog.sound)
print('parent instance attribute:', my_dog.name)
print('using parent method...')
my_dog.speak()

# Adding a cell for you to test this
# concept out with the Cat() type object

But...what happens if you pass in a Parent class and then define instance attributes within the child class? (I'm just going to focus on the class `Dog()` from here, but feel free to test it out by editing and adding to the `Cat()` example to ensure understanding.

class Animal():
    
    sound = 'Generic Animal Sound'
    
    def __init__(self, name):
        self.name = name
    
    def speak(self, n_times=2):
        return self.sound * n_times

# create instance attribute in child
class Dog(Animal):
    sound = 'Woof'
    
    def __init__(self, breed):
        self.breed = breed

my_dog = Dog('Italian Greyhound')
print('child class attribute:', my_dog.sound)
print('child instance attribute:', my_dog.breed)

# this next line will lead to an AttributeError
print('parent instance attribute:', my_dog.name)

In the example above, note that when we define instance attributes, this overwrites the parent instance attributes.

Unless...

Unless we specify that we want to inherit the instance attributes from the parent class. One way to do this is with `super()`

class Animal():
    
    sound = 'Generic Animal Sound'
    
    def __init__(self, name):
        self.name = name
    
    def speak(self, n_times=2):
        return self.sound * n_times

class Dog(Animal):
    sound = 'Woof'
    
    def __init__(self, name, breed):
        super().__init__(name)         # specify to include parent instance attributes
        self.breed = breed

my_dog = Dog(name = 'Ruffus', breed='Italian Greyhound')
print('child class attribute:', my_dog.sound)
print('child instance attribute:', my_dog.breed)
print('parent instance attribute:', my_dog.name)

Note that in the above instance attribute definition, we needed to specify that the two instance attributes would be `breed` and `name` within the definition. Then within side the `__init__` code block, we specify where `name` will be inherited from and that `breed` will be the instance attribute, specific to the `Dog()` class.

If this weren't the syntax, there would be no way for Python to disambiguate between which position was `name` and which was `breed`.

So...if that's true, why *didn't* we need to pass anything into `super` in that `Tool()` example from class?

class Tool():
    
    def __init__(self):       
        self.is_tool = True
        self.tool_type = None
    
    def use_tool(self):
        print('Using tool.')

class Hammer(Tool): #inherit Tool class
    
    def __init__(self):        
        super().__init__() # inherit initialization from Tool()
        self.tool_type = 'Hammer'
        self.why = 'To hammer things.'

In the above case, there are no additional values that need to be assigned on creation of an instance of a `Hammer()`. Specifically, `is_tool` and `tool_type` already have values assigned in the Parent class, so the user, when creating a Hammer instance, does not have to pass any values in when creating the instance. 

# seeing inheritance example
my_tool = Tool()
my_hammer = Hammer()
print(my_hammer.is_tool)
print(my_hammer.why)
print(my_hammer.tool_type)
my_hammer.use_tool()

Considering that, I'm going to edit the `Animal()`/`Dog()` example to demonstrate what that would look like for that example...

class Animal():
    
    sound = 'Generic Animal Sound'
    
    def __init__(self, name='Default Name'): #set default value for name
        self.name = name
    
    def speak(self, n_times=2):
        return self.sound * n_times

class Dog(Animal):
    sound = 'Woof'
    
    def __init__(self, breed):
        super().__init__()
        self.breed = breed

my_dog = Dog('Italian Greyhound')
print('child class attribute:', my_dog.sound)
print('child instance attribute:', my_dog.breed)
print('parent instance attribute:', my_dog.name)

In the above, I've set a default value for `name`. Thus, when I create a `Dog()` and do *not* pass any attributes into `super()`, it inherits the values from `Animal()`.

Note that by using the above syntax you lose the ability to change the value of `name` in `Dog()`...as that is not an input parameter to your `__init__` in Dog(). So, you're stuck with the name in the parent class.

# This code will generate a Type Error
my_dog = Dog(name='Lexi', breed='Italian Greyhound')

Note that this is not the case for `Animal()` (the parent class). There, you can still specify a different value for the attribute `name`.

my_animal = Animal(name='other animal name')
my_animal.name

While using `super()` is preferred, in response to a student question...

What if we wanted to call the Parent class directly...rather than use `super()`? 

We could use the syntax seen below, calling `Animal.__init__`, but know that `self` has to be passed in when this construct is used.

class Animal():
    
    sound = 'Generic Animal Sound'
    
    def __init__(self, name):
        self.name = name
    
    def speak(self, n_times=2):
        return self.sound * n_times

class Dog(Animal):
    sound = 'Woof'
    
    def __init__(self, name, breed):
        Animal.__init__(self, name)         # specify to include parent instance attributes
        self.breed = breed

my_dog = Dog('Ruffus','Italian Greyhound')
print('child class attribute:', my_dog.sound)
print('child instance attribute:', my_dog.breed)
print('parent instance attribute:', my_dog.name)
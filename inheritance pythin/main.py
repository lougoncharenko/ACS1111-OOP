from turtle import color


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce_self(self):
        print(f"My name is {self.name} and my age is {self.age}")
        
    

class Student(Person):
    def __init__(self, name, age, major):
        super().__init__(name, age)
        self.major = major

    def declare_major(self):
        print(f"{self.name} studies {self.major}")


class Instrument():
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def play_instrument(self):
        print(f"{self.name} makes the sound {self.sound}")


class Musician(Person):
    def __init__(self, name, age, fav_song, instrument):
        super().__init__(name, age)
        self.fav_song = fav_song
        self.instrument = instrument

    def introduce_self(self):
        print(f"My name is {self.name} and my age is {self.age} and my favorite song is {self.fav_song}")
        

    def hums_tune(self):
        print(f"{self.name} hums {self.fav_song}")

    def add_instrument(self, new_instrument):
        self.instrument = self.instrument.append(new_instrument)
        print(self.instrument)

    def play(self, n):
        print(f"{self.instrument[1]} plays the following sound", "Boom " *n )
       
Louisa = Musician("Louisa", 21, '7 rings', ['Trumpet', 'Drums'])
Cindy = Musician('Cindy', 25, 'Red room', ['Guitar', 'Violin'] )

musicians = [Louisa, Cindy]

class Band():
    def __init__(self, name, genre, members):
        self.name = name
        self.genre = genre
        self.member = members

    def list_members(self):
        for member in self.member:
            print(member.name)

    def play_song(self):
        for member in self.member:
            print(f"{member.name} plays {member.fav_song}")

    def introduce(self):
         for member in self.member:
            print(f"Hello! My name is {member.name} and I am {member.age}. I play {member.instrument}")



eagles = Band('eagle', 'rock', musicians)
eagles.list_members()
eagles.play_song()
eagles.introduce()

# trumpet = Instrument('Trumpet', "Toot")
# trumpet.play_instrument()
# piano = Instrument('Piano', 'plink')
# piano.play_instrument()


# cassidy = Person("Cassidy", 20)
# isabella = Student("Isabella", 19, 'computer science')

# cassidy.introduce_self()
# isabella.introduce_self()
# isabella.declare_major()

# Louisa = Musician('Louisa', 21, '7 rings')
# Louisa.introduce_self()


class Car():
    def __init__(self,model, color):
        self.model = model #protected
        self.color = color # protected

    def paint_color(self, color):
        self.color = color
        print(f"This car is painted {self.color}") #protected
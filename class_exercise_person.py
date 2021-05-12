class Person:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
        self.friends = []
        self.greeting_count = 0
        self.unique_greeting_count = []

    def __str__(self):
        return 'Person: %s %s %s' % (self.name, self.email, self.phone)

    def greet(self, other_person):
        self.greeting_count += 1
        self.unique_greeting_count.append(other_person)
        return ('Hello %s, I am %s' % (other_person.name, self.name))

    def print_contact_info(self):
        print("%s's email: %s\n%s's phone number: %s" % (self.name, self.email, self.name, self.phone))

    def add_friend(self, other_person):
        self.friends.append(other_person)

    def num_friends(self):
        return len(self.friends)
    
    def num_unique_greeting(self):
        print(len(self.unique_greeting_count))


sonny = Person("Sonny", "sonny@hotmail.com", "483-485-4948")
jordan = Person("Jordan", "jordan@aol.com", "495-586-3456")


# print(sonny.email, sonny.phone)
# print(jordan.email, jordan.phone)

# sonny.print_contact_info()

# jordan.add_friend(sonny)

# jordan.num_friends()
# sonny.num_friends()

sonny.greet(jordan)
print(sonny.greeting_count)
#sonny.num_unique_greeting()

sonny.greet(jordan)
print(sonny.greeting_count)
#sonny.num_unique_greeting()

# print(jordan.__str__())


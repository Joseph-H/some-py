from collections import ChainMap, Counter, defaultdict, deque, namedtuple, OrderedDict

# chainmap example
car_parts = {'hood': 500, 'engine': 5000, 'front_door': 750}
car_options = {'A/C': 1000, 'Turbo': 2500, 'rollbar': 300}
car_accessories = {'cover': 100, 'hood_ornament': 150, 'seat_cover': 99}

# combine all the maps together
car_pricing = ChainMap(car_accessories, car_options, car_parts)
print (car_pricing['hood']) #500

# counter example
print (Counter('superfluous'))
#Counter({'u': 3, 's': 2, 'e': 1, 'l': 1, 'f': 1, 'o': 1, 'r': 1, 'p': 1})

counter = Counter('superfluous')
print (counter['u']) #3

# defaultdict example
# you can set a default value if the value is not present
sentence = "The red for jumped over the fence and ran to the zoo for food"
words = sentence.split(' ')

# you can also pass a lambda to this constructor
d = defaultdict(int)
for word in words:
    d[word] += 1

print(d)

# deque example
numbers = deque([1,2,3,4,5])
numbers.append(6)
numbers.appendleft(0)
print(numbers)


# namedtuple example - allows you to create a tuple with named properties
# first parameter is the type second param is a space delimited list of property names
Person = namedtuple("Person", "firstname lastname age")
joseph = Person(firstname="joseph", lastname="h", age="30")
print(joseph)
print(type(joseph))

# OrderedDict example - dictionary that keeps insertion order
ordered = OrderedDict({"a":1, "b":2, "c":3})
print(ordered)

# remove a then re-insert it. it will be at the end
ordered.pop("a")
print(ordered)

ordered["a"] = 1
print(ordered)

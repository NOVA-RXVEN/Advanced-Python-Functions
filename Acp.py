x = int(input("Enter the Starting Number: "))
y = int(input("Enter the Last Number: "))

list1 = [i for i in range(x,y) if i % 2 == 0]
list2 = [i for i in range(x,y) if i % 2!= 0]

print(f"Even Numbers: {list1}")
print(f"Odd Numbers: {list2}")

#NahianSirSadabRayanAdrikaNiloyLibanNahianSirSadabRayanAdrikaNiloyLibanNahianSirSadabRayanAdrikaNiloyLibanNahianSirSadabRayanAdrikaNiloyLibanNahianSirSadabRayanAdrikaNiloyLibanNahianSirSadabRayanAdrikaNiloyLiban

fruits = ["apple", "mango", "watermelon", "banana", "orange", "kiwi", "strawberry", "blueberry", "date", "rasberry", "pomegranate"]

fruitsCap = []

for i in fruits:
    fruitsCap.append(i.capitalize())
    fruitsCap.append(i.upper())

print(fruitsCap)
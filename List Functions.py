lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
friends2 = friends.copy()
friends.extend(lucky_numbers)
friends.append("Creed")
friends.insert(1,"Kelly")
friends.pop()
print(friends.index("Oscar"))
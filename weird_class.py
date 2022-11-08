from types import SimpleNamespace

def Person(name, age, likes):
    _this = dict()
    _this["name"] = name
    _this["age"] = age
    _this["likes"] = likes

    def _greet():
        return f"Hi! My name is {name} and I'm {age} years old\n"
    def _date_profile():
        return f"If you like {likes[0]} " + "and ".join(likes[1:]) + "...\n"
    def _mul_age(n):
        return n*age
    
    _this["greet"] = _greet
    _this["date_profile"] = _date_profile
    _this["mul_age"] = _mul_age

    return SimpleNamespace(**_this)

p = Person("Rupert Holmes", 32, ["piña colada", "getting caught in the rain"])
print(p.greet())
print(p.date_profile())
print(p.mul_age(5))

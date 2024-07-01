def say_hi(name: str, age: int) -> str:
    """
    Generates a greeting message with the person's name and age.
    """
    return f"This is a cool dude {name}, he is {age} years old! WOW!!!"


assert say_hi("Alex", 32) == "This is a cool dude Alex, he is 32 years old! WOW!!!", 'Test1'
assert say_hi("Frank", 68) == "This is a cool dude Frank, he is 68 years old! WOW!!!", 'Test2'
print('ОК')

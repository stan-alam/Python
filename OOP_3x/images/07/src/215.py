# 215.A

def stan_function():
    print("Stan's function was called")

stan_function.description = "Stan's function is totally radical, dude!"

def second_function():
    print("The other function was called")

second_function.description = "This function is awesome!!!"

def yet_another_function(function):
    print("The description:", end=" ")
    print(function.description)
    print("the name:", end=" ")
    print(function.__name__)
    print("The class:", end=" ")
    print(function.__class__)
    print("Now We'll call the function that was passed to us!")
    function

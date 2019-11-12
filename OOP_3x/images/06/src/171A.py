# 171.A
random_keys = { }
random_keys["astring"] = "whatever"
random_keys[5] = "an_int"
random_keys[42.0] = "floats_are_good"
random_keys[("xyz", "456")] = "groovy tuples"

class AwesomeObj:
    def __init__(self, avalue):
        self.avalue = avalue

my_obj = AwesomeObj(14)
random_keys[my_obj] = "We can store objects!"
my_obj.avalue = 13
try:
    random_keys[[1,2,3]] = "Sorry we can't store lists"
except:
    print("unable to store lists\n")

for key, value in random_keys.items():
    print ("{} has value {}".format(key, value))

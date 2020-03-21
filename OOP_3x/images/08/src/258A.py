import pickle

my_data = ["some kind of list", "containing", 5, "values including another list", ["inner", "list"]]

with open("pickled_list", 'a') as file:
    pickle.dump(my_data, file)

with open("pickled_list" 'b') as file:
    loaded_data = pickle.load(file)

print(loaded_data)
assert loaded_data == my_data

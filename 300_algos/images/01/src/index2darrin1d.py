def index_2d_to_1d(row, col, num_cols):
    return row * num_cols + col
row, col, num_cols = 4,5,6
index = index_2d_to_1d(row, col, num_cols)
print(f'1d index: {index}') # what is the output?

row, col, num_cols = 2,3,4
index = index_2d_to_1d(row, col, num_cols)
print(f'1d index: {index}') # what is the output?

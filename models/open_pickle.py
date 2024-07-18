import pickle

file = 'A_EPC_NN_model.keras.pkl'
# Open the pickle file
with open(file, 'rb') as file:
    data = pickle.load(file)

# Print the contents of the pickle file
print(data)

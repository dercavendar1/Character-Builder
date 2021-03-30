import pickle


def save_data(input):
    file = open(b"saved data.obj", "wb")
    pickle.dump(input, file)


def load_data(file_path):
    loaded_data = open(file_path, "rb")
    data = pickle.load(loaded_data)

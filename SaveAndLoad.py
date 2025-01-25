import jsonpickle
import os

class SaveAndLoad:

    def save_data(data, filename):
        path = os.getcwd() + '/' + filename
        with open(path, "w") as file:
            json_data = jsonpickle.encode(data)
            file.write(json_data)
        print("Data saved to " + path)
        
    def load_data(filename):
        path = os.getcwd() + '/' + filename
        try:
            with open(path, 'r') as file:
                json_data = file.read()
                loaded_data = jsonpickle.decode(json_data)
            return loaded_data
        except FileNotFoundError:
            print("" + path + " not found. No data loaded.")
            return None
import json 

def save_data_to_file(file_path, data):
    """ Saves the provided JSON data"""
    try:
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=2)
        print(f'Data saved to {file_path}')
    except IOError as e:
        print(f'Failed to write to {file_path} : {e}')
    except TypeError as e:
        print(f'Data has non-serialized type {e}')
    except Exception as e:
        print(f'An expected error occurred: {e}')

def main():
    # data to be serialized 
    data = {
        "Name" : "Tanaka",
        "age" : 40,
        "studies" : ["Python", "Linux", "Java"],
        "isEmployed" : True,
        "hobbies" : ["travelling"]
    }
    
    file_path = 'data.json'
    save_data_to_file(file_path, data)

if __name__ == '__main__':
    main()
import csv
import json


class TestDataCreator:

    def __init__(self, json_path_file, csv_path_file):
        self.json_path_file = json_path_file
        self.csv_path_file = csv_path_file
        self.json_file = self.open_json()
        self.csv_file = self.open_csv()
        self.merged_files = self.merge_data()

    def open_json(self):
        with open(self.json_path_file) as json_file:
            return json.loads(json_file.read())

    def open_csv(self):
        with open(self.csv_path_file) as csv_file:
            read_file = csv_file.read()
            data = csv.reader(read_file.splitlines(), delimiter=',')
            next(data)
            return data

    def merge_data(self):
        merged_data = []

        for users in self.json_file:
            merged_data.append({'name': users['name'],
                                'gender': users['gender'],
                                'address': users['address'],
                                'books': []
                                })

        iterator = iter(merged_data)

        try:
            for book in self.csv_file:
                title, author, genre, height, publisher = book

                next(iterator)["books"].append({'title': title,
                                                'author': author,
                                                'height': height
                                                })

        except StopIteration:
            "Adding data is stopped"

        return merged_data

    def save_new_file(self, file_name):
        with open(file_name, 'w') as new_file:
            formated_file = json.dumps(self.merged_files, indent=3)
            new_file.write(formated_file)


if __name__ == "__main__":
    file = TestDataCreator('users.json', "books.csv")
    file.save_new_file("createdFile.json")

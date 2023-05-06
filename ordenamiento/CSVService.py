import csv

DEFAULT_ENCODING = 'ISO 8859_1'
DEFAULT_DELIMITER = ','


class CSVService:
    def __init__(self, csv_file_path):
        self.__csv_file = csv_file_path
        self.__headers = None
        self.__data = None
        self.__read_csv()

    def __read_csv(self):
        with open(self.__csv_file, 'r', encoding=DEFAULT_ENCODING) as file:
            reader = csv.reader(file, delimiter=DEFAULT_DELIMITER)
            self.__headers = next(reader)
            self.__data = []
            for row in reader:
                self.__data.append(row)

    def get_headers(self):
        return self.__headers

    def get_data(self):
        return self.__data

class FileManager:
    def __init__(self, file_name):
        self.file_name = file_name

    def read_file(self):
        file = open(self.file_name)
        data = file.read()
        #print(plik)
        file.close()
        return data

    def update_file(self, text_data):
        file = open(self.file_name)
        #file = open(self.file_name, 'a')
        #data = file.write(text_data)
        data = file.read()
        data += " " + text_data
        file.close()
        return data





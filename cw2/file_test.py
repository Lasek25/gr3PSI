from cw2.file import FileManager

plik = FileManager(r'C:\Users\Krzysztof\PycharmProjects\gr3PSI\cw2\test.txt')
print(plik.read_file())
print(plik.update_file("Additional text to add to the end of the file."))
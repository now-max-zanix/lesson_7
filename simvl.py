import module

text = input("\nВведите текст:(Enter-для чтения файла):")

if not text:
    text = module.read_from_file()

module.col_symbol(text)  #Frequency of each character

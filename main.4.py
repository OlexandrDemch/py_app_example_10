number = input("Введіть ціле число: ")

filtered_number = ''.join([c for c in number if c != '3' and c != '6'])

print(filtered_number)
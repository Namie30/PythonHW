# #1
# with open("Testing.txt", "w") as f:
#     for i in range(1000):
#         f.write("Hi guys this is myu file \n")
#
# #2
# numbers = [2, 8, 10, 13, 17]
# names = ["Second line", "Eighth line", "Tenth line", "Thirteenth line", "Seventeenth line"]
#
# with open("numbers.txt", "w") as f:
#     for i in range(1, 18):
#         if i in numbers:
#             idx = numbers.index(i)
#             f.write(f"{names[idx]}: {i}\n")
#         else:
#             f.write("\n")
#
# print("File created and numbers written on specified lines.")

#3
# with open("file1.txt", "w") as f1:
#     f1.write("Hello from file 1.\nThis is the first test file.")
#
# with open("file2.txt", "w") as f2:
#     f2.write("Hello from file 2.\nThis is the second test file.")
#
# print("file1.txt and file2.txt have been created and initialized.")
# def merge_files(file1, file2, output_file):
#     with open(file1, "w") as f1:
#         content1 = f1.read()
#
#     with open(file2, "ww") as f2:
#         content2 = f2.read()
#
#     with open(output_file, "w") as output:
#         output.write(content1)
#         output.write("\n")
#         output.write(content2)
#
#     print(f"Contents of {file1} and {file2} have been merged into {output_file}.")
# def print_merged_file(output_file):
#     with open(output_file, "r") as merged_file:
#         print(merged_file.read())
#
# file1 = "file1.txt"
# file2 = "file2.txt"
# output_file = "merged_file.txt"
#
# merge_files(file1, file2, output_file)
# print_merged_file(output_file)

#4
file_name = "example.txt"

with open(file_name, "w") as file:
    file.write("madam\n")
    file.write("damam\n")
    file.write("level\n")
    file.write("radar\n")
    file.write("madam\n")
    file.write("reviver\n")
    file.write("deified\n")

print(f"{file_name} has been created with sample text.")
def find_palindromic_lines(file_name):
    try:
        with open(file_name, "r") as file:
            lines = [line.strip() for line in file]

        for line in lines:
            reversed_line = line[::-1]
            if reversed_line in lines and reversed_line != line:
                print(f"'{line}' is a palindrome of '{reversed_line}'")
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

find_palindromic_lines(file_name)


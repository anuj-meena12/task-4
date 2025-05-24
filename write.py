def write_and_append():
    user_input = input("Enter some data to write to the file: ")
    with open("output.txt", "w") as file:
        file.write(user_input + "\n")
    with open("output.txt", "a") as file:
        file.write("This line is appended.\n")
    with open("output.txt", "r") as file:
        content = file.read()
    print("Final content of the file:")
    print(content)

if __name__ == "__main__":
    write_and_append()

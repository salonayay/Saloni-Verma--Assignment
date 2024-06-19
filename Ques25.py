def copy_file(source_file, destination_file):
    try:
        with open(source_file, 'r') as source:
            with open(destination_file, 'w') as destination:
                destination.write(source.read())
        print("File copied successfully.")
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print("An error occurred:", e)

def main():
    source_file = input("Enter the name of the source file: ")
    destination_file = input("Enter the name of the destination file: ")
    copy_file(source_file, destination_file)

if __name__ == "_main_":
    main()
# Open (or create) a file in write mode
file = open("my_file.txt", "w")

# Write content to the file
file.write("Hello, this is a sample text.\n")
file.write("You can write multiple lines using write().\n")
file.write("Python makes file handling easy!\n")

# Close the file
file.close()

print("Content written to my_file.txt successfully.")


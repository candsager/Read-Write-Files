# This program writes three lines of data
# to a file.
def main():
# Open a file named philosophers.txt.
    outfile = open('philosophers.txt', 'w')
# Write the names of three philosphers to the file –
# John Locke, David Hume and Edmund Burke
    outfile.write('John Locke\n')
    outfile.write('Edmund Burke\n')
    outfile.write('David Hume\n')
# Close the file.
    outfile.close()
# Call the main function.
main()

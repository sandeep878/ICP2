def count_words(input_file_path, output_file_path):
    try:
        with open(input_file_path, 'r') as input_file:
            content = input_file.read()
        words = content.split()
        word_count = len(words)
        with open(output_file_path, 'w') as output_file:
            output_line = f"Word count: {word_count}\n"
            output_file.write(output_line)
            count = 0
            for word in words :
                count =  count+1
                print (f"{word} : {count} \n")
                
        print(f"Word count written to '{output_file_path}'")
    except FileNotFoundError:
        print(f"File '{input_file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

input_file_path = 'input.txt'
output_file_path = 'output.txt'
count_words(input_file_path, output_file_path)

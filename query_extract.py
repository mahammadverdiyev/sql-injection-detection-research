import os


def combine_text_files(root_dir, output_file_name="combined_payloads.txt"):
    output_file_path = os.path.join(
        root_dir, output_file_name)

    with open(output_file_path, 'w', encoding='utf-8') as outfile:
        for dirpath, _, filenames in os.walk(root_dir):
            for filename in filenames:
                if filename.endswith(".txt"):
                    file_path = os.path.join(dirpath, filename)
                    try:
                        with open(file_path, 'r', encoding='utf-8') as infile:
                            for line in infile:
                                outfile.write(line)
                            outfile.write("\n")
                        print(f"Appended content from: {file_path}")
                    except Exception as e:
                        print(f"Error reading file {file_path}: {e}")


root_directory = "Intruder"

combine_text_files(root_directory, "combined_payloads.txt")
# type: ignore
print(
    f"\nAll .txt files combined into: {os.path.join(root_directory, 'combined_payloads.txt')}")

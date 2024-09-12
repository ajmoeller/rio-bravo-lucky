# rio-bravo-lucky

# Project Knowledge Compiler

This script compiles the contents of specified project files into a single knowledge base file. It's useful for creating a comprehensive overview of a project's codebase.

## Features

- Processes files based on a provided list of file paths
- Supports any project structure
- Creates an XML-like output format for easy parsing
- Provides progress updates and final statistics

## Requirements

- Python 3.6+

## Usage

1. Create a text file (e.g., `file_paths.txt`) listing the relative paths of files you want to process, one per line.

2. Run the script:

python project_knowledge_compiler.py /path/to/your/project

Optional arguments:
- `--file_paths`: Name of the file containing paths (default: file_paths.txt)
- `--output`: Name of the output file (default: project_knowledge.txt)

3. The script will create a `project_knowledge.txt` file containing the compiled information.

## Example
python project_knowledge_compiler.py /path/to/project --file_paths my_paths.txt --output my_knowledge_base.txt

This will process the files listed in `my_paths.txt` from the `/path/to/project` directory and output the results to `my_knowledge_base.txt`.

## Contributing

Contributions, issues, and feature requests are welcome!

## License

[MIT License](LICENSE)

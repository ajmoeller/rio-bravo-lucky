# Project Knowledge Compiler

This Python script compiles the contents of specified project files into a single knowledge base file, creating a comprehensive overview of a project's codebase. It now includes additional metadata and Git information for each file.

## Features

- Processes files based on a provided list of file paths
- Supports any project structure
- Creates an XML-like output format for easy parsing
- Includes file metadata (last modified date, file size, MD5 checksum)
- Retrieves Git information (last commit hash, author, and date) for each file
- Provides progress updates and final statistics
- Allows exclusion of specific file types

## Requirements

- Python 3.6+
- GitPython library (`pip install gitpython`)

## Usage

1. Create a text file (e.g., `file_paths.txt`) listing the relative paths of files you want to process, one per line.

2. Run the script:

   ```
   python project_knowledge_compiler.py /path/to/your/project
   ```

3. Optional arguments:
   - `--file_paths`: Name of the file containing paths (default: `file_paths.txt`)
   - `--output`: Name of the output file (default: `project_knowledge.txt`)
   - `--exclude`: File extensions to exclude (default: `.gif`, `.jpg`, `.png`, `.pdf`)

4. The script will create a `project_knowledge.txt` file containing the compiled information.

## Example

```
python project_knowledge_compiler.py /path/to/project --file_paths my_paths.txt --output my_knowledge_base.txt --exclude .exe .dll
```

This will process the files listed in `my_paths.txt` from the `/path/to/project` directory, exclude `.exe` and `.dll` files, and output the results to `my_knowledge_base.txt`.

## Output Format

The output is an XML-like structure:

```xml
<documents>
  <document index="1">
    <source>relative/path/to/file.ext</source>
    <metadata>
      <last_modified>2023-04-01T12:34:56</last_modified>
      <size>1234</size>
      <last_commit_hash>abcdef1234567890</last_commit_hash>
      <last_commit_author>John Doe</last_commit_author>
      <last_commit_date>2023-03-31T10:11:12</last_commit_date>
    </metadata>
    <document_content>
      <!-- File content here -->
    </document_content>
  </document>
  <!-- More documents... -->
</documents>
```

## Notes

- The script now includes Git information, which requires the file to be part of a Git repository. If a file is not in a Git repository, the Git information will be omitted.
- File checksums are calculated using MD5. Be aware that MD5 is not cryptographically secure, but it's sufficient for file integrity checks in this context.
- The script assumes UTF-8 encoding for all text files. Files that cannot be read with UTF-8 encoding will be marked with an error message in the output.

## Contributing

Contributions, issues, and feature requests are welcome!

## License

[MIT License](LICENSE)

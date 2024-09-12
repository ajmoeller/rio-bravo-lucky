import os
import argparse
import hashlib
import git
from datetime import datetime

__version__ = "1.1.0"

def read_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except Exception as e:
        return f"Error reading file: {str(e)}"

def get_file_metadata(file_path):
    """Get metadata for a file."""
    stat = os.stat(file_path)
    return {
        "last_modified": datetime.fromtimestamp(stat.st_mtime).isoformat(),
        "size": stat.st_size,
        "checksum": hashlib.md5(open(file_path,'rb').read()).hexdigest()
    }

def get_git_info(file_path):
    """Get Git information for a file."""
    try:
        repo = git.Repo(search_parent_directories=True)
        commits = list(repo.iter_commits(paths=file_path, max_count=1))
        if commits:
            return {
                "last_commit_hash": commits[0].hexsha,
                "last_commit_author": commits[0].author.name,
                "last_commit_date": commits[0].committed_datetime.isoformat()
            }
    except:
        pass
    return {}

def main():
    parser = argparse.ArgumentParser(description="Compile project files into a single knowledge base.")
    parser.add_argument("project_dir", help="Full path to the project directory")
    parser.add_argument("--file_paths", default="file_paths.txt", help="Name of the file containing paths (default: file_paths.txt)")
    parser.add_argument("--output", default="project_knowledge.txt", help="Name of the output file (default: project_knowledge.txt)")
    parser.add_argument("--exclude", nargs='+', default=[".gif", ".jpg", ".png", ".pdf"], help="File extensions to exclude")
    args = parser.parse_args()

    if not os.path.isdir(args.project_dir):
        print(f"Error: The directory '{args.project_dir}' does not exist.")
        exit(1)

    output = "<documents>\n"
    processed_files = 0
    total_files = 0
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_paths_txt = os.path.join(script_dir, args.file_paths)

    with open(file_paths_txt, 'r') as path_file:
        file_paths = path_file.readlines()
        total_files = len(file_paths)
        for relative_path in file_paths:
            relative_path = relative_path.strip()
            if relative_path:
                file_path = os.path.join(args.project_dir, relative_path)
                print(f"Processing: {file_path}")
                if os.path.exists(file_path):
                    if os.path.isfile(file_path) and not any(file_path.endswith(ext) for ext in args.exclude):
                        metadata = get_file_metadata(file_path)
                        content = read_file(file_path)
                        git_info = get_git_info(file_path)
                        
                        output += f"<document index=\"{processed_files + 1}\">\n"
                        output += f"<source>{relative_path}</source>\n"
                        output += f"<metadata>\n"
                        output += f"<last_modified>{metadata['last_modified']}</last_modified>\n"
                        output += f"<size>{metadata['size']}</size>\n"
                        for key, value in git_info.items():
                            output += f"<{key}>{value}</{key}>\n"
                        output += f"</metadata>\n"
                        output += f"<document_content>{content}</document_content>\n"
                        output += f"</document>\n\n"
                        processed_files += 1
                    else:
                        print(f"Skipping directory or excluded file: {file_path}")
                else:
                    print(f"File not found: {file_path}")

    output += "</documents>"

    output_file_path = os.path.join(script_dir, args.output)
    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        output_file.write(output)

    print(f"Project knowledge has been compiled in '{output_file_path}'")
    print(f"Processed {processed_files} out of {total_files} files.")

if __name__ == "__main__":
    main()
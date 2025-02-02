# git_operations.py

import subprocess
import random
from datetime import datetime

def get_unstaged_files(repo_path):
    """Get the list of unstaged files in the repository."""
    result = subprocess.run(['git', 'status', '--porcelain'], capture_output=True, text=True, cwd=repo_path)
    unstaged_files = [line.split()[1] for line in result.stdout.splitlines() if line.startswith('??') or line.startswith(' M')]
    return unstaged_files

def commit_random_file(repo_path):
    """Commit a random unstaged file in the repository."""
    unstaged_files = get_unstaged_files(repo_path)
    
    if not unstaged_files:
        print(f"No unstaged files to commit in {repo_path}.")
        return None
    
    # Select a random file from the unstaged files
    file_to_commit = random.choice(unstaged_files)
    
    # Add the file to the staging area
    subprocess.run(['git', 'add', file_to_commit], cwd=repo_path)
    
    # Commit the file
    commit_message = f"Automated commit of {file_to_commit} at {datetime.now()}"
    subprocess.run(['git', 'commit', '-m', commit_message], cwd=repo_path)
    
    print(f"Committed {file_to_commit} in {repo_path} with message: {commit_message}")
    return commit_message

def check_and_commit(repo_path):
    """Check if there are any commits today and commit a random file if not."""
    result = subprocess.run(['git', 'log', '--since=midnight', '--oneline'], capture_output=True, text=True, cwd=repo_path)
    
    if not result.stdout.strip():
        # No commits today, proceed to commit a random file
        commit_message = commit_random_file(repo_path)
        if commit_message:
            return f"Auto-commit performed in {repo_path}:\n{commit_message}"
        else:
            return f"No unstaged files to commit in {repo_path}."
    else:
        return f"There are already commits today in {repo_path}. Skipping commit."
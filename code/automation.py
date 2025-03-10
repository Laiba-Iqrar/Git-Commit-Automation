# automate.py

import random
from datetime import datetime
from git_operations import check_and_commit
from email_notifications import send_email
from config import REPO_PATHS

def job():
    print(f"Running scheduled job at {datetime.now()}")
    
    # Randomly select a repository
    repo_path = random.choice(REPO_PATHS)
    print(f"Selected repository: {repo_path}")
    
    # Check and commit in the selected repository
    commit_status = check_and_commit(repo_path)
    
    # Send email with commit status
    subject = "Daily Commit Status Report"
    body = f"Commit status for {datetime.now()}:\n{commit_status}"
    send_email(subject, body)

if __name__ == "__main__":
    job()
# GIT Useful Commands

git clone git@github.com:andrefsmelo/python-100days-vim
cd python-100days-vim  # Access the cloned repository

git branch  # Check the current branch

git checkout -b day-01  # Create the day-01 branch and switch to it

git add .  # Stage the changes

git commit -m "Day 1 - First Commit"  # Commit the changes

git push origin day-01  # Push the day-01 branch to the remote repository

git checkout main  # Switch back to the main branch

git merge day-01  # Merge the day-01 branch into main

git pull origin main  # Update the main branch with the latest changes from remote

git push origin main  # Push the changes to the remote repository

git branch -d day-01  # Delete the local day-01 branch

git push origin --delete day-01  # Delete the remote day-01 branch (optional)

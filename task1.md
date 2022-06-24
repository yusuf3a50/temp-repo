TASK 1 (Git and GitHub)

Question 1
Complete definitions for key Git & GitHub terminology

GIT WORKFLOW FUNDAMENTALS
· Working Directory
This is the location within a file system tree from where a process is run.

· Staging Area
This is essentially a snapshot of the file(s) ready to be committed. When you run 'git add *' you have added everything within the working directory to the staging area, it is then a snapshot, ready to be committed to your remote repo using the 'git commit' command. You can also run 'git add [filename]', adding any [filename] to the snapshot, AKA staging area.

· Local Repo (head)
This is a repository or file(s) which are located on your own computer (i.e. locally)

· Remote repo (master)
This is a repository or file(s) which are located on github's servers and are either privately or publicly accessible on the github website.

WORKING DIRECTORY STATES:
· Staged
The 'git add' command has been run, the snapshot has been taken but 'git commit' hasnt yet been run, thus the snapshot is yet to be uploaded. The file(s) may already exist on the remote repo but an updated version exists within the snapshot or the file(s) do not yet exist on the remote repo, only on the local repo.

· Modified
The file already exists on the remote repo but you have most likely made changes to your own version of the file. Thus when you run 'git add', it will note the modifications you have made to your local version of the file, ready for those modifications to be committed to the remote repo.

· Committed
The 'git commit' command has been run, thus updating the files on the remote repo.

GIT COMMANDS:
· Git add
(see above) this sets up the staging area and adds the files or the modifications of files to the index, ready to be sent to the remote repo.
· Git commit
This records the changes to the repository and provides a opportunity to add a comment to this commit, for example "adding annotations to code"
· Git push
This command sends the added or modified files to the remote repo, thus updating it.
· Git fetch
This receives any missing objects from another repository
· Git merge
Practice this command with caution! You can make a branch of a repo to work on it on your own. Then when you are ready, you can then reintegrate your work into the original branch, thus merging the two or more files back together again. 
· Git pull
This fetches files or modifications of files from anothe repo and integrates your repo with the other one.
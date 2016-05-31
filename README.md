# pythoncloud9

Using GitHub.

Link: https://services.github.com/kit/downloads/github-git-cheat-sheet.pdf


MAKE CHANGES
Review edits and craf a commit transaction
1. $ git status
    Lists all new or modified files to be commited
2. $ git add [file]
    Snapshots the file in preparation for versioning
3. $ git reset [file]
    Unstages the file, but preserve its contents
4. $ git diff
    Shows file differences not yet staged
5. $ git diff --staged
    Shows file differences between staging and the last file version
6. $ git commit -m "[descriptive message]"
    Records file snapshots permanently in version history


SYNCHRONIZE CHANGES
Register a repository bookmark and exchange version history
7. $ git fetch [bookmark]
    Downloads all history from the repository bookmark
8. $ git merge [bookmark]/[branch]
    Combines bookmark’s branch into current local branch
9. $ git push [alias] [branch]
    Uploads all local branch commits to GitHub
10 $ git pull
    Downloads bookmark history and incorporates changes
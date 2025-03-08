 of Github

 Hereâ€™s a list of essential **GitHub** and **Git** commands with descriptions:  

 ---

 ## **1. Git Configuration**
 | Command | Description |
 |---------|------------|
 | `git config --global user.name "Your Name"` | Set your name for commits. |
 | `git config --global user.email "your-email@example.com"` | Set your email for commits. |
 | `git config --global --list` | Show current Git configuration. |
 | `git config --global core.editor "vim"` | Set the default text editor. |

 ---

 ## **2. Repository Setup**
 | Command | Description |
 |---------|------------|
 | `git init` | Initialize a new Git repository. |
 | `git clone <repo_url>` | Clone an existing GitHub repository. |
 | `git remote add origin <repo_url>` | Connect local repo to a remote GitHub repository. |
 | `git remote -v` | View connected remote repositories. |

 ---

 ## **3. Basic Git Operations**
 | Command | Description |
 |---------|------------|
 | `git status` | Check the status of the working directory. |
 | `git add <file>` | Add a specific file to staging. |
 | `git add .` | Add all changes to staging. |
 | `git commit -m "commit message"` | Commit staged changes with a message. |
 | `git commit --amend -m "new message"` | Amend the last commit message. |

 ---

 ## **4. Branching**
 | Command | Description |
 |---------|------------|
 | `git branch` | List all branches. |
 | `git branch <branch_name>` | Create a new branch. |
 | `git checkout <branch_name>` | Switch to a different branch. |
 | `git switch <branch_name>` | Alternative command to checkout a branch. |
 | `git checkout -b <branch_name>` | Create and switch to a new branch. |
 | `git merge <branch_name>` | Merge a branch into the current branch. |
 | `git branch -d <branch_name>` | Delete a branch. |

 ---

 ## **5. Pushing and Pulling**
 | Command | Description |
 |---------|------------|
 | `git push origin <branch_name>` | Push local commits to GitHub. |
 | `git push -u origin <branch_name>` | Push and set upstream tracking for a branch. |
 | `git push --force` | Force push (overwrite remote changes). |
 | `git pull origin <branch_name>` | Pull the latest changes from a remote branch. |

 ---

 ## **6. Stashing Changes**
 | Command | Description |
 |---------|------------|
 | `git stash` | Save uncommitted changes temporarily. |
 | `git stash list` | Show a list of stashed changes. |
 | `git stash apply` | Apply the last stashed changes. |
 | `git stash drop` | Delete the last stash. |

 ---

 ## **7. Undoing Changes**
 | Command | Description |
 |---------|------------|
 | `git reset HEAD <file>` | Unstage a file. |
 | `git reset --hard HEAD~1` | Undo the last commit (permanently). |
 | `git revert <commit_id>` | Create a new commit that undoes a previous commit. |

 ---

 ## **8. Checking Commit History**
 | Command | Description |
 |---------|------------|
 | `git log` | Show commit history. |
 | `git log --oneline --graph` | Show history in a compact format. |
 | `git show <commit_id>` | Show details of a specific commit. |

 ---

 ## **9. Working with Tags**
 | Command | Description |
 |---------|------------|
 | `git tag` | List all tags. |
 | `git tag -a v1.0 -m "Version 1.0"` | Create a new annotated tag. |
 | `git push origin --tags` | Push tags to GitHub. |

 ---

 ## **10. GitHub-Specific Commands**
 | Command | Description |
 |---------|------------|
 | `gh auth login` | Authenticate GitHub CLI. |
 | `gh repo create <repo_name>` | Create a new repository on GitHub. |
 | `gh pr create` | Create a pull request from the CLI. |
 | `gh issue list` | List issues in a GitHub repository. |

 ---

 ### íº€ **Common Workflows**
 1. **Clone a repo & start working**  
    ```sh
       git clone <repo_url>
          cd repo_name
             git checkout -b new-feature
                git add .
                   git commit -m "Added a new feature"
                      git push origin new-feature
                         ```

                         2. **Merge feature branch into `main`**  
                            ```sh
                               git checkout main
                                  git pull origin main
                                     git merge new-feature
                                        git push origin main
                                           ```

                                           3. **Revert to a previous commit**  
                                              ```sh
                                                 git reset --hard <commit_id>
                                                    ```

                                                    Let me know if you need a deep dive into any of these commands! íº€

                                                    Practice of Github

Hereâ€™s a list of essential **GitHub** and **Git** commands with descriptions:  

---

## **1. Git Configuration**
| Command | Description |
|---------|------------|
| `git config --global user.name "Your Name"` | Set your name for commits. |
| `git config --global user.email "your-email@example.com"` | Set your email for commits. |
| `git config --global --list` | Show current Git configuration. |
| `git config --global core.editor "vim"` | Set the default text editor. |

---

## **2. Repository Setup**
| Command | Description |
|---------|------------|
| `git init` | Initialize a new Git repository. |
| `git clone <repo_url>` | Clone an existing GitHub repository. |
| `git remote add origin <repo_url>` | Connect local repo to a remote GitHub repository. |
| `git remote -v` | View connected remote repositories. |

---

## **3. Basic Git Operations**
| Command | Description |
|---------|------------|
| `git status` | Check the status of the working directory. |
| `git add <file>` | Add a specific file to staging. |
| `git add .` | Add all changes to staging. |
| `git commit -m "commit message"` | Commit staged changes with a message. |
| `git commit --amend -m "new message"` | Amend the last commit message. |

---

## **4. Branching**
| Command | Description |
|---------|------------|
| `git branch` | List all branches. |
| `git branch <branch_name>` | Create a new branch. |
| `git checkout <branch_name>` | Switch to a different branch. |
| `git switch <branch_name>` | Alternative command to checkout a branch. |
| `git checkout -b <branch_name>` | Create and switch to a new branch. |
| `git merge <branch_name>` | Merge a branch into the current branch. |
| `git branch -d <branch_name>` | Delete a branch. |

---

## **5. Pushing and Pulling**
| Command | Description |
|---------|------------|
| `git push origin <branch_name>` | Push local commits to GitHub. |
| `git push -u origin <branch_name>` | Push and set upstream tracking for a branch. |
| `git push --force` | Force push (overwrite remote changes). |
| `git pull origin <branch_name>` | Pull the latest changes from a remote branch. |

---

## **6. Stashing Changes**
| Command | Description |
|---------|------------|
| `git stash` | Save uncommitted changes temporarily. |
| `git stash list` | Show a list of stashed changes. |
| `git stash apply` | Apply the last stashed changes. |
| `git stash drop` | Delete the last stash. |

---

## **7. Undoing Changes**
| Command | Description |
|---------|------------|
| `git reset HEAD <file>` | Unstage a file. |
| `git reset --hard HEAD~1` | Undo the last commit (permanently). |
| `git revert <commit_id>` | Create a new commit that undoes a previous commit. |

---

## **8. Checking Commit History**
| Command | Description |
|---------|------------|
| `git log` | Show commit history. |
| `git log --oneline --graph` | Show history in a compact format. |
| `git show <commit_id>` | Show details of a specific commit. |

---

## **9. Working with Tags**
| Command | Description |
|---------|------------|
| `git tag` | List all tags. |
| `git tag -a v1.0 -m "Version 1.0"` | Create a new annotated tag. |
| `git push origin --tags` | Push tags to GitHub. |

---

## **10. GitHub-Specific Commands**
| Command | Description |
|---------|------------|
| `gh auth login` | Authenticate GitHub CLI. |
| `gh repo create <repo_name>` | Create a new repository on GitHub. |
| `gh pr create` | Create a pull request from the CLI. |
| `gh issue list` | List issues in a GitHub repository. |

---

### ðŸš€ **Common Workflows**
1. **Clone a repo & start working**  
   ```sh
   git clone <repo_url>
   cd repo_name
   git checkout -b new-feature
   git add .
   git commit -m "Added a new feature"
   git push origin new-feature
   ```

2. **Merge feature branch into `main`**  
   ```sh
   git checkout main
   git pull origin main
   git merge new-feature
   git push origin main
   ```

3. **Revert to a previous commit**  
   ```sh
   git reset --hard <commit_id>
   ```

Let me know if you need a deep dive into any of these commands! ðŸš€



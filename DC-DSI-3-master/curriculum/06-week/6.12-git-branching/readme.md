# Git Branching + Workflows

> [Lesson Summary](readme_summary.md)

## Learning Objectives

- Explain what a branch is in git
- Create, merge and delete branches on local and remote repositories
- Describe how branching and merging allows for collaboration during development
- Describe Github Workflows using issues, branches, and pull-requests
- Resolve a merge conflict

## Review (5 min)

Quickly review the basics of git:

<details>
<summary>1. What is the purpose of git? How does it differ from github?</summary>
  ```
  Git is a version control system allowing us to easily track files, manage changes, and move between versions. Github is a web application that hosts remote repositories and allows developers to easily host and share code.
  ```
</details>

<details>
<summary>2. What command is used to start tracking a directory? What commands record the changes that occurred in the tracked directory?</summary>
  <br>
  ```
  1. $ git init - create empty Git repo
  2. $ git add <file-name> - stage file(s) for commit
  3. $ git commit -m "commit message" - commit staged files
  ```
</details>

<details>
<summary>3. What's the difference between a fork and a clone?</summary>

  ```
  A fork is a copy of a repository on github, a clone is a copy of a remote available locally.
  ```

</details>

<details>
<summary>4. What commands are used to share changes (commits) between local and remote repos?</summary>
  <br>
  ```
  1. $ git remote add <remote_name> <repo_url> - add remote repo
  2. $ git push origin master - sync remote repo with local
  3. $ git pull origin master - sync local repo with remote
  ```
</details>


## Framing - Why Branch? (5 min)

> Say you are working on a paper. You’ve gotten a first draft out, submitted for review. You then get a new batch of data, and you’re in the process of integrating it into the paper. Halfway in, however, the review committee calls you up and tells you that you need to change some of your section headings to conform to format specifications. What do you do? [1](http://www.sbf5.com/~cduan/technical/git/git-2.shtml)

### Think/Pair/Share -1/2/2: What can you do? (5 min)

Take a minute to brainstorm some options for what could be done here, then share with your neighbor, and we'll share what we feel is important.

## How Git Branching Works (10 min)

In Git, branches are a part of your everyday development process. When you want to add a new feature or fix a bug—no matter how big or how small—you spawn a new branch to encapsulate your changes. This makes sure that unstable code is never committed to the main code base, and it gives you the chance to clean up your feature’s history before merging it into the main branch [2](https://www.atlassian.com/git/tutorials/using-branches).

Branches are incredibly lightweight "movable pointers" that help us as developers make experimental changes! A branch in git is just a label or pointer to a particular commit in a repository, along with all of it's history (parent commits).

What makes a branch special in git, is that we're always *on* a specific branch, and when we commit, the current branch HEAD moves forward to the new commit. Another way to say that is the HEAD always stays at the tip of the branch.

**Terminology:** HEAD is simply a reference to the current or most recent commit!

![Git Branch Diagram](branching.png)

> The diagram above visualizes a repository with multiple lines of development, one is the master branch, and the others are feature branches. By developing in branches, it’s not only possible to work on branches in parallel, but it also keeps the main master branch free from questionable code.

---

## Why Branch (5 mins)

<details>
<summary>Q. Why is branching an important part of git?</summary>
<br>

> Branches are useful for many reasons, but some of the most common ones:

> 1. To allow experimentation. By switching to a new branch, we can experiment,
and if the experiment fails, we can delete it and easily switch back to master
(or another branch of our choice). If it succeeds, we can merge those changes
into master.
2. To allow work to proceed on multiple features (or by multiple people) without
interfering. When a feature is complete, it can be merged back into master.
3. To allow easy bug fixes on a stable version while features are being developed.
4. "Branch Early, Branch Often": Branches are lightweight, there is no additional overhead associated with branches, so it can be a great way to organize our workflow

</details>

---

## Merging (5 min)

Now imagine that we have completed our awesome feature on its own branch and we want to bring those changes back into `master`, we now need a way to consolidate these two versions of our code base. The easiest way to do this is by  **merging** the feature branch into the master branch.

Let's see what this process looks like visually:

![before-merge](merging.png)

***Locally***, all we need to do is check out the master branch and then run the git merge command to integrate our feature branch:

```
$ git merge <feature_branch_name>

```
Once merged, you can delete the branch:

```
$ git branch -d <feature_branch_name>

```
***Remotely***, we could easily merge our branch back into master through a PR and delete the branch on Github.

### You Do: Branching Exercise (15 min)

We are going to start with a [brief tutorial](http://learngitbranching.js.org/).  This is an introduction to branching.

- Do Levels 1-3.  Stop at 4: "Rebase Introduction".
- Take your time:
  - Read all the dialogs.  They are part of the tutorial.
  - Think about what you want to achieve
  - Think about the results you expect *before* you press enter.
- Whenever you see/type `git commit`, it may help to assume changes have been made and staged.  Why else would you "commit"?

> Please run this exercise using Chrome. It will not work propertly in Safari or Firefox.

---

## Break (10 min)

---

## Common Commands for Managing Branches (5 min)

* `git branch <new_branch_name>` - create a new branch
* ⭐`git checkout <branch_name>` - switch to a specific branch (checks out tip commit and makes branch active)
* ⭐`git checkout -b <new_branch_name>` - create a new branch and check it out in one step
* `git branch` - list local branches
* `git branch -r` list remote branches
* `git branch -a` list both remote & local branches
* `git branch -d <branch_to_delete>` - delete a branch
  * will not let you delete if branch isn't merged into another branch (i.e. would cause data loss)
  * `git branch -D <branch_to_delete>` - over-rides and deletes a non-merged branch - **be careful!**
* ⭐`git merge <branch_name>` - merges `<branch_name>` into the current branch, creating a new merge commit in the process

[My favorite cheat Sheet](http://ndpsoftware.com/git-cheatsheet.html)

## Overview of a GitHub Workflow (10 min)
> From [Github Guides](https://guides.github.com/introduction/flow/)

To Recap, in Software Development, Github is very useful in managing and tracking updates and changes to our code.

![Github Workflows](github_workflows.jpg)

#### Discuss

Discuss an idea for a new feature or any question about our project/application with our team and agree on what needs to be done.

#### Create an Issue

An Issue is a note on a repo regarding some matter that needs attention. It could be a bug, a suggestion for a new feature, a question about the repo or code, etc! On GitHub you can also label, search and assign issues, which help with managing projects.

It can be useful to write the issue as short functional spec, documenting the requirements as user stories.

[Issue for simple feature on Garnet](https://github.com/ga-dc/garnet/issues/522)

#### Create a Branch

Create a feature branch off the master to work on this issue. Our branch name should have meaning to the issue we are working on.

```
$ git checkout -b [name of branch that solves issue]

```
#### Work on your Branch and Commit Locally

Make changes/commits commits locally, then push your branch up to our remote repository

#### Open a Pull-Request or PR

By making a PR, you’re requesting that someone pull in your changes and merge them into their branch. A PR allows you to compare the content on two branches, and all the changes or diffs (differences) are highlighted in green and red.

As soon as you make a change, you can open a Pull Request. People use Pull Requests to start a discussion about commits (code review) even before the code is finished. This way you can get feedback as you go or help from other developers/team members!

[PR for simple Garnet feature](https://github.com/ga-dc/garnet/pull/549)

#### Merge Branch into Master

It's good practice to even make a Pull Request for branches in your own repository and merge it yourself to get more comfortable with PRs!

### We Do: Branching, Merging, and PRs (10 min)

Many OSS projects request that you create pull requests from a non-master branch.

1. Fork and Clone https://github.com/ga-wdi-exercises/git-tricks.
2. Create and switch to a branch called `<your_name>_suggestion`.
3. Add your own "trick" aka git command/functionality you just learned (or researched) about.
4. Commit, and then checkout to master
5. Merge changes from your feature branch back into master
6. Push your master branch to your remote called 'origin' (your fork)
7. Create a pull request from your master to the upstream (ga-wdi-exercises) master branch

## Merge Conflicts (10 min)

PLEASE NOTE: Merging does not always go smoothly, but don't be scared!

```
Auto-merging <file_name>
CONFLICT (content): Merge conflict in <file_name>
Automatic merge failed; fix conflicts and then commit the result.

```
When we try to merge two branches (or commits from the same branch from a remote), changes may conflict. In this case, git will stop and ask us to fix the issues manually.

A ‘conflict’ occurs when the commit that has to be merged has some change in the same place as the current commit.

To do so:

1. Locate which files contain conflicts using `git status`
2. Open those files and fix the conflicts. (Look for the '<<<<', '====', and '>>>>' which will guide you to the conflict)
3. Commit the fixes.

```
<<<<<<< HEAD:file.txt
This is the original text in your current branch
=======
This is the modified text
>>>>>>> 77976da35a11db4580b80ae27e8d65caf5208086:file.txt

```
>The HEAD is a reference to the last commit in your current checked out branch. Anything between <<<<< HEAD and ===== is the original code from your checked out branch, while anything beneath from ===== to >>>>>> are the changes introduced by the commit you are trying to merge

## Break (10 min)

## You Do, 1-2 Pairs: Merge Conflicts (25 min)

1. Pair up with someone.
- Pick someone as the 'primary', and the 'secondary'.

2. Create a New Repo

  **Primary** Student Instructions:
  - In your `~wdi/sandbox` directory, create a new directory named `merge-conflicts`.
  - Initialize merge-conflicts as a git repository and create an `index.html` file
  - Work with the Secondary student to fill out the basic structure for the `index.html` file.
  -Include in the `index.html` file an `h1` tag with the content "Merge Conflicts", and a `p` tag with something new you learned about today.
  - Create a New Repo on Github called `merge-conflicts` and add this repo locally as a remote repo for your merge-conflicts directory.
  - Make sure to save and commit local changes and push up to the Remote Repo
  - Add the Secondary student as a Collaborator (search github for how to do this)

  **Secondary** Students Instructions:
  - After they are added as a Collaborator, they should clone the same repo. Do not fork the Repo.

3. Both the Primary and Secondary should make changes locally on the same "master" branch
  - Modify the `index.html`, including both changing the `h1` and `p` elements
  - Add and Commit Changes Locally.

5. Merging commits:
  - The Primary Student should push up their changes first
  - Then, the Secondary Student should do the same and try pushing up their changes

6. Merge conflicts:
  - When the Secondary Student tries to push their commits, there should be merge conflicts.
  - The Secondary Student should work locally (with the Primary) to resolve the merge conflicts.
  - Once completed, commit and push up changes to the remote repo

7. Pulling Changes:
  - Now, the Primary student should pull down the changes from the remote repo and work to resolve any merge conflicts

## Closing (5 min)

Review Learning Objectives:
* Explain what a branch is in git
* Create, merge and delete branches on local and remote repositories
* Describe how branching and merging allows for collaboration during development
* Describe Github Workflows using issues, branches, and pull-requests
* Resolve a merge conflict

Quiz Questions:
* What is a feature branch in Git?
* How can you check what branch your are currently working in?
* How can you bring a new feature in the main branch?
* What is a conflict in git? How can a conflict be resolved?

### Homework

From this point on, all homework submissions should be a pull request from a feature (or 'topic') branch, named `<your_name>_solution`.

## References & Additional Resources

* [Common Git Errors](https://github.com/ga-wdi-lessons/git-review/blob/master/readme.md)
* [Git-Guide](http://rogerdudler.github.io/git-guide/)
* [Atlassian - Git Merging versus Rebasing](https://www.atlassian.com/git/tutorials/merging-vs-rebasing/)
* [Github - Git-Command-Cheat-Sheet](https://education.github.com/git-cheat-sheet-education.pdf)
* [Git Book - Git Branching - Basic Branching and Merging](https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging)
* [Atlassian - Git Branching Tutorial](https://www.atlassian.com/git/tutorials/using-branches)
* [Interactive Git Branching Tutorial](http://pcottle.github.io/learnGitBranching/)
* [Git Cheat Sheet](http://ndpsoftware.com/git-cheatsheet.html)

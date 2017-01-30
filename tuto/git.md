# Gérer son code avec Git et GitHub

[Cours Openclassrooms](https://openclassrooms.com/courses/gerer-son-code-avec-git-et-github)

## Premiers pas avec Git

### Qu'est-ce que versionner son code ?

*commit :* création de fichier, suppression de fichier, ajout de texte... dans git
-> constitue un historique

### Git par rapport aux autres solutions de versioning

- Modèle centralisé : serveur central base de code (SVN, CVS)
- Modèle distribué : type peer to peer (intégralité des infos sur chaque machine) (GIT, Mercurial, Bazaar)
    - Moins de risques de perdre son code
    - Opérations plus rapide
    - Pas besoin de connexion internet obligatoire

### Faire son premier commit

`git status` : afficher le statut du repository (si répertoire non repository -> erreur)
`git init` : déclarer le répertoire courant comme un repository git

TP :

    $ git status
        fatal: Not a git repository (or any of the parent directories): .git

    $ git init
        Initialized empty Git repository in C:/Users/TOTO/Documents/formation/git/.git/

    $ git status
        On branch master

        Initial commit

        nothing to commit (create/copy files and use "git add" to track)

    $ touch test.md

    $ git status
        On branch master

        Initial commit

        Untracked files:
          (use "git add <file>..." to include in what will be committed)

                test.md

        nothing added to commit but untracked files present (use "git add" to track)

    $ git add test.md

    $ git status
        On branch master

        Initial commit

        Changes to be committed:
          (use "git rm --cached <file>..." to unstage)

                new file:   test.md

    $ git commit -m "ajout fichier test.md"
        [master (root-commit) 29f061e] ajout fichier test.md
         1 file changed, 0 insertions(+), 0 deletions(-)
         create mode 100644 test.md

    $ git status
        On branch master
        nothing to commit, working directory clean

### Lire l'historique

`git log`

Lorsqu'on fait une modification sur un fichier il faut l'ajouter à la liste des fichiers à embarquer dans le prochain commit avec `git add`. On peut embarquer tous les fichiers modifiés lors du commit avec l'option -a même si le `git add` n'a pas été effectué : `$ git commit -a -m "commit tous les fichiers modifiés"`

### Se positionner sur un commit donné

`git checkout [SHA]`

TP :

    $ git log
        commit bbc5ad8568684c7e8cf66b9a2005555b1914a768
        Author: Toto <toto@mail.com>
        Date:   Wed Jan 27 07:59:05 2016 +0100

            test3

        commit f91fb67c189b7fc432a16885bfec9ccde094553c
        Author: Toto <toto@mail.com>
        Date:   Wed Jan 27 07:58:30 2016 +0100

            test2

        commit 52aef346d02e1fb3a4983b517ee1fbee63bfce3a
        Author: Toto <toto@mail.com>
        Date:   Wed Jan 27 07:56:57 2016 +0100

            test1

    $ git checkout f91fb67c189b7fc432a16885bfec9ccde094553c
        Note: checking out 'f91fb67c189b7fc432a16885bfec9ccde094553c'.

        You are in 'detached HEAD' state. You can look around, make experimental
        changes and commit them, and you can discard any commits you make in this
        state without impacting any branches by performing another checkout.

        If you want to create a new branch to retain commits you create, you may
        do so (now or later) by using -b with the checkout command again. Example:

          git checkout -b <new-branch-name>

        HEAD is now at f91fb67... test2

    $ git log
        commit f91fb67c189b7fc432a16885bfec9ccde094553c
        Author: Toto <toto@mail.com>
        Date:   Wed Jan 27 07:58:30 2016 +0100

            test2

        commit 52aef346d02e1fb3a4983b517ee1fbee63bfce3a
        Author: Toto <toto@mail.com>
        Date:   Wed Jan 27 07:56:57 2016 +0100

            test1

    $ cat test.md
        "toto"

    $ git checkout master
        Previous HEAD position was f91fb67... test2
        Switched to branch 'master'

    $ cat test.md
        "toto"
        tata

## Apprendre à utiliser GitHub

### Comprendre les remotes

Sauvegarder son code à un endroit distant (backup sur une autre machine) : `git remote`

### GitHub

[GitHub](https://github.com) Création d'un compte

### Récupérer du code d'un autre repository

Clone : (Récupérer l'url de clone d'un projet github public)

Sur son poste : dans un répertoire `git clone [clone_url]` récupère le repository du projet

### Créer son premier repository

Création dans github

Récupération du projet en local par l'url de clone (voir § précédent)

### Envoyer son code sur GitHub

Modification d'un fichier du projet récupéré sur github précédemment et envoi :

    $ git add [fichier]
    $ git commit -m "modif fichier"
    $ git push origin master

Envoi des modifications sur un remote : `git push [remote_name] [branch]`
    - origin nom du remote github du projet (convention)
    - master : branche principale

### Récupérer des modifications

Récupération des modifications : `git pull [remote_name] [branch]

Ex récupération des modif depuis le remote github :

    $ git pull origin master

## Collaborer et maitriser son historique

### Créer des branches

Voir la branche sur laquelle on est : `git branch`  -> initiale = master (* indique la branche en cours)
Créer une branche : `git branch [nom_branche]`
Changer de branche : `git checkout [nom_branche]`

Créer une branche et s'y positionner immédiatement : `git checkout -b [nom_branche]`

### Fusionner des branches

Se positionner dans la branche dans laquelle on souhaite rapatrier les modification d'une branche puis : `git merge [nom_branche]`

### Résoudre un conflit

Le fichier en conflit se présente de la façon suivante :

```
    <<<<<<< HEAD
    texte dans master
    =======
    texte dans nom_branche
    >>>>>>> [nom_branche]
```

Editer le fichier pour résoudre le conflit.

`git add [fichier]` : le conflit a été résolu
`git commit` : sans message en paramètre : le message est généré automatiquement par le merge (ouvert dans l'editeur de texte).

### Savoir qui a fait une modification

`git blame [fichier]` : liste de toutes les modification du fichier
`git show [SHA_COMMIT]` : affiche le diff lié au commit passé en paramètre.

### Ignorer des fichiers

Créer un fichier .gitignore dans lequel on liste les fichiers à ignorer.

### Eviter des commits superflus

`git stash` : permet de mettre de côté son travail en cours mais sans le commiter (pour effectuer une modification plus urgente par exemple)
`git stash pop` : permet de récupérer ce qui avait été mis de côté par git stash

git stash permet également de garder ses modifications lorsqu'on doit changer de branche (git checkout)

### Contribuer à des projets open source

- Dans github faire un fork du projet dans son propre repository.
- En local git clone pour récupérer le projet
- Faire ses modifications (en respectant les consignes propres au projet)
- Envoyer ses modifications sur github
- Depuis github "compare and pull request"

---

# Pro GIT 2nd Edition

[Livre Pro GIT](http://git-scm.com/book/en/v2)

## Getting Started

### About Version Control

- Local Version Control : local simple database keeping changes (ex: *rcs*)
- Centralized Version Control : central VCS Server keeping changes (ex: *svn*, *cvs*)
- Distributed Version Control : clients fully mirror the repository. Each client keep all changes (ex: *git*, *mercurial*)

### A Short History of Git

Birth in 2005 from Linux kernel community.

Goals :

- Speed
- Simple design
- Strong support for non linear dev (thousands of parallel branches)
- Fully distributed
- Able to handle large projects (linux kernel)

### Git basis

#### Snapshots, Not Differences

Different from other VCS which keep changes from a file.

Git thinks of its data like a set of snapshots of a miniature filesystem. Every time you commit, it basically takes a picture of what all your files look at the moment and stores a reference to that snapshot. (If file has no change, git link to a previous identical file already stored).

>Git thinks about its data more like a **stream of snapshots**.

#### Nearly Every operation is local

Browse history

Local diff between versions

#### Git Has Integrity

Everything is check-summed (SHA-1)

#### Git Generally Only Add Data

Git only add data to the Git database avoiding losing actions.

#### The Three State

File can reside in 3 main states :

- **Committed**  : data is safely stored in the local database
- **Modified** : file has been changed but not committed to the database
- **Staged** : a modified file has been marked in its current version to go into the next commit snapshot

```
WORKING DIRECTORY     STAGING AREA     .git directory (Repository)
       |                     |                       |
       |#--------------------------------------------|
       |                Checkout the project         | 		 
       |                     |                       |
       |                     |                       |
       |--------------------#|                       |
       |   Stage fixes       |                       | 		 
       |                     |                       |
       |                     |                       |
       |                     |----------------------#|
       |                     |        Commit         | 		 
       |                     |                       |
```

Basic Git Workflow :

1. Modify files in working directory
2. Stage the files, adding snapshots of them to the staging area
3. Do a commit, storing files of the staging area in git directory

### Installing Git

[Download linux](http://git-scm.com/download/linux)

[Download win](http://git-scm.com/download/win)

Récupérer les sources Git par Git pour mise à jour : `git clone git://git.kernel.org/pub/scm/git/git.git`

### First Time Git Setup

Set configuration variables : `git config`

Variables can be stored in three different places :

1. `/etc/gitconfig` : Values for every user on the system. Variables set with `git config --system`
2. `~/.gitconfig` or `~/.config/git/config` : Values specific to the user. `git config --global`
3. `config` file in the git directory (`.git/config`) : Values specific to that single directory

Identity - name : `git config --global user.name "John Doe"`

Identity - mail : `git config --global user.email johndoe@example.com`

Editor : `git config --global core.editor emacs`

Checking Config : `git config --list`

Checking Config for a specific key :`git config <key>` (ex: `git config user.name`)

Getting Help : `git help <verb>` (ex : `git help config`)

## Git Basics

### Getting a Git Repository

Two main approaches :

1. Initialize a Repository in an existing directory : Go to the project directory : `git init`. It Creates a new subdirectory .git. At this point nothing is tracked yet. To start version controlling files : add files and do an initial commit.
	- `git add *.c`
	- `git add LICENSE`
	- `git commit -m 'Initial project version'`
2. Clone an existent Repository : `git clone https://github.com/libgit2/libgit2 mylibgit` : clone libgit2 project in mylibgit directory (optional)

### Recording changes to the repository

#### Lifecycle of the status of files

```
UNTRACKED    UNMODIFIED    MODIFIED    STAGED
    |             |            |          |
    |------------------------------------#|	 
    |           Add the file   |          |
    |             |            |          |
    |             |-----------#|          |	 
    |             |   Edit     |          |
    |             |            |          |
    |             |            |---------#|	 
    |             |            |  Stage   |
    |             |            |          |
    |#------------|            |          |	 
    | Remove file |            |          |
    |             |            |          |
    |             |#----------------------|	 
    |             |          Commit       |
    |             |            |          |
```

- Checking the status of files : `git status`
- Tracking new files : `git add <file>`
- Staging modified files : `git add <file>`

#### Short status

`git status -s`

ex:

```
$ git status -s

 M README
MM Rakefile
A  lib/git.rb
M  lib/simplegit.rb
?? LICENSE.txt
```

?? => not tracked file
A => Added file
M on left column => Modified and staged
M on the right column => Modified
MM => Modified and staged then modified

#### Ignoring files

Configuration in file .gitignore

#### Viewing staged and unstaged changes

- `git diff` : show only changes that haven't been yet staged
- `git diff --staged` : compares staged changes to the last commit (--staged or --cached)

> To use an external diff tool : `git difftool`
> `git difftool --toolhelp` : see what tool is available on the system

#### Committing changes

`git commit` : Commit changes in the staging area.

Each time you commit, you're recording a snapshot of your project that you can revert to or compare to later.

#### Skipping the staging area

`git commit -a`

#### Removing files

- rm file from working directory
- then `git rm`

If the file was already modified or added : `git rm -f`

To remove a file from git track but keep it in the working tree : `git rm --cached <file>`

#### Moving files

`git mv file_from file_to`

Equivalent to :
```
mv file_from file_to
git rm file_from
git add file_to
```

### Viewing the commit history

`git log` : lists the commit in the repository in reverse chronological order.

ex: `git log -p -2`

`-p` show differences introduces in each commit
`-2` limits the histroy to the two last entries

`git log --stat` : show statistics
`git log --pretty` : enable custom format for the output of git log
`git log --since` : limit the date (since=2.weeks)
`git log --grep` : grep the commit message

### Undoing things

To add a forgotten file to the last commit : `git commit --amend`

Unstaging a staged file : `git reset HEAD <file>`

Unmodifying a modified file : `git checkout -- <file>`

### Working with remotes

Remote repositories are versions of the project that are hosted on the Internet or network.

Showing remotes servers : `git remote`. `-v` show urls.

Adding remote repositories : `git remote add [shortname] [url]`

Fetching remote : `git fetch [remote-name]` : Pulls the data to the local repository but don't merge it with local work. Merging must be done manually.

Pulling remote : `git pull` : Fetch and merge a remote branch into current branch.

Pushing to remote : `git push [remote-name] [branch-name]`

Inspecting a remote : `git remote show [remote-name]`

Renaming remote : `git remote rename <remote-name-from> <remote-name-to>`

Removing remote : `git remote rm <remote-name>`

### Tagging

List tags : `git tag`

`git tag -l 'expr'`  grep expr in tag

Two sorts of tags :

- Lightweight tag : pointer to a specific commit
- Annotated tag : full object in Git database (checksummed, taggername, email, message, can be signed)

Create annotated tag : `git tag -a <tagname> -m 'message'`

Create lightweight tag : `git tag <tagname>`

Create a tag on specific commit : `git tag -a <tagname> <checksum_commit>` use the checksum or part of checksum of the commit (shown by git log)

`git show <tagname>` displays informations about the tag

Share tag : by default `git push` doesn't transfer tags to remote servers. `git push <remote-name> [tagname]`

In local you can put a version in the working directory by creating a branch at a specific tag : `git checkout -b [branchname] [tagname]

### Alias

```
git config --global alias.co checkout
git config --global alias.br branch
git config --global alias.ci commit
git config --global alias.st status
```

Alias allows creating commands :

ex: `git config --global alias.unstage 'reset HEAD --'` makes the two following commands equivalent :

- `git unstage fileA`
- `git reset HEAD -- fileA`

Useful log alias to see the last commit : `git config --global alias.last 'log -1 HEAD`

## Git branches

### Branches in a Nutshell

ex: initialization of a git repository with 3 files

```
$ git add README test.rb LICENSE
$ git commit -m 'The initial commit of my project'
```

Git repository contains 5 objects : 
    - 3 blobs (file content)
    - 1 tree (directory content, specifies which file names are stored as which blob)
    - 1 commit object (a pointer to the tree with all commit metadata (user, message...)
  
When a new commit is done, it refers to the previous commit as its parent.

> A branch in Git is simply a lightweight movable pointer to one of these commits.

At first commit a branch 'master' is automatically created pointing on the commit and then moved forward at each commit.

#### Creating a branch 

`git branch <branch_name>` 

This creates a new pointer to the current commit, but it doesn't switch to that branch.

To know on which branch it is, git keeps a special pointer called `HEAD`.

To see on which branch we are : `git log --oneline --decorate` 

#### Switching branch

`git checkout <branch_name>`

This moves `HEAD` to the branch.

When changes are made on two branches check the divergent history with `git log --oneline --decorate --graph --all`


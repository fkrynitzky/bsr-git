# BSR Git
Git introductory project for BSR students.

### Preliminary
Be ready to use **command-line**. That said, I leave you complete freedom of
choice when it comes to selecting Git tools. If using GUI plug-in to your
beloved code editor is what best suits your workflow - I'm totally cool with
that. However keep in mind that all resources provided with this tutorial will
refer to bare Git commands. Your interface of choice may - or may not -
implement all features necessary to achieve what you want.

My recommendation is to stick to bare Git command-line tool. Besides forcing the
user to be more focused on what he or she actually does (and not mindlessly
clicking GUI buttons), dealing with command-line interface may just be an
enlightening experience for those of you who got stuck in some [feature overloaded IDE](https://visualstudio.microsoft.com/).

Before you start to actually start coding and using Git:
1. **Read** chapters 1. to 3. from [Git Pro Book](https://git-scm.com/book/en/v2) to get the basic idea of how Git works.
2. **Install** Git on your working rig. Basic installation process is covered in [chapter 1.5](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) of Git Pro Book.
3. Take a look at [a guide to writing commit messages](https://chris.beams.io/posts/git-commit/) and [Gitflow overview](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow). Keep these links under your pillow! Or just bookmark them.

### Task
Programming task coming only after you request it with a specific issue on
GitHub. Note that issues are not part of Git suite. They're feature provided by
GitHub to help collaborate on code. Issues are sort of a message board for
developers - each issue being a specific problem or feature to discuss.
Messages can directly refer to some Git/GitHub entities like commits.

So, what can you do to move forward with Git?

1. Sign in to GitHub.
2. Use [issue section](https://github.com/fkrynitzky/bsr-git/issues) to add new issue requesting me to describe your task. If such issue already exists, mark your presence there by posting a comment or reacting to existing comments.


### The Task

First, watch video about lunar arithmetic:

<a href="http://www.youtube.com/watch?feature=player_embedded&v=cZkGeR9CWbk
" target="_blank"><img src="http://img.youtube.com/vi/cZkGeR9CWbk/0.jpg" 
alt="IMAGE ALT TEXT HERE" width="240" height="180" border="10" /></a>

Secondly - and this is where long-awaited coding and Git learning actually starts - write lunar arithmetic library that implements addition and multiplication. You're free to choose the programming language. Preferably let it be the the one you feel most comfortable with. There are, however, some guidelines you should follow when developing and submitting code.

#### Project guidelines

1. Work on separate branch, dedicated to developing library with language of your choice. Use `git checkout` with `-b` option to create and switch to your branch. Name your branch after the language you chose. So, for example, if you chose Arduino C/C++, you could start your branch using command `git checkout -b arduino-c`.
2. Put your code into a directory named after the language you chose. So, for instance, if you chose Python, create `python/` directory under the top-most project directory and put your code there.
3. Use a separate commit for each feature implemented. That said, there should be at least two commits on each language-specific branch: one for adding addition and second for multiplication.
4. Follow [commit message guideline](https://chris.beams.io/posts/git-commit/). 

To start working, clone this repo to your local machine:

`git clone https://github.com/athleaguerm/awaken-backend.git`

... and start coding!

### FAQ
*Why English?*
We agreed to write documentation of our target project in English. Let's start practicing now.

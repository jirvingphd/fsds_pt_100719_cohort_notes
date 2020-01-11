# fsds_pt_100719_cohort_notes

- Notes for Flatiron School's Data Science Bootcamp cohort online-ds-pt-100719.

## IMPORTANT LINKS

### STUDY GROUP RECORDINGS & NOTES REPOS

- **PART TIME LINKS:**

  - 📺[YOUTUBE STUDY GROUP PLAYLIST: online-ds-PT-100719](https://www.youtube.com/playlist?list=PLFknVelSJiSydTybrkhr3dfRAFCyzAfC6)

  - 📓[STUDY GROUP NOTES REPO: online-ds-PT-100719](https://github.com/jirvingphd/fsds_pt_100719_cohort_notes)

- **FULL TIME LINKS:**

  - 📺[YOUTUBE STUDY GROUP PLAYLIST: online-ds-FT-100719](https://www.youtube.com/playlist?list=PLFknVelSJiSyE_BQomZ8mFFrCfk1H9hfh)

  - 📓[STUDY GROUP NOTES REPO: online-ds-FT-100719](https://github.com/jirvingphd/fsds_100719_cohort_notes)

- **NOTE RE NOTES REPOS:**

  - 🚨**DO NOT FORK NOTES REPO BEFORE CLONING** (to easily get all new notebooks.)

  - Just clone directly and run `git pull` from inside the repo's folder in your terminal to get the new notebooks.

### RESOURCES FOLDER

- 🗂[STUDENT RESOURCES GOOGLE DRIVE FOLDER](https://drive.google.com/drive/folders/1E3JBOl0uhLMRKvl9R5vpl6xaxchiJ6JA?usp=sharing)
  - See  Student Resources Section farther down the page for details.

## CONTACT INFO

### Your Instructor/Cohort Lead

> **James M Irving, Ph.D.**<br><br>
💬[Slack DM (@James Irving)](https://learn-co.slack.com/team/UP0AQ4CUA)<br>
📩[james.irving@flatironschool.com](mailto:james.irving@flatironschool.com)<br>
🗓[Schedule a 1 on 1 Meeting](https://go.oncehub.com/JamesIrvingOfficeHours)<br><br>
👨‍⚖️[My LinkedIn](https://www.linkedin.com/in/james-irving-4246b571/)<br>
💾[My GitHub Profile](https://github.com/jirvingphd)

## STUDENT RESOURCES

### TABLE OF CONTENTS

I. STUDENT RESOURCES GOOGLE DRIVE FOLDER CONTENTS

II. MODULE PROJECT INFO/PROCESS

III. How to: install updated `learn-env`

VI. How to: install and activate Jupyter Notebook Extensions


___

### I. STUDENT RESOURCES GOOGLE DRIVE FOLDER CONTENTS

> Contains a collection of resources, cheatsheets, and official best-of collection of study group videos in a gsheet.

- [GOOGLE DRIVE LINK](https://drive.google.com/drive/folders/1E3JBOl0uhLMRKvl9R5vpl6xaxchiJ6JA?usp=sharing)

- **TWO MUST-SEE DOCS IN MAIN FOLDER:**
  1. [Master Python Data Science Cheatsheets PDF](https://drive.google.com/open?id=1PxRAhlaK7ucf0S2F732eJ94ovaPtUSE_).
  2. [Student Resources GSheet of Study Group Videos by Topic](https://drive.google.com/open?id=1CNGDhjcQZDRx2sWByd2v-mgUOjy13Cd_hQYVXPuzEDE)

    <details>
      <summary style="font-weight:50%;">Student Resources GSheet Tab Info</summary>

    | Student Resources Gsheet Tab | Contents | 
    | --- | --- |
    | Screencasts | Not much on this tab, skip it.|
    | Study Groups V1 / Study Groups V2| A "best of" collection of study groups by all instructors|
    | |Note: v1's sections numbers are a little different than your v2, so read the topic, not the section #|
    |Peer 2 Peer Study Groups| Student-led study groups on misc. topics|
    |Additional Topics | Additional instructor-led videos on topics beyond of Learn lessons|

    </details>

___

### II. MODULE PROJECT INFO/PROCESS

- Your projects and associated Learn.co lessons can all be found on the [Portfolio Projects Section](https://learn.co/tracks/data-science-career-v2/portfolio-projects) on Learn.
- Project deadlines are on the Google Calendar at the top of this homepage.

### PROJECT SUBMISSIONS

#### 1. "Soft" Deadline AKA "Project Links Deadline"

- Full time: 1 week after project start date.
- Part time: 2 weeks after project start date.

- All required project links must be **entered on the sidebar of the project's Learn.co lesson page** and make sure to **check "I'm done"** at the bottom of the sidebar.
  - Note: you can continue to update your project after turning in the links.

- **Schedule your project review as soon as you turn in your links** (see next section below.)

- **Q: What if I don't have all pieces of my project finished by the soft deadline?**

  - For your notebook and presentation: 

    - You may continue to update your repo's contents up until your scheduled project review.

  - For the video/blog post/READMEs:
    - See "HOW TO USE PLACEHOLDER LINKS FOR Videos & Blog Posts" below

#### 2. SCHEDULE YOUR PROJECT REVIEW

- Use the link below to schedule your project review with me ASAP.
  - [Schedule a Project Review](https://go.oncehub.com/PortfolioProjectReviews)
  - The earlier you schedule your first review, the more time you will have to schedule a second review, if required. 
  - Please push any final changes before your scheduled project review.

#### 3. "Hard" Deadline AKA "Successfully Passing Your Project Review" Deadline

- YOU **MUST SUCCESSFULLY PASS YOUR PROJECT REVIEW WITHIN 2 WEEKS AFTER THE SOFT DEADLINE** / PROJECT LINK DEADLINE.

- You are allowed **as many project review attempts** as you can fit in before the hard deadline.

- Schedule your first review as soon as possible, so you have sufficient time to re-present the project before the hard deadline.

### HOW TO: PROJECT README, PLACEHOLDER VIDEO AND BLOG POST LINKS

<details>
  <summary style="font-weight:50%;">HOW TO USE PLACEHOLDER LINKS FOR Videos & Blog Posts</summary>

- **I highly recommend making an account with a url-shortening service that allows you to edit the destination url *after creation*.**
- I recommend www.rebrandly.com, but there are other services out there.

#### Blog post: 
  - Please think of at least a title for your blog post and  publish your rough draft/placeholder to get a blog post url.
  - If you can't think of one, use an updatable short url from rebrandly.

#### Video: two options.

  - Create a shortened url that you can redirect (PREFERRED OPTION) 
    - Use a placeholder YouTube video link to create your video url.
    - Later on, you can come back to rebrandly to edit the link that your shortened url redirects to.
  - Submit any YouTube video link, either appropriate or humorous, up to you (NON-PREFERRED OPTION)

#### README: See below for instructions on turning your notebook into a README for your repo.
</details>

### How To: convert your project notebook into the repo's README

**There are two methods:**

1. Command line method:
Launch a terminal in the same folder as your notebook.

```shell
jupyter nbconvert --to markdown notebook_name.ipynb
mv README.md README_old.md
mv notebook_name.md README.md
```

2. Jupyter Notebook GUI method:

- Select `File` > `Download as` > `Markdown`
  - Notebook + output images will be downloaded a zip file.
  - Extract contents of zip folder to main folder of repo.
  - Rename the original `README.md` to `README_old.md`
  - Rename the notebook.md to `README.md`

___

## III. HOW TO INSTALL UPDATED `learn-env` WITH THE NEW REPO/LESSON

- Read and clone the new lesson's repo [GitHub Link](https://github.com/learn-co-curriculum/dsc-data-science-env)
  - Clone repo: `git clone https://github.com/learn-co-curriculum/dsc-data-science-env`
  - cd into repo: `cd dsc-data-science-env`
  - If `learn-env` is already installed jump down to ["updating-your-virtual-environment"](https://github.com/learn-co-curriculum/dsc-data-science-env#updating-your-virtual-environment)
    - Run these commands

    ```shell
      conda activate base # To make sure you're not in the learn-env environment
      conda remove -n learn-env --all # To get rid of the environment
      conda env list # Make sure it doesn't list learn-env - if it does, try the last step again
      ```

  - Enter the command to create `learn-env`:
    ```shell
    # for mac:
    conda env create -f environment.yml
    # for windows:
    conda env create -f windows.yml
    ```

### Make sure learn shows up in your jupyter notebook kernels:

- Type this command into terminal:<br>
  `python -m ipykernel install --user --name=learn-env`

### **To set learn-env as your default env** (so you won't have to activate it each time)

-  Enter the following command into your terminal (Windows Users See Warning Below)<br>
`echo "conda activate learn-env" >> ~/.bash_profile` 
- **BONUS HACK:** Run this to create a "jnb" shortcut that allows you to type `jnb` to open jupyter notebook.
  ```echo "alias jnb='jupyter notebook'">>~/.bash_profile```
  - Note: if you are using a different shell besides bash, you will need to find out its equivalent of `.bash_profile`

- **NOTE: WINDOWS USERS WARNING, THE INSTRUCTIONS HAVE AN ERROR:**
  - Change "conda activate learn-env" to whatever you normally type to activate your `learn-env`.
    - For most windows users its actually "`source activate learn-env`".
  - The corrected command is `echo "source activate learn-env" >> ~/.bash_profile`

- **To manually make edits/corrections to your `.bash_profile`:**
  - Launch a new terminal in its default folder (or type `cd ~`
  - Then type `open .bash_profile`

___

## IV. Installing and activating Jupyter Notebook Extensions - [Study Group Video on JNE](https://youtu.be/Fl7Xwr_kUkw)

- In your terminal enter the following commands:

  ```shell
  conda install -c conda-forge jupyter_contrib_nbextensions
  jupyter nbextension enable jupyter_nbextensions_configurator
  ```

- When you boot up jupyter notebook, click on the new tab called `nbextensions` on the jupyter notebook home page and check out the list of available extensions.
  - If the list of available notebook extensions is grayed out:
    - Uncheck "`disable configuration for nbextensions without explicit compatibility (they may break your notebook environment, but can be useful to show for nbextension development)`" at the top of the page

- **Recommended extensions to turn on:**
  - `Variable Inspector`: Lets you see details about all of the variables in your notebook.
  - `Table of Contents (2)`: Clickable sidebar with markdown headers as bookmarks/links.
  - `Collapsible Headings`: Collapse sections of your notebook using markdown headers.
  - `Codefolding`: Lets you collapse function definitions and blocks of code. 

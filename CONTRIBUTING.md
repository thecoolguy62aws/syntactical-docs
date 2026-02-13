# Contributing

Contributing to Syntactical Docs is quite simple, but some things are requried to do it.

## Prerequisites

- A computer (preferably Windows)
- Have Python installed on that computer (I know, I know, I'm making you install a different programming language to work on this one's docs. Once Syntactical is a bit better, I will change this to use it.)
- Know how to use GitHub flavored markdown
- Know basics of Git and GitHub (forking, pull requests, etc.)

Now that you have all the stuff you need, lets make some docs!

## Steps

1. Start by making a fork of this repository. Click here to create a fork: <a href="https://github.com/thecoolguy62aws/syntactical/fork" target="_blank">![Fork Syntactical](https://img.shields.io/badge/github-Fork_Syntactical-blue?logo=github)</a>
2. Now you have your own personal copy of Syntactical Docs! If you wish, you can make a clone of this fork on your device, otherwise just use the GitHub editor.
3. Next, you'll want to find the file in your fork called "plain.md". Open this file.
4. Make your changes in `plain.md`. This file uses **GitHub Flavored Markdown**.
5. After making your changes, if you are using Windows, run `build.bat` (if it doesn't work, try using the other method). If you are not on Windows (or the Windows method didn't work), use Python to run `build.py`.
6. If you only editing pre-existing sections (eg. installation, modules, etc.) you can skip steps
7. If you added new sections, open the "index.html" file.
8. Around line 29, you will find this snippet (maybe with more/less sections):
    ```html
    <div class="sidenav">
        <a href="#introduction">Introduction</a>
        <a href="#installation">Installation</a>
        <a href="#builtin-functions">Builtin Functions</a>
        <a href="#modules">Modules</a>
        <!-- More Sections Here -->
    </div>
    ```
    Notice that the order of the sections reflects the order they are on the page.
9. Copy this snippet: 
    ```html
    <a href="#your-section">Your Section</a>
    ```
10. Paste this snippet into the order of where your section is. It should end up looking something like this if your section is at the bottom:
    ```html
    <div class="sidenav">
        <a href="#introduction">Introduction</a>
        <a href="#installation">Installation</a>
        <a href="#builtin-functions">Builtin Functions</a>
        <a href="#modules">Modules</a>
        <a href="#your-section">Your Section</a>
        <!-- More Sections Here -->
    </div>
    ```
11. Assuming your section is not called "Your Section," you will have to change the name. Check your markdown code for the *exact name* of your **heading one**.
12. Replace the text "Your Section" with the full name of your header in the markdown text. (excluding the `# `)
13. For the text "#your-section" you will start by taking what you put in the last step, and add `#` to the beginning. (DO **NOT** INCLUDE THE `#` YOU HAD TO PUT IN THE MARKDOWN) Now, make all the letters lowercase. Lastly, replace spaces with a `-`. This should all be working now! Here's an example of what the snippet might look like after making a section at the bottom called "Getting Started"
    ```html
    <div class="sidenav">
        <a href="#introduction">Introduction</a>
        <a href="#installation">Installation</a>
        <a href="#builtin-functions">Builtin Functions</a>
        <a href="#modules">Modules</a>
        <a href="#getting-started">Getting Started</a>
        <!-- More Sections Here -->
    </div>
    ```
14. You've added to the docs of Syntactical! But you're not done yet, you still need to open a pull request and get it accepted.
15. Open the GitHub repository of your fork. Above the file explorer, but below the branch selector, you will find a option that says "Contribute." Click it.
16. Now, click "Create Pull Request."
17. Once you create your pull request, you are done! Your changes will be live once your pull request gets acceptecd.


**Thank you for contributing to the Syntactical Docs**
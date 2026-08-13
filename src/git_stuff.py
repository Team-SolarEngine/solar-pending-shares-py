import subprocess as sp
from datetime import datetime

"""
Process for approval for a pending share. Step-by-step on how it works.

git clone https://github.com/Team-SolarEngine/test-repo
           |
           v
writes featured-repos.txt with the url given
           |
           v
commits it
           |
           v
delete the cloned folder
           |
           v
repeat

Returns:
    If all good, then "All good!"
    : Else, the error message.
"""

def start_approve_process(url):
    try:
        # clone the test repo and add the url to the featured-repos.txt file
        sp.run(["git", "clone", "https://github.com/Team-SolarEngine/test-repo"], check=True)

        # set the username and email for commits
        ## solar-bot[approver] is our dummy guy, don't mind about him too much.
        sp.run(["git", "-C", "test-repo", "config", "user.name", "solar-bot[approver]"], check=True)
        sp.run(["git", "-C", "test-repo", "config", "user.email", "solar-bot[approver]@users.noreply.github.com"], check=True)

        # write the given url to the featured-repos.txt file
        with open("test-repo/featured-repos.txt", "a") as f:
            # filter out https://github.com/ from the url
            filtered_url = url.replace("https://github.com/", "")

            # writes the url to the file, with a newline at the start
            f.write("\n" + filtered_url)

        # commit the changes to the test repo
        sp.run(["git", "add", "featured-repos.txt"], check=True, cwd="test-repo")
        sp.run(["git", "commit", "-m", "add featured repo - " + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " at gmt+8"], check=True, cwd="test-repo")
        sp.run(["git", "push"], check=True, cwd="test-repo")

        # delete the dir
        sp.run(["rm", "-rf", "test-repo"], check=True)

        # return if it all worked well
        return "All good!"
    except Exception as e:
        return str(e)
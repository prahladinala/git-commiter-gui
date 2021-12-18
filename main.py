import tkinter as tk
import os
# import time

root = tk.Tk()

# setting the windows size
root.geometry("350x300")
root.title("Github Committer")

# declaring string variable
# for storing name and password
msg_var = tk.StringVar()
url_var = tk.StringVar()


# defining a function that will
# get the name and password and
# print them on the screen
def submit():

    message = msg_var.get()
    git_url = url_var.get()

    # print("The message is : " + message)
    # print("The git url is : " + git_url)
    # print(type(message))

    if message == "":
        status_text.set("")
        error_text.set("Oops! Commit message required.")
    
    if git_url == "":
        status_text.set("")
        error_text.set("Oops! GitHub Url is required to commit")

    if message == "" and git_url == "":
        status_text.set("")
        error_text.set("Oops! Commit message and Github Url required")

    if message != "" and git_url != "":
        error_text.set("")
        status_text.set("Status:")

    # INIT
    init = "git init"
    print(init)
    os.system(init)
    status_text.set("Initalized the repository")
    # time.sleep(5)

    # ADD
    add = "git add ."
    print(add)
    os.system(add)
    status_text.set("Added all your files")
    # time.sleep(5)

    # COMMIT
    commit = f'git commit -m "{message}"'
    print(commit)
    os.system(commit)
    status_text.set("Commiting your code to local repo")
    # time.sleep(5)

    # BRANCH
    branch = "git branch -M main"
    print(branch)
    os.system(branch)
    status_text.set("Branch named to main")
    # time.sleep(5)

    # REMOTE
    remote = "git remote add origin " + git_url+ ".git"
    print(remote)
    os.system(remote)
    status_text.set("Adding origin to remote repo")
    # time.sleep(5)

    # PUSH
    push = "git push -u origin main --force"
    os.system(push)
    status_text.set("Pushing your code to remote repo")
    # time.sleep(5)

    status_text.set("Pushed your code to remote repo")

    msg_var.set("")
    url_var.set("")


# creating a label for
# heading label
main_label = tk.Label(root, text='GitHub Commiter',
                     font=('calibre', 15, 'bold'),justify='center')
# main_label.tag_configure("GitHub Commiter", )

# name using widget Label
msg_label = tk.Label(root, text='Commit Message',
                     font=('calibre', 12, 'bold'))

# creating a entry for input
# name using widget Entry
msg_entry = tk.Entry(root, textvariable=msg_var,
                     font=('calibre', 12, 'normal'))

# creating a label for password
url_label = tk.Label(root, text='Github URL', font=('calibre', 12, 'bold'))

# creating a entry for password
url_entry = tk.Entry(root, textvariable=url_var,
                     font=('calibre', 12, 'normal'))

# creating a button using the widget
# Button that will call the submit function
sub_btn = tk.Button(root, text='Commit to Git', command=submit, font=(
    "calibre", 12, 'bold'), bg="#ff0066", fg="white", height=1, width=15)

# Status label
# variable for status text
status_text = tk.StringVar()
status_text.set("")
status_label = tk.Label(root, textvariable=status_text, font=('calibre', 12, 'normal'))

# Error Label
error_text = tk.StringVar()
error_text.set("")
error_label = tk.Label(root, textvariable=error_text, font=('calibre', 12, 'normal'))

# placing the label and entry in
# the required position using grid
# method
# main_label.grid(row=0, column=0, pady=(5))
main_label.grid(columnspan=2, pady=(10))
msg_label.grid(row=1, column=0, pady=(5))
msg_entry.grid(row=1, column=1, pady=(5))
url_label.grid(row=2, column=0, pady=(5))
url_entry.grid(row=2, column=1, pady=(5))
# sub_btn.grid(row=3, column=1, pady=(10))
sub_btn.grid(columnspan=2, pady=(10))
status_label.grid(columnspan=2)
error_label.grid(columnspan=2)

# performing an infinite loop
# for the window to display
root.mainloop()

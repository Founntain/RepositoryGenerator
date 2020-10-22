from github import Github
import json
import os

def main():
    #Read config file
    with open('config.json') as file:
        data = json.load(file)

    #Get Username, password, repository path & code command
    username = data["username"]
    password = data["password"]
    repositoriesPath = data["repositoryFolder"]
    codeCommand = data["codeCommand"]

    github = Github(username, password)

    repoName = input("Enter a repository name: ")
    description = input("Enter a description or leave blank: ")

    private = False
    try:
        value = int(input("Is this a private repo? 0 => no | 1 => yes: "))

        if value > 1:
            raise Exception("value > 1")
        
        private = bool(value)
    except:
        #If input is not a number or bigger then 1 set to False
        private = False

    #Get GitHub user
    user = github.get_user()

    #Create new repository on GitHub
    newRepo = user.create_repo(repoName, description, "", private)

    print("New repo with name" + newRepo.name + " created...\nInitializing repo with README.md")

    #Create Repository folder for the new Repository
    os.system("mkdir " + repositoriesPath + newRepo.name);
    os.chdir(repositoriesPath + newRepo.name)
    #Create README.md and initialize a new Git repository
    #And push it to the new GitHub repository
    os.system("echo # Test >> README.md");
    os.system("git init")
    os.system("git add *")
    os.system("git commit -m \"Init Commit\"")
    os.system("git branch -M master")
    os.system("git remote add origin https://github.com/" + username + "/" + newRepo.name + ".git")
    os.system("git push -u origin master")

    #Start VsCode or VsCode Insiders
    os.system(codeCommand)

main()
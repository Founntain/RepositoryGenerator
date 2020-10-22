# Test 

## Preparing the script
First you need to create a `config.json` the config should look like this
```JSON
{
    "username": "YOUR_GITHUB_USERNAME",
    "password": "YOUR_GITHUB_PASSWORD",
    "repositoryFolder": "Y:\\PATH\\TO\\YOUR\\REPOSITORIES\\FOLDER\\",
    "codeCommand": "code ."
}
```

If you use VsCode Insiders replace `code .` with `code-insiders .` for the `codeCommand` property.

The `repositoryFolder` property is used to create a folder for the new repository and create a README.md in that folder and push it to the new repository. You probably have somewhere on your PC a folder that contains all your repositories.
After you created the config you can run the script.

## Running the script
Run the script with python `python main.py`  
Enter all the values and the script will create a repository on GitHub and the Repository Folder on your PC at the given path
`repositoryFolder/Repository_Name`.

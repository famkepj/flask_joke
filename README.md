[![.github/workflows/run_test_deploy.yml](https://github.com/famkepj/flask_joke/actions/workflows/run_test_deploy.yml/badge.svg)](https://github.com/famkepj/flask_joke/actions/workflows/run_test_deploy.yml)

### Short report:
1) Name three components of your solution, explain what they are and how they relate to each other. A 'component' can be anthing from GitHub Actions or Bash to Digital Ocean and SSH.
- Made the app in my terminal, is al little bit difficult with the layout, but I couldn't do the assiment on my windows pc - gunicorn is not working on windows
- Secret keys made in the terminal - stored in Github - compared by the workflow
- sh file

2) Discuss three problems that you encountered along the way and how you solved them.
- Problem:	- Github couldn't read the secrets
- Solution:	- Put them in 'env'
```python
env:
  secrets_private_key: ${{ secrets.SSH_PRIVATE_KEY }}
  secrets_host: ${{ secrets.SSH_HOST }}
  secrets_user: ${{ secrets.SSH_USER }}
  secrets_port: ${{ secrets.SSH_PORT }}
  secrets_digitalocean: ${{ secrets.DIGITALOCEAN_ACCESS_TOKEN }}
```

- Problem: 	- From August 13, 2021, GitHub is no longer accepting account passwords when authenticating Git operations. You need to add a PAT (Personal Access Token) instead
- Solution: 	- Create personal acces token on Github & put this in windows credentials
	- ######  Create Personal Access Token on GitHub
	  From your GitHub account, go to 
 	  - => Settings 
	  - => Developer Settings 
	  - => Personal Access Token 
	  - => Generate New Token (Give your password) 
	  - => Fillup the form 
	  - => click Generate token 
	  - => Copy the generated Token, it will be something like ghp_sFhFsSHhTzMDreGRLjmks4Tzuzgthdvfsrta

	- ######  For Windows OS ⤴
	  Go to 
	  - => Credential Manager from Control Panel 
	  - => Windows Credentials 
	  - => find git:https://github.com 
	  - => Edit 
	  - => On Password replace with with your GitHub Personal Access Token 

- Problem:	- Workflow is working but website is still not published on website -> don't know what I am missing
- Solution:       - Search the internet -> ask for help in slack


3) (optional) Anything of note that you want to share about the process of solving this assignment.
- I hade many errors in my workflow but everytime it tells you what is wrong, so eventually evrything is working
- At the end I am lost everything is working, but still not published. 
- I start over again in the module deployment and make everything step by step

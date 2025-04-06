import requests

def get_github_data(username):
    url = f"https://api.github.com/users/{username}/repos"
    response = requests.get(url)
    if response.status_code == 200:
        repos = response.json()
        return {
            "repos": len(repos),
            "stars": sum(repo['stargazers_count'] for repo in repos),
        }
    return {}
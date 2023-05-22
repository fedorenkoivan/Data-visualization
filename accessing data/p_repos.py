import requests

# Зробити виклик через API та зберегти відповідь.
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

# Зберегти відповідь API у змінну.
responce_dict = r.json()
print(f"Total repositories: {responce_dict['total_count']}")

repo_dicts = responce_dict['items']
print(f"Repositories returned: {len(repo_dicts)}")

for repo_dict in repo_dicts[:10]:
    print("\nSelected information from first repository:")
    print(f"Name: {repo_dict['name']}")
    print(f"Owner: {repo_dict['owner']['login']}")
    print(f"Stars: {repo_dict['stargazers_count']}")
    print(f"Repository: {repo_dict['html_url']}")
    print(f"Created: {repo_dict['created_at']}")
    print(f"Updated: {repo_dict['updated_at']}")
    print(f"Description: {repo_dict['description']}")
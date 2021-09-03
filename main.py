import os
import json
#import logging as log
import requests import get  # noqa We are just importing this to prove the dependency installed correctly

def get_pull_request_page(url, token):
    #log.debug("Accessing Github API with URL: {}".format(url))
    headers = {'Authorization': 'token %s' % token}
    response = get(url, auth=auth, verify=True)
    if response.status_code == 200:
        link_header = response.headers.get('Link', None)
        next_url = get_next_page_url(link_header)
        return next_url, json.loads(response.text)

    #log.error("Error accessing Github API : HTTP {} | {}".format(response.status_code, response.text))
    #raise SCMToolException("Unable to retrieve pull requests from github API | {}".format(response))

def main():
    repo = os.environ["GITHUB_REPOSITORY"]
    server_url = os.environ["GITHUB_SERVER_URL"]
    github_token = os.environ["github_token"]

    print(f"Hello repo: {server_url}/{repo}")
    print("Token: %s", github_token[0: 5])

    pull_requests_url = "{server_url}/{repo}/pulls?state=open&per_page=100".format(
                server_url=server_url,
                repo=repo
            )

#     while pull_requests_url:
#         result = get_pull_request_page(pull_requests_url, token)
#         pull_requests_url = result[0]
#         for pull_request in result[1]:
#             print(f"Pull request: {pull_request}")

if __name__ == "__main__":
    main()

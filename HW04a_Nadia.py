"""
HW 04a
Nadia Vedeneyeva
Develop with the perspective of the tester in mind
"""

import requests
import json
import unittest

def commitCount(gitHubID):
    repos = getRepositories(gitHubID)
    dct = {}
    for repo in repos:
        repoName = repo['name']
        dct[repoName] = getCommits(gitHubID, repoName)
    return dct

def getRepositories(gitHubID):
    URL = 'https://api.github.com/users/' + gitHubID + '/repos'
    r = requests.get(url = URL)
    data = r.json()
    return data

def getCommits(gitHubID, repoName):
    URL = 'http://api.github.com/repos/' + gitHubID + '/' + repoName + '/commits'
    r = requests.get(url = URL)
    data = r.json()
    return len(data)

class GitHubAPITest(unittest.TestCase):

    def test_commitCount(self):
        assert len(commitCount('ruthylevi')) > 0

    def test_getRepositories(self):
        assert len(getRepositories('nadia-v')) > 0

    def test_getCommits(self):
        assert len([getCommits('nadia-v', 'university-rep[ository')]) > 0


def main():
    user = input('Please enter GitHub user ID:\n')

    print(f'{user} has {commitCount(user)} commits')

main()

if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
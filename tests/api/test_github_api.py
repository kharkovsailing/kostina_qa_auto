import pytest
from modules.api.clients.github import GitHub


@pytest.mark.api
def test_user_exists(github_api):
    user = github_api.get_user('defunkt')
    assert user['login'] == 'defunkt'


@pytest.mark.api
def test_user_not_exists(github_api):
    r = github_api.get_user('butenkosergii')
    assert r['message'] == 'Not Found'
    

# Test with parametres to search 'total count' of repositories

@pytest.mark.parametrize('name, count', [('Sailing-Photo-Gallery', 1), ('sergiibutenko_non_exist', 0)])
def test_repo_count(github_api, name, count):
    assert github_api.search_repo(name)['total_count'] == count

# The same test without parametres - the next two tests:
    
@pytest.mark.api
def test_repo_can_be_found(github_api):
    repo = github_api.search_repo('Sailing-Photo-Gallery')
    assert repo['total_count'] == 1
    
    
@pytest.mark.api
def test_repo_cannot_be_found(github_api):
    repo1 = github_api.search_repo('sergiibutenko_non_exist')
    assert repo1['total_count'] == 0
    
# Test for a singl-char repository
    
@pytest.mark.api
def test_repo_with_single_char_be_found(github_api):
    repo2 = github_api.search_repo('s')
    assert repo2['total_count'] != 0

# Test for emojis

@pytest.mark.api
def test_emoji(github_api):
    assert github_api.get_emogjis().status_code == 200
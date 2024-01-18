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
    
    
@pytest.mark.api
def test_repo_can_be_found(github_api):
    repo = github_api.search_repo('become_qa_auto')
    assert repo['total_count'] == 54
    
    
@pytest.mark.api
def test_repo_cannot_be_found(github_api):
    repo1 = github_api.search_repo('sergiibutenko_non_exist')
    assert repo1['total_count'] == 0
    
    
@pytest.mark.api
def test_repo_with_single_char_be_found(github_api):
    repo2 = github_api.search_repo('s')
    assert repo2['total_count'] != 0

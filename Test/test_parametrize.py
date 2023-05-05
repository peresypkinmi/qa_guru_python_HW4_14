"""
Переопределите параметр с помощью indirect параметризации на уровне теста
"""
import pytest
from selene.support.shared import config
from git_auth import GitAuth


@pytest.fixture(params=[(1920, 1080), (390, 884)])
def browser(request):
    config.window_width = request.param[0]
    config.window_height = request.param[1]


@pytest.mark.parametrize('browser', [(1920, 1080)], indirect=True)
def test_github_desktop(browser):
    auth = GitAuth()
    auth.open_start_page()
    auth.click_sing_up_button()
    auth.check_auth_form_header()


@pytest.mark.parametrize('browser', [(390, 884)], indirect=True)
def test_github_mobile(browser):
    auth = GitAuth()
    auth.open_start_page()
    auth.open_navigation_menu()
    auth.click_sing_up_button()
    auth.check_auth_form_header()

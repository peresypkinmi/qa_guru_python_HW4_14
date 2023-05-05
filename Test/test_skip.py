"""
Параметризуйте фикстуру несколькими вариантами размеров окна
Пропустите мобильный тест, если соотношение сторон десктопное (и наоборот)
"""
import pytest
from selene.support.shared import config
from git_auth import GitAuth


@pytest.fixture(params=[(1920, 1080), (390, 884)])
def browser(request):
    config.window_width = request.param[0]
    config.window_height = request.param[1]


def test_github_desktop(browser):
    if config.window_width == 390 and config.window_height == 884:
        pytest.skip(reason = "не подходит соотношение сторон для теста не десктопе")
    auth = GitAuth()
    auth.open_start_page()
    auth.click_sing_up_button()
    auth.check_auth_form_header()


def test_github_mobile(browser):
    if config.window_width == 1920 and config.window_height == 1080:
        pytest.skip(reason = "не подходит соотношение сторон для теста на мобильном устройстве")
    auth = GitAuth()
    auth.open_start_page()
    auth.open_navigation_menu()
    auth.click_sing_up_button()
    auth.check_auth_form_header()

"""
Сделайте разные фикстуры для каждого теста, которые выставят размеры окна браузера
"""
from homework.git_auth import GitAuth


def test_github_desktop(desktop_config):
    auth = GitAuth()
    auth.open_start_page()
    auth.click_sing_up_button()
    auth.check_auth_form_header()


def test_github_mobile(mobile_config):
    auth = GitAuth()
    auth.open_start_page()
    auth.open_navigation_menu()
    auth.click_sing_up_button()
    auth.check_auth_form_header()

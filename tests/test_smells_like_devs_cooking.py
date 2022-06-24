from time import sleep

import pytest


def test_home(page):
    page.goto("https://smells-like-devs-cooking-frontend-rho.vercel.app/")

    assert page.title() == "Smells Like Devs Cooking"
    assert page.inner_text("a") == "\xa0\xa0Home"
    # assert page.inner_text("a") == "sign up"

    # username_value = page.locator("text=USER NAME").input_value()
    # password_value = page.locator("text=PASSWORD").input_value()
    #
    # assert username_value == ''
    # assert password_value == ''


def test_home_page_values(logged_in_page):
    assert logged_in_page.inner_text("a") == "\xa0\xa0Home"
    # assert logged_in_page.inner_text("a") == "About the Cooks"
    # assert logged_in_page.inner_text("a") == "Create a Blog Post"
    # assert logged_in_page.inner_text("a") == "admin's profile"
    # assert logged_in_page.inner_text("a") == "logout"


def test_home_page_navigation(logged_in_page):
    anchor = logged_in_page.locator("text=Create a Blog Post")
    url = anchor.get_attribute("href")
    assert url == "/create"
    # with logged_in_page.expect_navigation(url=url):
    #     anchor.click()


@pytest.mark.skip("TODO")
def test_detail_page(logged_in_page):
    anchor = logged_in_page.locator("div div a").first
    url = anchor.get_attribute("href")
    blog_post_name = anchor.text_content()
    anchor.click()
    
    assert logged_in_page.url.endswith(url)
    assert blog_post_name in logged_in_page.inner_text("body")
    

@pytest.fixture
def logged_in_page(page):
    page.goto("https://smells-like-devs-cooking-frontend-rho.vercel.app/loginpage")
    
    page.fill('#username', 'admin')
    page.fill('#password', 'admin')
    page.click('button')
    # sleep(3)

    return page

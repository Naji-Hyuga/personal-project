# -*- coding: utf-8 -*-
from pages.main_page import MainPage
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
from pages.locators import link
from pages.locators import MainPageLocators


# def test_guest_can_go_to_login_page(browser):
#     browser.get(link)
#     page = MainPage(browser, link)
#     page.open()
#     page.go_to_login_page()
#
#
# #Метод проверяющий наличие ссылки
# def test_guest_should_see_login_link(browser):
#     page = MainPage(browser, link)
#     page.open()
#     page.should_be_login_link()


def test_guest_should_see_login_url(browser):
    page = LoginPage(browser, link)
    page.open()
    page.browser.find_element(*MainPageLocators.LOGIN_LINK).click()
    page.should_be_login_url()


def test_guest_should_be_login_form(browser):
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_form()


def test_guest_should_be_register_form(browser):
    page = LoginPage(browser, link)
    page.open()
    page.should_be_register_form()



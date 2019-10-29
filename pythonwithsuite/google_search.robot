*** Settings ***
Library         google_search_lib.py    chrome
Test Setup      Log To Console    Starting a test...
Test Teardown   Close

*** Test Cases ***
Run A Google Search
    Search for      emoji wars
    Sleep           10s


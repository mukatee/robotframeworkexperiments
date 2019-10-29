*** Settings ***
Library         google_search_lib.py    chrome

*** Test Cases ***
Run A Google Search
    Search for      emoji wars
    Sleep           10s
    Close


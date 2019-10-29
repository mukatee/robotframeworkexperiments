*** Settings ***
Library  SeleniumLibrary

*** Test Cases ***
Run A Google Search
    Open browser    http://google.com/   Chrome
    Press Keys      name:q    emoji wars+ENTER
    Sleep           10s
    Close All Browsers


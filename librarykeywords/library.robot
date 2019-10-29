*** Settings ***
Library  OperatingSystem

*** Variables ***
${PATH}    ${CURDIR}/library.robot

*** Test Cases ***
Check Test OK
    Log To Console       Hello Critical Donkey
    File Should Exist    ${PATH}

Check Test Fail
    Log To Console           Hello Failing Donkey
    File Should Not Exist    ${PATH}

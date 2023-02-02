*** Settings ***
Library     SeleniumLibrary
Library    SeleniumLibrary

*** Variables ***
${browser}  chrome
${url}  https://www.nopcommerce.com/en/login?returnUrl=%2Fen%2Fget-started

*** Test Cases ***
LoginTest
    open browser    ${url}  ${browser}
    logintoapplication
    close browser

*** Keywords ***
loginToApplication
    input text        id:Username   mmsezgin@gmai.com
    input text        id:Password    12345
    click element    xpath://*[@type='submit']
*** Settings ***
Variables   cfg.py



*** Test Cases ***
test1
    log to console   ${url}
    log to console   ${data}
    log to console   @{data}[0]
    log to console   ${user1["username"]}
    log to console   &{user1}[username]

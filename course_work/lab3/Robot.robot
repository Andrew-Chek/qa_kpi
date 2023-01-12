*** Settings ***
Library    Process
Library    OperatingSystem
*** Variables ***
${cli}    /home/andrey/progbase.projects/qa_kpi/course_work/lab3/main.py

*** Test Cases ***
Dir root create
    ${result} =    Run Process    python3   ${cli}    get    directory    name\=root
    Should Contain    ${result.stdout}   Status code: 200

Dir inner create
    ${result} =    Run Process    python3   ${cli}    post    directory    parent\=root    name\=child12    max_elems\=8
    Should Contain    ${result.stdout}   Status code: 201

Dir create not exists
    ${result} =    Run Process    python3   ${cli}    post    directory    parent\=root    name\=child12    max_elems\=8
    Should Contain    ${result.stdout}   Status code: 400

Dir move
    ${result} =    Run Process    python3   ${cli}    patch    directory    name\=child12    parent\=root
    Should Contain    ${result.stdout}   Status code: 200

Dir delete
    ${result} =    Run Process    python3   ${cli}    delete    directory    name\=child12
    Should Contain    ${result.stdout}   Status code: 200

Dir delete not exists
    ${result} =    Run Process    python3   ${cli}    delete    directory    name\=child12
    Should Contain    ${result.stdout}   Status code: 400


Binary file create
    ${result} =    Run Process    python3   ${cli}    post    binaryfile    fileName\=binaryFile1    father\=newDir1    content\=hello
    Should Contain    ${result.stdout}   Status code: 200

Binary file read
    ${result} =    Run Process    python3   ${cli}    get    binaryfile
    Should Contain    ${result.stdout}   Status code: 200

Binary file delete
    ${result} =    Run Process    python3   ${cli}    delete    binaryfile
    Should Contain    ${result.stdout}   Status code: 200

Buffer file create
    ${result} =    Run Process    python3   ${cli}    post    bufferfile    fileName\=bufferFile1    father\=newDir1    maxSize\=10
    Should Contain    ${result.stdout}   Status code: 200

Buffer file read
    ${result} =    Run Process    python3   ${cli}    get    bufferfile
    Should Contain    ${result.stdout}   Status code: 400

Buffer file delete
    ${result} =    Run Process    python3   ${cli}    delete    bufferfile
    Should Contain    ${result.stdout}   Status code: 200
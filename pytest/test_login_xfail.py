import pytest

message = "Bye, Ameya"


#@pytest.mark.xfail
#Issue id-2345 is now resolved
def test_verify_login():
    user = 'mark'
    passwd = 'mark@123'
    assert 'mark' in user
    assert 'mark@123' == passwd


#@pytest.mark.skip
def test_welcome_message():
    global message
    print("\nInside Welcome Message Assert Function")
    if 'Welcome' not in message:
        pytest.xfail("This test is expected to fail because the message does not have expected word")
    assert message.startswith('Welcome'), "Assertion Failed. Message does not start with word 'Welcome'"



@pytest.mark.xfail('Welcome' not in message, reason="This test is expected to fail because the message does not have expected word")
def test_multiple_messages():
    global message
    print("\n"+message)
    validmessages = ('Welcome', 'Hey', 'Howdy')
    assert message.startswith(validmessages)

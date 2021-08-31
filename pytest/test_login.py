def test_verify_login():
    user = 'mark'
    passwd = 'mark@123'
    assert 'mark' in user
    assert '@123' in passwd


message = "Hey, Ameya"

import pytest

#@pytest.mark.dependency(depends=["test_multiple_messages"])
def test_welcome_message():
    global message
    print("\nInside Welcome Message Assert Function")
    assert message.startswith('Welcome'), "Assertion Failed. Message does not start with word 'Welcome'"

#@pytest.mark.dependency
def test_multiple_messages():
    global message
    print("\n"+message)
    validmessages = ('Welcome', 'Hey', 'Howdy')
    assert message.startswith(validmessages)

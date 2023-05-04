from hello import print_hello, print_goodbye

def test_print_hello():
    assert "Hi" == print_hello()

def test_print_goodbye():
    assert "bye" == print_goodbye()
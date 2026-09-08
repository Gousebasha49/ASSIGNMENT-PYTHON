x = "I am global"


def test_scope():
    x = "I am local"
    print("Local variable:", x)
    print("Global variable:", globals()["x"])


test_scope()
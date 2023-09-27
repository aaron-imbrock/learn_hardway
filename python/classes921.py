spam = 'maps'


def scope_test():
    def do_local():
        spam = 'local spam'

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print(f"after do_local() local assignment: {spam}")
    do_nonlocal()
    print(f"After do_nonlocal() nonlocal assignment: {spam}")
    do_global()
    print(f"After do_global() global assignment: {spam}")


scope_test()
print(f"In global scope: {spam}")

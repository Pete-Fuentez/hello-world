def example(required, option1=2, option2=3):
    print(required, option1, option2)

example(1)
example(1, 10)
example(1, 10, 20)
example(1, option2=20)
example(1, option2=20, option1=10)




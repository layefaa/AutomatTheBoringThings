def student_info(*args, **kwargs):
    print(args, kwargs)


student_info(1, 2, 3, name='John', age=20)
student_info(name='John', age=20)

numbers = [1, 2, 3]
info = {'name': 'John', 'age': 20}

student_info(*numbers, **info)

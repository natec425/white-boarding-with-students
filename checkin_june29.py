def name_file(file_name):
    with open(file_name) as file:
        file.readline()  # to skip the first line
        contents = file.read()
    student_list = contents.split('\n')
    return student_list


def list_to_dictionary(names):
    dictionary = {}
    for name in names:
        dictionary[name] = False
    return dictionary


def valid_names(students):
    '''Dict -> Set
    >>> valid_names({'lisa': False, 'oz': False, 'trey': False})
    {'lisa', 'oz', 'trey'}
    '''
    return set(students.keys())


def string_names(student_dict):
    '''
    >>> string_names({'a': ..., 'b': ..., 'c': ...})
    a, b, c
    '''
    print(', '.join(student_dict))


def input_valid_name(valid_names):
    while True:
        user_response = input('Name: ')
        if user_response in valid_names:
            return user_response
        elif user_response == 'quit':
            break
        else:
            print('Please provide a valid name')


def checkin(students, student_name):
    ''' (dict, str) -> None

    Check in a student by changing their value
    to True.

    >>> students = {'lisa': False, 'Jo': False}
    >>> checkin(students, 'lisa')
    >>> students
    {'lisa': True, 'Jo': False}
    '''
    # for name in students:
    #     if name == student_name:
    #         students[student_name]= True
    students[student_name] = True


def check_out(students, student_name):
    ''' (dict, str) -> None

    >>> students = {'jeff': True}
    >>> check_out(students, 'jeff')
    >>> students
    {'jeff': False}
    >>> check_out(students, 'jeff')
    >>> students
    {'jeff': False}
    '''
    students[student_name] = False


def print_status(students):
    checked_in = []
    not_in = []
    for student in students:
        if students[student]:
            checked_in.append(student)
        else:
            not_in.append(student)
    print('Checked in:', ', '.join(checked_in))
    print('Not checked in:', ', '.join(not_in))


def checkin_or_checkout(students, student_name):
    ''' (dict, str) -> None

    >>> checkin_or_checkout({'Jo': True, 'lisa': False}, 'lisa')
    Would you like to checkin or checkout? checkin
    CHECKIN
    '''
    while True:
        response = input('Would you like to checkin or checkout? ')
        if response == 'checkin':
            checkin(students, student_name)
            break
        elif response == 'checkout':
            check_out(students, student_name)
            break
        else:
            print('Invalid response')


def main():
    list_of_students = name_file('names.txt')
    student_checkins = list_to_dictionary(list_of_students)
    student_names = valid_names(student_checkins)
    while True:
        name = input_valid_name(student_names)
        if name is None:
            break
        checkin_or_checkout(student_checkins, name)
        print_status(student_checkins)


if __name__ == '__main__':
    main()
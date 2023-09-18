import random


def yell(text: str):
    return text.upper() + '!'


def whisper(text: str):
    return text.lower() + '...'


# Function name and function object are separate things


def functions_are_objects(_yell):
    bark = _yell
    del _yell
    print(bark("Woof"))
    print(bark.__name__)  # yell. Attribute for debugging purposes only


def could_be_stored_in_data_structures(_yell):
    bark = _yell
    funcs = [bark, str.lower, str.capitalize]
    for f in funcs:  # Methods may be called as positionals
        print(f, f('bottom text'))
    print(funcs[0]('нижний текст'))  # Access may be direct


def could_be_passed_to_other_functions(method):
    greeting = method("Privet kozhaniy :)")
    print(greeting)


def could_be_mapped(_yell):
    greets = ['Hello', "hey", 'hi']
    print(list(map(_yell, greets)))


def nested_functions_exist(volumes: list, text: str):
    """
    Also called 'inner functions'
    """

    def get_speak_func(volume):
        def funk(_text: str):
            return ''.join([char.upper() for char in text.strip() if
                            random.randint(0, 10) > 5])

        def sep(_text: str):
            return ' '.join(_text.strip())

        if volume > 50:
            return funk
        return sep

    print(list(get_speak_func(volume)(text) for volume in volumes))


if __name__ == "__main__":
    functions_are_objects(yell)
    could_be_stored_in_data_structures(yell)
    could_be_passed_to_other_functions(yell)
    could_be_passed_to_other_functions(whisper)
    could_be_mapped(yell)
    nested_functions_exist([10, 51], "Henlo")

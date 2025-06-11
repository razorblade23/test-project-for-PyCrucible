import cowsay


def say_message():
    message = """
    This is the message from a test module.

        - razorblade23
    """.strip()

    print(cowsay.get_output_string("cow", message))

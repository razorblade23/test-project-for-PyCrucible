import cowsay

from test_module.test import say_message

message = """
The most remarkable thing about my mother is that for thirty years she served
the family nothing but leftovers.  The original meal has never been found.
		-- Calvin Trillin
""".strip()

print(cowsay.get_output_string("cow", message))

say_message()

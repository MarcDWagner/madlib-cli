from textwrap import dedent

# def welcome():
#     print(dedent("""
#     Welcome to Madlib!
#     During the madlib process, you will be prompted to enter a part of speech (noun, adjective, verb, etc..), once all prompts have been filled a message will be returned using those parts of speech you input in order to create a sentence.
#     """))

# welcome()
# read into dark_and_stormy_night_template
def read_template(self):
    with open("assets/dark_and_stormy_night_template.txt") as f:
        contents = f.read()
        print(contents)


# def parse_template():

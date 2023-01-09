from .base_test import *

def test_fr_to_en(gpt3_client: Gpt3Client):
    prompt = """Teacher: What are some common kitchen utensils?
bob: spoon, fork
Teacher: Those are two, what are some others?
bob: je ne sais pas
"""

    response = gpt3_client.invoke_from_file("./en/conversation.txt", {}, prompt, stop=['Teacher:', 'bob:'])

    assert response == "CORRECTION: I don't know"

def test_fr_to_en_with_grammar_error(gpt3_client: Gpt3Client):
    prompt = """Teacher: What are some common kitchen utensils?
bob: spoon, fork
Teacher: Those are two, what are some others?
bob: je sait pas
"""

    response = gpt3_client.invoke_from_file("./en/conversation.txt", {}, prompt, stop=['Teacher:', 'bob:'])

    assert response == "CORRECTION: I don't know"

def test_de_to_en(gpt3_client: Gpt3Client):
    prompt = """Teacher: What are some common kitchen utensils?
bob: spoon, fork
Teacher: Those are two, what are some others?
bob: ich weiß nicht
"""

    response = gpt3_client.invoke_from_file("./en/conversation.txt", {}, prompt, stop=['Teacher:', 'bob:'])

    assert response == "CORRECTION: I don't know"

def test_en_dont_auto_complete_sentences(gpt3_client: Gpt3Client):
    prompt = """Teacher: What are the different types of blocks in Minecraft?
bob: grass, wood
"""

    response = gpt3_client.invoke_from_file("./en/conversation.txt", {}, prompt, stop=['bob:'])

    assert response.startswith("Teacher:")

def test_de_to_fr(gpt3_client: Gpt3Client):
    prompt = """Professeur : Quels sont les ustensiles de cuisine courants ?
bob : cuillère, fourchette
Professeur : Ce sont deux, quels sont les autres ?
bob: ich weiß nicht
"""

    response = gpt3_client.invoke_from_file("./fr/conversation.txt", {}, prompt, stop=['Teacher:', 'bob:'])

    assert response == "CORRECTION: Je ne sais pas"

def test_de_to_fr_with_grammar_error(gpt3_client: Gpt3Client):
    prompt = """Teacher: What are some common kitchen utensils?
bob: spoon, fork
Teacher: Those are two, what are some others?
bob: ich weise nicht
"""

    response = gpt3_client.invoke_from_file("./en/conversation.txt", {}, prompt, stop=['Teacher:', 'bob:'])

    assert response == "CORRECTION: I don't know"

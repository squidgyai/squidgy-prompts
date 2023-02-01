# Squidgy Prompts - Learn Languages with GPT3
Squidgy Prompts are a collection of prompts from [Squidgies](https://squidgies.app) which can be used
to help study languages (with or without the Squidgies app).

They include prompts for:
* Building flashcard "decks":
    * Deck description
    * Deck lesson outline
    * Deck lesson text
    * Deck vocabulary
    * "Sentence mining" (phrase generation)
    * Fill in the blank "hint"s for cloze exercises
* Language tutor (open ended discussion)
* Discussion questions (focused discussion on a question)
* Vocabularly conversation - discussion about a new vocabulary word
* Grammar correction
* Translation correction - grammar correction plus ensures that the translated phrase is faithful to the original
* Alternative suggestions - suggests different ways to phrase sentences that sound more fluent
* Taboo - a game where AI needs to guess word by having the user describe it
* Twenty Questions - a game where the user needs to guess a word through asking questions
* Explaining the difference between two words or phrases

# Goals

* Support any language
* Composable - prompts should work together
* Prompts should be able to be "completed" or have some definition of what "done" is, although this may not be possible in all conversations (e.g. open ended conversation)
* Prompt responses need to be structured and machine readable so they can be embedded in applications
* Quality while balancing performance - for the most part this means creating a prompt for each language and iterating on it to minimize size (an art, not a science)

# Questions, Ideas and Contributions
Ask questions or get involved by joining the [Squidiges discord](https://discord.gg/A3nSQEQZ6f).

Squidgy Prompts is open source. We welcome any/all contributions and ideas. Some areas of focus include:
* Adding more languages
* Improving prompt quality
* Addition of personalities to speakers
* Addition of other prompt types

# Test Suite

The Squidgy Prompts have a test suite using [SquidgyTesty](https://github.com/squidgyai/squidgy-testy).

To install:
```
$ pip install git+https://github.com/squidgyai/squidgy-testy
```

Then to run all the tests:
```
$ cd squidgy-prompts
$ python -m squidgy_testy
```

You can also run just a single test suite or test:
```
python -m squidgy_testy --test-suite test_vocab_conversation --test fr_conversation_start
```
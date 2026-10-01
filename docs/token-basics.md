# Token Basics

Tokens are small units of text that language models process. A token is not always the same as a word; punctuation, spaces, and parts of words can each contribute to token usage.

## Why tokens matter

- They affect how much text a model can read in one request.
- They influence API usage and cost on many services.
- They help explain context-window limits.

## Context window

The context window is the total amount of tokenized information a model can consider for a request, including instructions, conversation history, retrieved material, and generated output.

## Good practice

Keep prompts focused, avoid unnecessary repetition, and summarize older context when appropriate.

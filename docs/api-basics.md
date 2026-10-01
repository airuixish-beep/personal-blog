# AI API Basics

An AI API lets an application send structured requests to a model service and receive generated responses.

## Typical flow

1. Create an API credential with the provider.
2. Store it securely in an environment variable.
3. Send a request from your application.
4. Read the returned response.
5. Handle errors, rate limits, and timeouts.

## Safety notes

- Never commit API keys to GitHub.
- Use environment variables for credentials.
- Set spending limits when available.
- Avoid sending sensitive personal information unless the service and use case are appropriate.

## Learning goal

This project focuses on teaching the request/response pattern rather than providing paid API access or reselling model services.

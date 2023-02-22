# tokencal

http wrapper for computing openai tokens. https://platform.openai.com/tokenizer

---

tokencal provides an easy way to compute OpenAI tokens using HTTP. As OpenAI only provides an official SDK for Python, the project is a wrapper around the Python SDK that enables developers to obtain tokens in any programming language that supports HTTP requests, without having to directly use the OpenAI SDK. This allows for greater flexibility and easier integration with existing systems.

## How to use

```
git clone https://github.com/pandodao/tokencal.git
cd tokencal
docker compose up -d
```

The default port is `8000`, then you can do GET/POST requests.

```
% curl "http://localhost:8000/token?s=testsdflaswoer"
{"s":"testsdflaswoer","token":6}%


% curl -X POST -d '{"s":"你好"}' -H "Content-Type: application/json" "http://localhost:8000/token"
{"s":"你好","token":4}%
```

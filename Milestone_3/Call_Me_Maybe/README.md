*This project has been created as part of the 42 curriculum by masanz-s and cpfister*

[Martin GitHub](https://github.com/martinnsanzz)

# Call-Me-Maybe
*'Hey, I just met you, and this is crazy.' Carly Ray Jepsen (2011)*


## Description

**Call-Me-Maybe**

---

## Instructions

---

## Resources
This is a list of multiple resources use through out the life-cycle of the project

### LLM
[Constrained Decoding](https://www.aidancooper.co.uk/constrained-decoding/)
[Implementing Constrained Decoding](https://medium.com/@albersj66/part-6-implementing-constrained-decoding-for-phi-3-vision-2c72a1be6a17)
[Function calling with LLMs](https://www.promptingguide.ai/applications/function_calling)
[Understand Tokens](https://learn.microsoft.com/en-us/dotnet/ai/conceptual/understanding-tokens)
[LLMs -WIKI](https://en.wikipedia.org/wiki/Large_language_model)
[How do LLMs work](https://medium.com/data-science-at-microsoft/how-large-language-models-work-91c362f5b78f)
[Structured Output from LLMs](https://www.youtube.com/watch?v=xpvFinvqRCA)
[Qwen Model](https://huggingface.co/Qwen/Qwen3-0.6B)
[Qwen Docs](https://qwen.readthedocs.io/en/latest/getting_started/concepts.html)
[How Constrained Decoding Works](https://medium.com/@sebuzdugan/make-invalid-json-impossible-how-constrained-decoding-actually-works-5a512106396a)

### VENV
[UV and Environments](https://docs.astral.sh/uv/pip/environments/)
[WIriting your pyproject.toml](https://packaging.python.org/en/latest/guides/writing-pyproject-toml/)

### Python Specifics
[Argparse library](https://docs.python.org/3/library/argparse.html)
[Argparse tutorial](https://www.youtube.com/watch?v=tirLko5urBo)
[Working with JSON data in Python](https://realpython.com/python-json/)
[Using Qwen in Python](https://qwen.readthedocs.io/en/stable/getting_started/quickstart.html)
[Pytorch Doc](https://pytorch.org/)
[Regular Expressions in Python](https://www.youtube.com/watch?v=wnuBwl2ekmo)
[Python RegEx](https://www.w3schools.com/python/python_regex.asp)


---

## AI Usage

**AI was NOT used to generate code.** All function implementations were written by Martin™.

**Where AI was used:**



---

## Current Work Plan 
1. Represent each function's schema as data you already have. You don't need a new schema format — functions_definition.json already gives you name, parameters (with types), and returns for each function. Load it into a structure you can query: given a function name, what are its parameter names and types.

2. Build a "generation state" tracker. This is an object (or just a variable) that knows where you currently are in the output: are you before the opening {? Inside the "name" key's value? Which function was chosen? Inside "parameters"? Which parameter, and what type does it expect? This state changes as tokens get accepted — every accepted token may advance the state.

3. For each state, define what's legal next. Some states have a small fixed set of legal strings (e.g. right after {", the only legal continuation is name — or right after "name": ", the only legal continuations are your actual function names from step 1). Other states are open-ended patterns (a number for a "number" type parameter, arbitrary characters for a "string" type until a closing quote). Write these as either literal strings or regex patterns per state.

4. Write the prefix-check function. Given the current state and a candidate string (a token's decoded text), decide: if I append this to what's been generated, am I still consistent with what this state allows? For literals, this is a "does the token match part of my few known target strings" check. For patterns, this is a partial-match / prefix-match regex check.

5. Replace your top-5 random pick with a filtered argmax. In your loop, before picking a token, iterate the vocab (via the vocab file mapping ID→string), run each candidate through step 4's check against your current state, and only keep survivors. Then argmax the logits among survivors only.

6. Advance the state after each accepted token. Once you pick a token, update your tracker: did you just finish typing "name" and hit a quote? Move to "expecting colon" state. Did you just complete a full valid function name? Move to "parameters" scope, now bound to that function's specific parameter schema.

7. Stop condition. Instead of MAX_TOKENS as your only stopper, your state machine naturally tells you when the JSON object is complete (you've closed the final } and satisfied all required keys) — that becomes your real termination condition, separate from a token cap you might keep as a safety net.

Where do you want to start building first — the schema-lookup structure from step 1, or the state/tracker design from step 2?
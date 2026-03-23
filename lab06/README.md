 
    messages=[...],
    format=MyModel.model_json_schema()
)
result = MyModel.model_validate_json(response.message.content)
```

## Setup
Ensure Ollama is running and the model is available:
```bash
ollama pull llama3.2:latest
```

## Lab File Structure
```
lab06/
├── README.md                 # This documentation
├── lab06.py                  # Main lab script (complete the 3 functions)
├── tests/
│   ├── conftest.py           # Auto-skips tests if Ollama is not running
│   └── test_lab06.py         # Pytest tests for your implementations
```

## Lab Instructions
1. Pull the lab06 directory from the repo
2. Complete the three functions in `lab06.py`:
   - **`generate_character()`** -- Use `ollama.chat()` with `format=CharacterSheet.model_json_schema()` to generate a character sheet from a description. Parse the response with `CharacterSheet.model_validate_json()`.
   - **`generate_monster()`** -- Same pattern, using the `MonsterStats` schema.
   - **`generate_encounter()`** -- Uses the `Encounter` schema which contains nested `MonsterStats`. Craft a prompt that tells the LLM the party level, number of monsters, and theme.
3. Run the script to see structured output in action
4. Run the tests to validate your implementation

## Running
```bash
python lab06/lab06.py
```

## Testing
```bash
pytest lab06/tests/ -v
```

## References
- [Ollama Python API](https://github.com/ollama/ollama-python)
- [Ollama Structured Output Blog](https://ollama.com/blog/structured-outputs)
- [Pydantic Documentation](https://docs.pydantic.dev/)
- [JSON Schema Specification](https://json-schema.org/)

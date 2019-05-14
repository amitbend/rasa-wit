# Wit Interpreter

A `rasa_core` [Interpreter](http://rasa.com/docs/core/api/interpreter/) using Wit's API so you can build your models on wit.ai's platform and manage the dialog on **Rasa Core**

## Installation

Install using pip:

```
pip install rasa-wit
```

## Usage

```py
from rasa_wit.interpreter import WitInterpreter
from rasa_core.agent import Agent

agent = Agent.load(
    'path/to/dialogue/models',
    interpreter=WitInterpreter(
    token,
    
    ))

msg = agent.handle_text('Hey Wit!')
```

Note that due to the way that Wit currently works, the returned `entities` will not have `start` and `end` values.

### License
MIT © [Amit Bendor](https://amitbend.com)
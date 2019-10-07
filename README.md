# ORES API

This repo contains a python package called "oresapi".  This package makes it
straightforward to query the ORES API in a performant way.  

# Example

```
>>> from oresapi import Session
>>>
>>> my_session = Session(
...     "https://ores.wikimedia.org",
...     user_agent="Demonstrating how to use Session - my_address@email.com")
>>>
>>> rev_ids = [12345, 678910]
>>> results = my_session.score("enwiki", ["damaging", "goodfaith"], rev_ids)
>>>
>>> for rev_id, result in zip(rev_ids, results):
...     print(rev_id, result)
...
12345 {'goodfaith': {'score': {'prediction': True, 'probability': {'true': 0.9454305247958957, 'false': 0.05456947520410427}}}, 'damaging': {'score': {'prediction': False, 'probability': {'true': 0.1774477630070302, 'false': 0.8225522369929699}}}}
678910 {'goodfaith': {'score': {'prediction': True, 'probability': {'true': 0.9971569940025945, 'false': 0.002843005997405501}}}, 'damaging': {'score': {'prediction': False, 'probability': {'true': 0.008388045944843079, 'false': 0.9916119540551569}}}}
```

# Author
* Aaron Halfaker - https://github.com/halfak

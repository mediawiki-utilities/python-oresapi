# ORES API

This repo contains a python package called "oresapi".  This package makes it
straightforward to query the ORES API in a performant way.  

# Examples

## CLI
```
$ echo -e '{"rev_id": 123456}\n{"rev_id": 234567}' | ./utility score_revisions https://ores.wikimedia.org "example@email.org" enwiki damaging goodfaith 
2020-04-23 09:58:18,547 INFO:oresapi.utilities.score_revisions -- Reading input from <stdin>
2020-04-23 09:58:18,547 INFO:oresapi.utilities.score_revisions -- Writing output to from <stdout>
{"score": {"damaging": {"score": {"probability": {"false": 0.8895027179951033, "true": 0.11049728200489672}, "prediction": false}}, "goodfaith": {"score": {"probability": {"false": 0.0379063620644855, "true": 0.9620936379355145}, "prediction": true}}}, "rev_id": 123456}
{"score": {"damaging": {"score": {"probability": {"false": 0.980325356782424, "true": 0.01967464321757594}, "prediction": false}}, "goodfaith": {"score": {"probability": {"false": 0.011545340309922048, "true": 0.988454659690078}, "prediction": true}}}, "rev_id": 234567}
```

## Python
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

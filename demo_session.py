from oresapi import Session

my_session = Session(
    "https://ores.wikimedia.org",
    user_agent="Demonstrating how to use Session - my_address@email.com")

rev_ids = [12345, 678910]
results = my_session.score("enwiki", ["damaging", "goodfaith"], rev_ids)

for rev_id, result in zip(rev_ids, results):
    print(rev_id, result)

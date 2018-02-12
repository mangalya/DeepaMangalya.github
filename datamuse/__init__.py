import datamuse
# from datamuse import Datamuse

# api = datamuse.Datamuse()
# orange_rhymes = api.words(rel_syn='challenge',max=15)
# print(orange_rhymes)
from datamuse import scripts
foo_df = scripts.dm_to_df(foo_complete)
print(foo_df)
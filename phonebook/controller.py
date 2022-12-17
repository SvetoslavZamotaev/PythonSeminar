import view as v
from view import ShowMeAll
from view import askFor
from WriteAndSearch import WriteIn
from WriteAndSearch import Search
from logger import ShowMeTime

askFor()
if v.mode == 'find':
    Search()
elif v.mode == 'add':
    WriteIn(ShowMeTime())
elif v.mode == 'showme':
    print(ShowMeAll())

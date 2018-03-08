from datetime import datetime

doc = {
  'author': 'kimchy',
  'text': 'Elasticsearch: cool. bonsai cool.',
  'timestamp': datetime.now(),
}

query = {
  "query": {
    "match_all": {}
  }
}
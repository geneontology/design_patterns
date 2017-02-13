import yaml
from jsonschema import Draft4Validator
import sys

dosdp_core_file = open("DOSDP_schema_core.yaml", "r")
dosdp_core = yaml.load(dosdp_core_file.read())

v = Draft4Validator(dosdp_core)

pattern_docs = []

for pattern in pattern_docs:
  pattern_file = open(p, "r")
  pattern_positive = yaml.load(pattern_file.read())

  if not v.is_valid(pattern_file):
      es = v.iter_errors(pattern_file)
      for e in es: 
          print(e)
      sys.exit(1)
    
  else:
      print(True)

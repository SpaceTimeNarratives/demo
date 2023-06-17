import re
import os
from IPython.display import HTML
from collections import OrderedDict
from lemminflect import getLemma, getInflection

BG_COLOR = {
    'PLNAME':'#feca74','GEONOUN': '#9cc9cc', 'GPE':'#feca74', 'CARDINAL':'#e4e7d2',
    'FAC':'#9cc9cc','QUANTITY':'#e4e7d2','PERSON':'#aa9cfc', 'ORDINAL':'#e4e7d2',
    'ORG':'#7aecec', 'NORP':'#d9fe74', 'LOC':'#9ac9f5', 'DATE':'#c7f5a9',
    'PRODUCT':'#edf5a9', 'EVENT': '#e1a9f5','TIME':'#a9f5bc', 'WORK_OF_ART':'#e6c1d7',
    'LAW':'#e6e6c1', 'LOCADV':'#f5b5cf', 'PERCENT':'#c9ebf5', 'MONEY':'#b3d6f2',
    '+EMOTION':'#94f72a', '-EMOTION':'#f75252', 'TIME-SEM':'#d0e0f2', 'MOVEMENT':'#f2d0d0','no_tag':'#FFFFFF'
}

# Generates a dictionary of entities with the indexes as keys
def extract_entities(text, ent_list, tag='PLNAME'):
  sorted(set(ent_list), key=lambda x:len(x), reverse=True)
  extracted_entities = {}
  for ent in ent_list:
    for match in re.finditer(f' {ent}[\.,\s\n;:]', text):
      # modified to return the `tag` too...
      extracted_entities[match.start()+1]=text[match.start()+1:match.end()-1], tag
  return {i:extracted_entities[i] for i in sorted(extracted_entities.keys())}

combine = lambda x, y: (x[0], x[1], x[2]+' '+y[2], x[3])

# Combines multiple adjacent semantic tokens
# Example: [('at','TIME'), ('this','TIME'), ('point','TIME')] => [('at this point', 'TIME')] 
def combine_multi_tokens(a_list):
  new_list = [a_list.pop()]
  while a_list:
    last = a_list.pop()
    if new_list[-1][0] - last[0] == 1:
      new_list.append(combine(last, new_list.pop()))
    else:
      new_list.append(last)
  return sorted(new_list)

# Generates a dictionary of semantic entities combining adjacent ones
def extract_sem_entities(processed_text, tag_types):
  entities, tokens = {}, [token.text for token in processed_text]
  for tag_type in tag_types:
    tag_indices = [(i, token.idx, token.text, tag_type) for i, token in enumerate(processed_text) 
                        if token._.pymusas_tags[0].startswith(tag_type[0])]
    if tag_indices:
      for i, idx, token, tag in combine_multi_tokens(tag_indices):
        entities[idx] = token, tag
  return OrderedDict(sorted(entities.items()))

# Merging entities
def merge_entities(first_ents, second_ents):
  return OrderedDict(sorted({** second_ents, **first_ents}.items()))

# Generates a list of all tokens, tagged and untagged, for visualisation
def get_tagged_list(text, entities):
  begin, tokens_tags = 0, []
  for start, (ent, tag) in entities.items():
    if begin <= start:
      tokens_tags.append((text[begin:start], None))
      tokens_tags.append((text[start:start+len(ent)], tag))
      begin = start+len(ent)
  tokens_tags.append((text[begin:], None)) #add the last untagged chunk
  return tokens_tags

# Marking up the token for visualization
def mark_up(token, tag=None):
  if tag:
    begin_bkgr = f'<bgr class="entity" style="background: {BG_COLOR[tag]}; padding: 0.05em 0.05em; margin: 0 0.15em;  border-radius: 0.55em;">'
    end_bkgr = '\n</bgr>'
    begin_span = '<span style="font-size: 0.8em; font-weight: bold; border-radius: 0.35em; vertical-align: middle; margin-left: 0.5rem">'
    end_span = '\n</span>'
    return f"{begin_bkgr}{token}{begin_span}{tag}{end_span}{end_bkgr}"
  return f"{token}"

# generate html formatted text 
def visualize(text, entities):
  token_tag_list = get_tagged_list(text, entities)
  start_div = f'<div class="entities" style="line-height: 2.5; direction: ltr">'
  end_div = '\n</div>'
  html = start_div
  for token, tag in token_tag_list:
    html += mark_up(token,tag)
  html += end_div
  return HTML(html)

# Get inflections and lemmas of geo nouns
def get_inflections(names_list):
    gf_names_inflected = []
    for w in names_list:
      gf_names_inflected.append(w)
      gf_names_inflected.extend(list(getInflection(w.strip(), tag='NNS', inflect_oov=False)))
      gf_names_inflected.extend(list(getLemma(w.strip(), 'NOUN', lemmatize_oov=False)))
    return list(set(gf_names_inflected))

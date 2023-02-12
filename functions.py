!pip install lemminflect

from IPython.display import HTML
from collections import OrderedDict
from lemminflect import getLemma, getInflection

BG_COLOR = {'PLNAME':'#feca74','GEONOUN': '#9cc9cc', 'LOCADV':'#f5b5cf'}

# Generates a list of all tokens, tagged and untagged, for visualisation
def extract_entities(text, ent_list, tag='PLNAME'):
  sorted(set(ent_list), key=lambda x:len(x), reverse=True)
  extracted_entities = {}
  for ent in ent_list:
    for match in re.finditer(f' {ent}[\.,\s\n;:]', text):
      # modified to return the `tag` too...
      extracted_entities[match.start()+1]=text[match.start()+1:match.end()-1], tag
  return {i:extracted_entities[i] for i in sorted(extracted_entities.keys())}

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
def visualize(token_tag_list):
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
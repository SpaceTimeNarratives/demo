# Extracting Imprecise Geographical and Temporal References from Journey Narratives (demo)

Previous approaches to understanding geographies in textual sources tend to focus on geoparsing to automatically identify place names and allocate them to coordinates. Such methods are highly quantitative and are limited to named places for which coordinates can be found, and have little concept of time. Yet, as narratives of journeys make abundantly clear, human experiences of geography are often subjective and more suited to qualitative representation. In these cases, "geography" is not limited to named places; rather, it incorporates the vague, imprecise, and ambiguous, with references to, for example, "the camp", or "the hills in the distance", and includes the relative locations using terms such as "near to", "on the left", "north of" or "a few hours’ journey from". 

In this demonstration repository, we present a series of Python notebooks that describe our research prototypes to extract and analyze qualitative and quantitative references to place and time in two corpora of English Lake District travel writing and Holocaust survivor testimonies.

## Code Documentation
The code for this demo uses a collection of functions that extract and visualize entities and semantic tokens from a given text. It was written by an anonymous author and utilizes the `Spacy` library for natural language processing, the `lemminflect` library for inflection and lemmatization, and the `re` library for regular expression matching.

This code is useful for anyone who needs to extract and visualize entities and semantic tokens from a given text.

### Functions
The functions in this code are stored in `functions.py` file and are described as below:

- `extract_entities(text, ent_list, tag='PLNAME')`: Generates a dictionary of entities with the indexes as keys based on a list of entities and the input text.

- `get_inflections(names_list)`: Gets inflections and lemmas of geo nouns.

- `combine_multi_tokens(a_list)`: Combines multiple adjacent semantic tokens.

- `extract_sem_entities(processed_text, tag_types)`: Generates a dictionary of semantic entities combining adjacent ones based on a list of semantic token types and a processed text.

- `merge_entities(first_ents, second_ents)`: Merges two entity dictionaries.

- `get_tagged_list(text, entities)`: Generates a list of all tokens, tagged and untagged, for visualization.

- `mark_up(token, tag=None)`: Marks up a token for visualization.

- `visualize(text, entities)`: Generates and returns HTML-formatted text with tagged entitities for visualization.

## Citation
If you find the notebooks and other resources in this repository useful, kindly cite as below:

```bibtex
@inproceedings{10.1145/3615887.3627761,
author = {Ezeani, Ignatius and Rayson, Paul and Gregory, Ian and Haris, Erum and Cohn, Anthony and Stell, John and Cole, Tim and Taylor, Joanna and Bodenhamer, David and Devadasan, Neil and Steiner, Erik and Frank, Zephyr and Olson, Jackie},
title = {Towards an Extensible Framework for Understanding Spatial Narratives},
year = {2023},
isbn = {9798400703492},
publisher = {Association for Computing Machinery},
address = {New York, NY, USA},
url = {https://doi.org/10.1145/3615887.3627761},
doi = {10.1145/3615887.3627761},
booktitle = {Proceedings of the 7th ACM SIGSPATIAL International Workshop on Geospatial Humanities},
pages = {1–10},
numpages = {10},
keywords = {qualitative spatial representation, datasets, place names, corpus annotation, toponyms, ontology, named entity recognition, spatial narratives, spatio-textual regions, sense of place, location, geographical feature nouns, locale},
location = {Hamburg, Germany},
series = {GeoHumanities '23}
}
```
or

```
Ignatius Ezeani, Paul Rayson, Ian Gregory, Erum Haris, Anthony Cohn, John Stell, Tim Cole, Joanna Taylor, David Bodenhamer, Neil Devadasan, Erik Steiner, Zephyr Frank, and Jackie Olson. 2023. Towards an Extensible Framework for Understanding Spatial Narratives. In Proceedings of the 7th ACM SIGSPATIAL International Workshop on Geospatial Humanities (GeoHumanities '23). Association for Computing Machinery, New York, NY, USA, 1–10. https://doi.org/10.1145/3615887.3627761
```

## Licence
To be confirmed...

## Acknowledgements
The [Space Time Narratives project](https://spacetimenarratives.github.io/) is funded in the UK from 2022 to 2025 by ESRC, project reference: [ES/W003473/1](https://gtr.ukri.org/projects?ref=ES%2FW003473%2F1). We also acknowledge the input and advice from the other members of the project team in generating requirements for our research presented here. More details of the project can be found on the [website](https://spacetimenarratives.github.io/).

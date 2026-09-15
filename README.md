# PUPILA

PUPILA is a local-first engine for translating a task from an interface a
person already knows to an interface they do not know yet.

The engine does not copy a visual interface, execute clicks, or assume that
two applications have the same internal implementation. It compares declared
capabilities, roles, actions, labels, modalities, and preconditions, then
returns a reviewable candidate set with evidence and uncertainty.

## Boundary

```text
interface snapshot A + task intent
        -> PUPILA association
        -> candidate mappings + evidence + ambiguity
        -> human or host application decides whether to apply
```

The first slice is deliberately provider-independent. An agent may supply a
snapshot or explain a mapping, but PUPILA remains the contract and verifier;
it is not a chatbot and it never commits an external action.

## Modules

- `src/pupila/`: compares declared interface capabilities and maps a task
  between a familiar and an unfamiliar surface, retaining ambiguity and
  evidence per source element.
- `visual/`: deterministic CPU geometry for supplied visual measurements,
  including calibration gates, screen-plane intersections and operation
  context. It does not capture camera frames, run an eye-tracking model or
  claim physical calibration from synthetic data.

The product direction includes both direct help and analogical transfer. The
current executable assistance slice is the task-mapping engine; automatic
detection of a learner becoming stuck, from live application events, is not
implemented here. Host adapters must supply bounded observations explicitly.

## Run

```text
python -m unittest discover -s tests -v
PYTHONPATH=visual/src python -m unittest discover -s visual/tests -v
```

## Product boundary

The repository contains generic algorithms and contracts only. It does not
contain MAK works, private archives, credentials, user recordings, or an
application-specific corpus.

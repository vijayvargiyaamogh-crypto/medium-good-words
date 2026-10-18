# Medium Good Words

A Python solver for finding words in a 5x5 letter grid.

## How it works

The solver uses a trie and depth-first search (DFS) to find words.
- Each cell can be used at most once per word.
- All eight neighboring directions are allowed.
- Words must contain at least four letters.
- Results are printed in descending order of word length.

## Requirements

Python 3 and the included trie.pkl file.

## Usage

Run python medium_good_words.py from this directory.
Enter five rows of five letters, one row per line.

## Files

- medium_good_words.py: the word-search algorithm.
- trie.pkl: the prebuilt trie used by the solver.
- re-enable.txt: the included text word list.

# Music_ID (example of how Shazam works)
Build database of songs given using glob function, then build signatures for each song and for single test song wanted to be matched using  spectogram function. Then take five highest values found using the normalization and print out song names. Plot three closest values of their spectogram.

# Add music files
First download zip files which contain the snippets of songs to build library from and also the songs used that are corrupted or different from original songs to use to find within library of songs. Those corrupted files will be our test files. They start a few seconds after actual songs start to prove that it will correctly match up song even when out of sync.

# Try different songs
On line 48, just change the name of the song to one of the other test songs from the zip folder to prove each songs works.

# What's needed
Numpy is used and soundfile libraries need to be installed. Runs on python 3.7.

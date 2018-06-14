# README

Library give the ability to search for words in an interval and splice out the intervals to smaller files.
## Libraries needed:

 For splicing out intervals
 - Pydub: https://github.com/jiaaro/pydub#installation

 For understanding the TextGrid files
 - TextGrid: https://github.com/kylebgorman/textgrid

 Commands to install:

 `pip install pydub textgrid`


## Usage
Imagine we have an mp3 and a TextGrid file called `bilen` and we are looking for "t"-intervals:
we would run:

`python splice_praat_into_seperate_files.py -i bilen.mp3 -t bilen.TextGrid -s "t"`

the spliced files will be put in the output folder
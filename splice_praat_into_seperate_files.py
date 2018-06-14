# For args
import getopt
import sys
import textgrid
from pydub import AudioSegment


def print_usage():
    print 'splice_praat_into_seperate_files.py -i <inputfile> -t <TextGridFile> -o <outputfolder> -s \"textToSearchFor\"'


def main(argv):
    inputTextGridFile = ''
    inputFile = ''
    outputFolder = 'output/'
    search_for_mark = ''
    try:
        # opts is a list of returning key-value pairs, args is the options left after striped
        # the short options 'hi:o:', if an option requires an input, it should be followed by a ":"
        # the long options 'ifile=' is an option that requires an input, followed by a "="
        opts, args = getopt.getopt(argv, "hi:o:t:s:", ["ifile=", "tfile=", "ofolder=", "search_string="])
    except getopt.GetoptError:
        print_usage()
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print_usage()
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputFile = arg
        elif opt in ("-t", "--tfile"):
            inputTextGridFile = arg
        elif opt in ("-o", "--ofolder"):
            outputFolder = arg
        elif opt in ("-s", "--search_string"):
            search_for_mark = arg
    print 'Input file is: ', inputFile
    print 'Input TextGrid: ', inputTextGridFile
    print 'Output folder is: ', outputFolder
    print 'Searching for: ', search_for_mark


    splice_ts(inputFile, outputFolder, inputTextGridFile, search_for_mark)


def splice_ts(inputFile, outputFolder, textgrid_file, search_for):
    tg = textgrid.TextGrid.fromFile(textgrid_file)
    sound = AudioSegment.from_mp3(inputFile)
    count = 0
    for interval in xrange(len(tg[0])):
        stuff = tg[0][interval]

        if stuff.mark == search_for:
            count = count + 1
            start_of_interval = int(stuff.minTime*1000)  # Get time in milliseconds
            end_of_interval = int(stuff.maxTime*1000)  # Convert to integer

            # Concatenate
            interesting_part = sound[start_of_interval:end_of_interval]

            interesting_part.export(outputFolder + search_for + str(count) + ".mp3", format="mp3")

            print(str(start_of_interval) + " -> " + str(end_of_interval) + " :: " + stuff.mark)


if __name__ == "__main__":
    main(sys.argv[1:])
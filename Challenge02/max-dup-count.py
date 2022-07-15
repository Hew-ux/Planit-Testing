#!/usr/bin/python3
import sys
import argparse

class CharacterManipulator:

    @staticmethod
    def duplicates(string):
        # Nuke the capitalisation.
        string = string.lower()

        # Initialise count as a dictionary (we are going to be storing multiple
        # integer values in this).
        count = {}

        # Loop through all the characters in the string.
        for i in string:
            if i in count:
                # Add one to that particular element in the dictionary.
                count[i] += 1
            else:
                count[i] = 1

        # Find the maximum value of the count. This info by itself is useless, we
        # need the first character in the string with which it matches.
        MaximumDuplicates = max(count.values())

        # Convert the dictionary into two lists, using their position as information.
        Characters = list(count.keys())
        Values = list(count.values())

        # Initialise CharacterWithHighestOccurrences variable as a string.
        CharacterWithHighestOccurrences = ""

        # Find the first occurence of the MaximumDuplicates value and save its
        # matching key to the variable.
        CharacterWithHighestOccurrences = Characters[Values.index(MaximumDuplicates)] + "\n"

        return CharacterWithHighestOccurrences

if __name__ == "__main__":
  # Set up the parser.
  parser = argparse.ArgumentParser( description = "Find the character" \
  " which has the highest number of occurrences in the given string." \
  " If two characters occur the same amount, return the first one that" \
  " appears in the string." )
  # Add available inputs.
  #parser.add_argument('-v', '--verbose', help="turn on debug messages", action="store_true" )
  parser.add_argument('string', metavar='<string>', help="The string this program will analyse to see which character occurs the most.")
  args = parser.parse_args()

  # Save the output of the duplicates counter.
  output = CharacterManipulator.duplicates(args.string)

  # Write the output to the standard output.
  sys.stdout.write(output)
  sys.stdout.flush()
  # Exit
  sys.exit(0)

import argparse
import glob
import logging
import os

logging.basicConfig(format='[%(asctime)s] %(levelname)-8s | %(message)s',
                    datefmt='%d-%b-%Y %H:%M:%S', level=logging.INFO)
log = logging.getLogger()

args_parser = argparse.ArgumentParser(description='Merges two or more text files')
args_parser.add_argument('-path', dest='path', default='files',
                         help='The path to the directory that contains the files to merge (default is \'files\')')
args_parser.add_argument('-ext', dest='file_extension', default='',
                         help='The extension of the files to merge (merges everything by default)')
args_parser.add_argument('-out', dest='out_file', default='output.txt',
                         help='Merged lines output file name')
args_parser.add_argument('-no_duplicates', dest='no_duplicates', action='store_true',
                         help='Prevent duplicate lines')
args_parser.add_argument('-sort', dest='sort', action='store_true',
                         help='Sort merged lines')
args_parser.add_argument('-prefix_before', dest='prefix_before', default='',
                         help='The prefix to replace in each line before merging. -prefix_after must be provided')
args_parser.add_argument('-prefix_after', dest='prefix_after', default='',
                         help='The new prefix each line before merging. If -prefix_after was not provided, '
                              'this will be used to strip the prefix by splitting the line and removing the first part')
args_parser.add_argument('-suffix_before', dest='suffix_before', default='',
                         help='The suffix to replace in each line before merging. -suffix_after must be provided')
args_parser.add_argument('-suffix_after', dest='suffix_after', default='',
                         help='The new suffix each line before merging. If -suffix_before was not provided, '
                              'this will be used to strip the suffix by splitting the line and removing the last part')


class TextFilesMerger:
    """ Merges two or more text files, line by line.

    Optional features:
     - Remove duplicate lines
     - Sort merged lines
     - Prefix and suffix alteration before merging

    Args:
        path: The path to the directory that contains the files to merge
        file_extension: The extension of the files to merge
        out_file: Merged lines output file name
        no_duplicates: If True, prevents duplicate lines
        prefix_before: The prefix to replace in each line before merging. prefix_after must be provided
        prefix_after: The new prefix each line before merging. prefix_before must be provided
        suffix_before: The suffix to replace in each line before merging. suffix_after must be provided
        suffix_after: The new suffix each line before merging. suffix_before must be provided
    """

    def __init__(self, path, file_extension, out_file, no_duplicates, sort, prefix_before, prefix_after, suffix_before,
                 suffix_after):
        self.path = path
        self.file_extension = file_extension
        self.out_file = out_file
        self.no_duplicates = no_duplicates
        self.sort = sort
        self.prefix_before = prefix_before
        self.prefix_after = prefix_after
        self.suffix_before = suffix_before
        self.suffix_after = suffix_after

    def merge(self):
        if not self.file_extension:
            file_pattern = '**/*'
            log.info('All files in \'{}\' will be merged.'.format(self.path))
        else:
            file_pattern = '**/*.{}'.format(self.file_extension)
            log.info('\'{}\' files in \'{}\' will be merged.'.format(self.file_extension, self.path))

        all_lines = []
        for file in glob.glob(os.path.join(self.path, file_pattern), recursive=True):
            if os.path.isdir(file):
                continue
            log.info('Merging lines from: {}'.format(file))
            with open(file, 'r') as fi:
                lines = fi.read().splitlines()
                lines = [self._alter_prefix_and_suffix(line) for line in lines]
                all_lines += lines

        if self.no_duplicates:
            log.info('Removing duplicate lines')
            all_lines = set(all_lines)

        if self.sort:
            log.info('Sorting lines')
            all_lines = sorted(all_lines)

        with open(self.out_file, 'w') as fo:
            fo.write("\n".join(all_lines))

    def _alter_prefix_and_suffix(self, line):
        if self.prefix_before and self.prefix_after:
            line = line[len(self.prefix_before):] if line.startswith(self.prefix_before) else line
        elif not self.prefix_before and self.prefix_after:
            line = line.split(self.prefix_after)[1] if self.prefix_after else line
        if self.suffix_before and self.suffix_after:
            line = line[:-len(self.prefix_before)] if line.endswith(self.prefix_before) else line
        elif not self.suffix_before and self.suffix_after:
            line = line.split(self.suffix_after)[0] if self.suffix_after else line
        return line


if __name__ == '__main__':
    args = args_parser.parse_args()
    merger = TextFilesMerger(args.path, args.file_extension, args.out_file, args.no_duplicates, args.sort,
                             args.prefix_before, args.prefix_after, args.suffix_before, args.suffix_after)
    log.info('Merging files...')
    merger.merge()
    log.info('Done')

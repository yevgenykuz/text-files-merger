Text Files Merger
#################

This script does the following:

1. Takes one or more input files
2. [Optional] Alters prefix and suffix of each line from the input files (in memory, original files are untouched)
3. [Optional] Removes duplicate lines
4. [Optional] Sorts lines
5. Merges all lines and saves result to a new file

-----


.. contents::

.. section-numbering::

Usage
=====
This project requires:

* Python >=3.6

Clone the source code
---------------------
In your working folder (your home folder, for example)

.. code-block:: bash

    git clone https://github.com/yevgenykuz/text-files-merger.git

Configure and run
-----------------
Run with (*see arguments*):

.. code-block:: bash

    python merge_files.py

For example, the following will merge, sort, remove duplicates, and strip everything after "_-" suffix (including)
all .txt files in the relative "files" directory. Result will be saved to "output.txt" file:

.. code-block:: bash

    python merge_files.py -e="txt" -d -s -sa="_-"


Arguments
---------

.. code-block::

    usage: merge_files.py [-h] [-p PATH] [-e FILE_EXTENSION] [-o OUT_FILE] [-d]
                      [-s] [-pb PREFIX_BEFORE] [-pa PREFIX_AFTER]
                      [-sb SUFFIX_BEFORE] [-sa SUFFIX_AFTER]

    optional arguments:
      -h, --help         show this help message and exit
      -p PATH            The path to the directory that contains the files to
                         merge (default is 'files')
      -e FILE_EXTENSION  The extension of the files to merge (merges everything by
                         default)
      -o OUT_FILE        Merged lines output file name
      -d                 Prevent duplicate lines
      -s                 Sort merged lines
      -pb PREFIX_BEFORE  The prefix to replace in each line before merging.
                         -prefix_after must be provided
      -pa PREFIX_AFTER   The new prefix each line before merging. If
                         -prefix_before was not provided, this will be used to
                         strip the prefix by splitting the line and removing the
                         first part
      -sb SUFFIX_BEFORE  The suffix to replace in each line before merging.
                         -suffix_after must be provided
      -sa SUFFIX_AFTER   The new suffix each line before merging. If
                         -suffix_before was not provided, this will be used to
                         strip the suffix by splitting the line and removing the
                         last part


Meta
====
Authors
-------
`yevgenykuz <https://github.com/yevgenykuz>`_

License
-------
`MIT License <https://github.com/yevgenykuz/text-files-merger/blob/master/LICENSE>`_

-----

#!/usr/bin/env python3
"""
Script for updating the output files using the current behavior.
"""
import sys

sys.path.append("..")
sys.path.append(".")

from glob import glob
import re
from typing import cast, List
from os import path

from corpus2alpino.converter import Converter
from corpus2alpino.collectors.filesystem import FilesystemCollector
from corpus2alpino.targets.filesystem import FilesystemTarget
from corpus2alpino.writers.lassy import LassyWriter
from corpus2alpino.writers.paqu import PaQuWriter

args = sys.argv[1:]
if args:
    patterns = args[0].split(",")
else:
    patterns = ["example*.xml", "example*.txt", "example*.cha"]

test_files = cast(List[str], [])
for pattern in patterns:
    test_files += (
        f
        for f in glob(path.join(path.dirname(__file__), pattern))
        if "_expected" not in f
    )

writers = [("txt", PaQuWriter()), ("xml", LassyWriter(True))]

for ext, writer in writers:
    for test_file in test_files:
        expected_filename = re.sub("\.(txt|xml|cha)$", "_expected." + ext, test_file)
        converter = Converter(
            FilesystemCollector([test_file]),
            target=FilesystemTarget(expected_filename, True),
            writer=writer,
        )

        # make sure the complete conversion is done
        list(converter.convert())

from test_enrich_lassy import get_enriched

with open("enrichment_expected.xml", mode="w", encoding="utf-8") as expected_file:
    expected_file.write(get_enriched())

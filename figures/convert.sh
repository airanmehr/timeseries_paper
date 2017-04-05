#!/usr/bin/env bash

for f in $(ls *.tiff); do  convert $f ${f%.tiff}.eps; done
pdf2ps ExperimentalEvolution.pdf ExperimentalEvolution.eps
pdf2ps HMMGM.pdf HMMGM.eps

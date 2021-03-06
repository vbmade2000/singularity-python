#!/usr/bin/env python

# This is an example of generating image packages from within python

from singularity.analysis.classify import estimate_os

image_package = "python:3.6.0.img.zip"

# We can obtain the estimated os (top match)
estimated_os = estimate_os(image_package=image_package)
# Most similar OS found to be %s debian:7.11

# We can also get the whole list and values
os_similarity = estimate_os(image_package=image_package,return_top=False)

# If you want to sort
os_similarity.sort_values(by=['SCORE'])

#!/usr/bin/env python3

__author__ = ['[Brandon Amos](http://bamos.github.io)']
__date__ = '2015.06.06'

"""
Detect and remove duplicate images using average hashing.

http://www.hackerfactor.com/blog/index.php?/archives/432-Looks-Like-It.html
"""

import argparse
import hashlib
import imagehash
import os
import sys

from collections import defaultdict
from PIL import Image


def getImgs(d):
    """Get the images from the test directory, partitioned by class."""
    exts = ["jpg", "png"]

    imgClasses = []  # Images, separated by class.
    for subdir, dirs, files in os.walk(d):
        imgs = []
        for fName in files:
            (imageClass, imageName) = (os.path.basename(subdir), fName)
            if any(imageName.lower().endswith("." + ext) for ext in exts):
                imgs.append(os.path.join(subdir, fName))
        imgClasses.append(imgs)
    return imgClasses


def getHash(imgPath):
    """Get the hash of an image, and catch exceptions if the image
    file is corrupted."""
    try:
        return imagehash.average_hash(Image.open(imgPath))
    except:
        return None


def runOnClass(args, imgs):
    """Find and remove duplicates within an image class."""
    d = defaultdict(list)
    for imgPath in imgs:
        imgHash = getHash(imgPath)
        if imgHash:
            d[imgHash].append(imgPath)

    numFound = 0
    for imgHash, imgs in d.items():
        if len(imgs) > 1:
            print("{}: {}".format(imgHash, " ".join(imgs)))
            numFound += len(imgs) - 1  # Keep a single image.

            if args.delete:
                largestImg = max(imgs, key=os.path.getsize)
                print("Keeping {}.".format(largestImg))
                imgs.remove(largestImg)
                for img in imgs:
                    os.remove(img)

            if args.sha256:
                print("")
                for img in imgs:
                    print(hashlib.sha256(open(img, 'rb').read()).hexdigest())
                print("")
    return numFound

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('inplaceDir', type=str,
                        help="Directory of images, divided into "
                        "subdirectories by class.")
    parser.add_argument('--delete', action='store_true',
                        help="Delete the smallest duplicate images instead "
                        "of just listing them.")
    parser.add_argument('--sha256', action='store_true',
        help="Show sha256 sum for duplicate images")
    args = parser.parse_args()

    numFound = 0
    for imgClass in getImgs(args.inplaceDir):
        numFound += runOnClass(args, imgClass)
    print("\n\nFound {} total duplicate images.".format(numFound))

#!/usr/bin/env python2

import sys
sys.path.append("/home/bamos/repos/caffe-local/python")

import argparse
import numpy as np
import os
import time

from caffe.proto import caffe_pb2
from caffe.io import array_to_blobproto
from collections import defaultdict
from skimage import io

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('meanPrefix', type=str, help="Prefix of the mean file.")
    parser.add_argument('imageDir', type=str, help="Directory of images to read.")
    args = parser.parse_args()

    exts = ["jpg", "png"]

    mean = np.zeros((1, 3, 152, 152))
    N = 0
    classSizes = defaultdict(int)

    beginTime = time.time()
    for subdir, dirs, files in os.walk(args.imageDir):
        for fName in files:
            (imageClass, imageName) = (os.path.basename(subdir), fName)
            if any(imageName.lower().endswith("." + ext) for ext in exts):
                img = io.imread(os.path.join(subdir, fName))
                if img.shape == (152, 152, 3):
                    mean[0][0] += img[:, :, 0]
                    mean[0][1] += img[:, :, 1]
                    mean[0][2] += img[:, :, 2]
                    N += 1
                    if N % 1000 == 0:
                        elapsed = time.time() - beginTime
                        print("Processed {} images in {:.2f} seconds. "
                              "{:.2f} images/second.".format(N, elapsed,
                                                             N / elapsed))
    mean[0] /= N

    blob = array_to_blobproto(mean)
    with open("{}.binaryproto".format(args.meanPrefix), 'wb') as f:
        f.write(blob.SerializeToString())
    np.save("{}.npy".format(args.meanPrefix), mean[0])

    meanImg = np.transpose(mean[0].astype(np.uint8), (1, 2, 0))
    io.imsave("{}.png".format(args.meanPrefix), meanImg)

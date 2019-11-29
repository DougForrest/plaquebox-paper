#!/bin/bash

declare -a urls=("https://zenodo.org/record/1470797/files/Dataset%201a%20Development_train.zip?download=1"
				   "https://zenodo.org/record/1470797/files/Dataset%202%20Hold-out.zip?download=1"
					"https://zenodo.org/record/1470797/files/Dataset%203%20CERAD-like%20hold-out.zip?download=1")

declare -a filenames=('Dataset%201a%20Development_train.zip'
						'Dataset%202%20Hold-out.zip'
						'Dataset%203%20CERAD-like hold-out.zip')


for i in "${!urls[@]}"; do
  curl ${urls[$i]} | gsutil cp - gs://plaquebox-paper/data/${filenames[$i]}
done

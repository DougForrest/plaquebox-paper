#! /bin/bash

# Update fast ai library
sudo /opt/anaconda3/bin/conda install -yc fastai fastai

sudo apt-get install -y libvips
pip install pyvips

cd ~
git clone https://github.com/DougForrest/plaquebox-paper.git /home/jupyter/plaquebox-paper/
cd /home/jupyter/plaquebox-paper/

export MOUNT_DIR=disk-1
export DEVICE_ID=sdb
sudo mkdir -p /mnt/disks/$MOUNT_DIR
sudo mount -o discard,defaults /dev/$DEVICE_ID /mnt/disks/$MOUNT_DIR

export GCP=gcp
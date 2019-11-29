#! /bin/bash

export MOUNT_DIR=disk-1
export DEVICE_ID=sdb
sudo mkdir -p /mnt/disks/$MOUNT_DIR
sudo mount -o discard,defaults /dev/$DEVICE_ID /mnt/disks/$MOUNT_DIR
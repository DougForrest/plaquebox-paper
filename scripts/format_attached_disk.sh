sudo lsblk

sudo mkfs.ext4 -m 0 -F -E lazy_itable_init=0,lazy_journal_init=0,discard /dev/sdb

sudo mkdir -p /mnt/disks/disk-1


sudo mount -o discard,defaults /dev/sdb /mnt/disks/disk-1

sudo chmod a+w /mnt/disks/disk-1

echo UUID=`sudo blkid -s UUID -o value /dev/sdb` /mnt/disks/disk-1 ext4 discard,defaults,nofail 0 2 | sudo tee -a /etc/fstab
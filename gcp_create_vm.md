# Setup

# Create service account
Run the following commands using the Cloud SDK on your local machine, or in Cloud Shell to allow access to google storage.

```bash
export SERVICE_ACCT_NAME="plaquebox-paper-storage-sa"
export SERVICE_ACCT_NAME="storage"
export PROJECT_ID="plaquebox-paper"
export KEY_FILE="plaquebox-paper-key"

# Create the service account.
gcloud iam service-accounts create $SERVICE_ACCT_NAME

# Grant permissions to the service account.
gcloud projects add-iam-policy-binding $PROJECT_ID --member "serviceAccount:${SERVICE_ACCT_NAME}@${PROJECT_ID}.iam.gserviceaccount.com" --role "roles/owner"

# Generate the key file.
gcloud iam service-accounts keys create $KEY_FILE.json --iam-account $SERVICE_ACCT_NAME@$PROJECT_ID.iam.gserviceaccount.com


# Add a role to a single service account.
gcloud projects add-iam-policy-binding $PROJECT_ID \
  --member serviceAccount:$SERVICE_ACCT_NAME@$PROJECT_ID.iam.gserviceaccount.com \
  --role roles/iam.serviceAccountUser

export INSTANCE_NAME="plaquebox-paper-prep-vm"
export ZONE="us-west1-b" # budget: "us-west1-b"
# Setting on an already created instance
gcloud compute instances set-service-account $INSTANCE_NAME \
	--service-account $SERVICE_ACCT_NAME@$PROJECT_ID.iam.gserviceaccount.com \
	--scopes storage-full \
	--zone $ZONE
```

# Set env vars and create compute instance

```bash
export IMAGE_FAMILY="pytorch-latest-gpu" # or "pytorch-latest-cpu" for non-GPU instances
export ZONE="us-west1-b" # budget: "us-west1-b"
export INSTANCE_NAME="plaquebox-paper-prep-vm-6"
export INSTANCE_TYPE="n1-standard-8" # budget: "n1-highmem-4"

# budget: 'type=nvidia-tesla-k80,count=1'
# launch and create disk
gcloud compute instances create $INSTANCE_NAME \
		--project=$PROJECT_ID \
        --zone=$ZONE \
        --image-family=$IMAGE_FAMILY \
        --image-project=deeplearning-platform-release \
        --maintenance-policy=TERMINATE \
        --machine-type=$INSTANCE_TYPE \
        --boot-disk-size=300GB \
        --service-account=$SERVICE_ACCT_NAME@$PROJECT_ID.iam.gserviceaccount.com \
	    --scopes=https://www.googleapis.com/auth/cloud-platform \
	    --create-disk=mode=rw,size=500,type=projects/plaquebox-paper/zones/$ZONE/diskTypes/pd-ssd,name=disk-1,device-name=disk-1


# Preprocessing machine
export INSTANCE_NAME="plaquebox-paper-prep-vm-10"
export INSTANCE_TYPE="n1-standard-64"
# Launch existing disk
gcloud compute instances create $INSTANCE_NAME \
		--project=$PROJECT_ID \
        --zone=$ZONE \
        --image-family=$IMAGE_FAMILY \
        --image-project=deeplearning-platform-release \
        --maintenance-policy=TERMINATE \
        --machine-type=$INSTANCE_TYPE \
        --boot-disk-size=300GB \
        --service-account=$SERVICE_ACCT_NAME@$PROJECT_ID.iam.gserviceaccount.com \
	    --scopes=https://www.googleapis.com/auth/cloud-platform \
		--disk=name=disk-1,device-name=disk-1,mode=rw,boot=no \
		--metadata-from-file startup-script=/Users/doug/code/alzheimer/plaquebox-paper/scripts/startup.sh


# NN training machine
export PROJECT_ID="plaquebox-paper"
export SERVICE_ACCT_NAME="storage"
export INSTANCE_NAME="plaquebox-paper-nn-4"
# export INSTANCE_TYPE="n1-highmem-8"
export INSTANCE_TYPE="n1-standard-2"
export IMAGE_FAMILY="pytorch-latest-gpu"
export ZONE="us-west1-b"
# Launch existing disk
gcloud compute instances create $INSTANCE_NAME \
		--project=$PROJECT_ID \
        --zone=$ZONE \
        --image-family=$IMAGE_FAMILY \
        --image-project=deeplearning-platform-release \
        --maintenance-policy=TERMINATE \
        --machine-type=$INSTANCE_TYPE \
        --boot-disk-size=300GB \
        --service-account=$SERVICE_ACCT_NAME@$PROJECT_ID.iam.gserviceaccount.com \
	    --scopes=https://www.googleapis.com/auth/cloud-platform \
		--disk=name=disk-1,device-name=disk-1,mode=rw,boot=no \
		--metadata-from-file startup-script=./scripts/startup.sh

        --accelerator="type=nvidia-tesla-t4,count=1" \


```

# Connect to serial port (Optional)
To debug boot and networking issues, troubleshoot malfunctioning instances
```bash
gcloud compute connect-to-serial-port $INSTANCE_NAME
```


# SSH into Instance
```bash
# Connect via ssh
gcloud compute ssh --zone=$ZONE --project=$PROJECT_ID jupyter@$INSTANCE_NAME -- -L 8080:localhost:8080

gcloud compute ssh --zone=$ZONE --project=$PROJECT_ID $INSTANCE_NAME
```


# Stop Instance
```bash
# Unmount disk
# SSH into the machine and run
export MOUNT_DIR=disk-1
sudo umount /dev/disk/by-id/google-$MOUNT_DIR

#Stop instance
gcloud compute instances stop $INSTANCE_NAME

#Detach disk
gcloud compute instances detach-disk $INSTANCE_NAME --disk=$MOUNT_DIR --zone=$ZONE --project=$PROJECT_ID


```

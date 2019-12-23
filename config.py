from datetime import datetime
import os 


experiment_name = 'resnet50'

data_dir = os.path.join('/mnt', 'disks', 'disk-1', 'data')

output_path = os.path.join(data_dir,
                           experiment_name)

csv_dir = os.path.join('data', 'CSVs')
models_dir = os.path.join(output_path, 'models')
csv_path = {
    'train': os.path.join(csv_dir, 'tiles_train.csv'),
    'validation': os.path.join(csv_dir, 'tiles_validation.csv'),
    'test': os.path.join(csv_dir, 'tiles_test.csv'),
}

img_path = os.path.join(data_dir,
                        'tiles', 'tiles')

img_path_test = os.path.join(data_dir,
                        'tiles', 'tiles')

image_classes = ['cored', 'diffuse', 'CAA']


run_date = datetime.now().strftime('%Y_%m_%d')

if not os.path.exists(output_path):
    os.makedirs(output_path)
    print("Config.py creating local data directory {}".format(output_path))
else:
    print("Config.py using existing local data directory {}".format(output_path))

if not os.path.exists(models_dir):
    os.makedirs(models_dir)
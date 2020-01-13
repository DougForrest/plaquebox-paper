from datetime import datetime
import os
from fastai.vision import models


experiment_name = 'original_w_negative'
experiment_description = """Using the original dataset including
                            the null observations"""

batch_size = 256
model_name = 'resnet18'
image_size = 256
model = models.resnet18
databunch_train_validation = 'databunch_train_validation.pkl'
databunch_test = 'databunch_test.pkl'
v1_epochs = 10
v2_epochs= 20

run_date = datetime.now().strftime('%Y_%m_%d')

if os.environ.get('USER', None) == 'jupyter':
    input_path = os.path.join('/mnt', 'disks', 'disk-1', 'data', 'tiles')
    output_path = os.path.join('/mnt', 'disks', 'disk-1', 'data')
    csv_dir = os.path.join('data', 'CSVs')
    gs_bucket = "gs://plaquebox-paper/experiment"
    gs_results_dir = f"gs://plaquebox-paper/experiment/{experiment_name}/results"
    gs_data_dir = f"gs://plaquebox-paper/experiment/{experiment_name}/data"
    gs_model_dir = f"gs://plaquebox-paper/experiment/{experiment_name}/model"
    
else:
    input_path = os.path.join('data')
    output_path = input_path
    csv_dir = os.path.join(input_path, 'CSVs')

results_dir = os.path.join(os.path.join(output_path,
                                        experiment_name,
                                        'results'))

data_dir = os.path.join(os.path.join(output_path,
                                     experiment_name,
                                     'data'))

model_dir = os.path.join(os.path.join(output_path,
                                      experiment_name,
                                      'model'))

for dir_name in [results_dir, data_dir, model_dir]:
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)

train = os.path.join(csv_dir, 'train_multilabel.csv')
validation = os.path.join(csv_dir, 'validation_multilabel.csv')
test = os.path.join(csv_dir, 'test_multilabel.csv')

img_path = os.path.join(input_path,
                        'tiles')

img_path_test = os.path.join(input_path,
                             'tiles')

image_classes = ['cored', 'diffuse', 'CAA']

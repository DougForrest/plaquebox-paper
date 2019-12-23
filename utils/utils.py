import datetime
import os
import json


def load_json(filepath):

    with open(filepath) as f:
        data = json.load(f)

    return(data)


def save_json(data, filepath, indent=2):

    with open(filepath, 'w') as f:
        json.dump(data, f, indent=indent)
        
        
def walk_dir(parent_dir):

    results = []
    crawl_cnt = 0
    for dir_name, sub_dir_list, file_list in os.walk(parent_dir):
        for file_name in file_list:

            file_path = os.path.join(os.path.realpath(dir_name), file_name)

            file_info = {}
            file_info['path'] = file_path
            file_info['filename'] = os.path.basename(file_path)
            file_info['file_type'] = os.path.splitext(file_path)[1].lower()
            # file_info['modified_date'] = time.strftime("%Y%m%dT%H%M%S000+10:00", time.gmtime(os.stat(file_path).st_mtime))
            # file_info['created_date'] = time.strftime("%Y%m%dT%H%M%S000+10:00", time.gmtime(os.stat(file_path).st_ctime))
            try:
                file_info['modified_date'] = datetime.date.fromtimestamp(os.path.getmtime(file_path))
                file_info['created_date'] = datetime.date.fromtimestamp(os.path.getctime(file_path))
                file_info['size'] = os.path.getsize(file_path)
                file_info['error'] = False

            except Exception as e:
                print(e)
                file_info['error'] = True

            file_info['crawl_cnt'] = crawl_cnt
            results.append(file_info)
            crawl_cnt += 1

    return (results)
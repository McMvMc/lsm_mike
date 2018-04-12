import os
import json

def prepare_custom_db(f, im_folder, data_split):
    model_list = [o for o in os.listdir(im_folder)
                  if os.path.isdir(os.path.join(im_folder,o))]
    with open(f, 'w') as out:
        json.dump({im_folder: {
            "name":"cars",
            data_split: model_list}}, out)


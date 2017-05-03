import os
import glob


sample_root_directory = '/Users/vihanggodbole/Developer/restaurant-menu-ocr/train_data_to_remove/'
root_directory = '/Users/vihanggodbole/Developer/restaurant-menu-ocr/English/Fnt/'

paths = glob.glob(sample_root_directory + '/*.png')
paths = [path.split('-')[3].split('.')[0] for path in paths]    # contains file numbers

print(paths[0])

paths_to_remove = glob.glob(root_directory + '**/*.png')
print(len(paths_to_remove))
for path in paths:
    for other_path in paths_to_remove:
        if other_path.endswith(path + '.png'):
            os.remove(other_path)

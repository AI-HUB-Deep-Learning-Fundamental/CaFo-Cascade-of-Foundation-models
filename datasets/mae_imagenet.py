import os
from .utils import Datum, DatasetBase, read_json, write_json, build_data_loader
from .oxford_pets import OxfordPets

class MAE_Imagenet(DatasetBase):
    
    dataset_dir = 'mae_imagenet'

    def __init__(self, root, num_shots):
        # root = os.path.abspath(os.path.expanduser(cfg.DATASET.ROOT))
        assert num_shots <= 2
        self.dataset_dir = os.path.join(root, self.dataset_dir)
        self.image_dir = os.path.join(self.dataset_dir, 'images')
        self.split_path = os.path.join(self.dataset_dir, 'mae_image_2shot.json')

        train, val, test = OxfordPets.read_split(self.split_path, self.image_dir)
        train = self.generate_fewshot_dataset(train, num_shots=num_shots)

        super().__init__(train_x=train, val=val, test=test)
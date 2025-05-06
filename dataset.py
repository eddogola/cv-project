from torch.utils.data import Dataset
from PIL import Image
import json
import os


class ZindDataset(Dataset):
    def __init__(self, data_path, size=1575):
        self.data_path = data_path
        self.data = []
        
        for i in range(size):
            dir_path = os.path.join(data_path, f"{i:04d}")

            floor_plans = []
            panos = []
            room_layout = None
            
            floor_plans_path = os.path.join(dir_path, "floor_plans")
            panos_path = os.path.join(dir_path, "panos")
            room_layout_json_path = os.path.join(dir_path, "zind_data.json")

            with open(room_layout_json_path, "r") as f:
                room_layout = json.load(f)
            
            for floor_plan_file in os.listdir(floor_plans_path):
                floor_plan_path = os.path.join(floor_plans_path, floor_plan_file)
                floor_plan_img = Image.open(floor_plan_path)
                floor_plans.append(floor_plan_img)

            for pano_file in os.listdir(panos_path):
                pano_path = os.path.join(panos_path, pano_file)
                pano_img = Image.open(pano_path)
                panos.append(pano_img)

            self.data.append({
                "id": i,
                "floor_plans": floor_plans,
                "panos": panos,
                "room_layout": room_layout,
            })

    def __getitem__(self, index):
        return self.data[index]

    def __len__(self):
        return len(self.data)
    

if __name__ == "__main__":
    zind_path = "../data/zillow/zind/data"
    dataset = ZindDataset(zind_path)
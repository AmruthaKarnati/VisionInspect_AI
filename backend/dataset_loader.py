import os

DATASET_PATH = "./data/mvtec_ad"

def load_mvtec_dataset():
    """Scans the MVTec AD directory and indexes available dataset categories and image paths."""
    if not os.path.exists(DATASET_PATH):
        return {"error": f"Dataset directory '{DATASET_PATH}' not found."}

    dataset_summary = {}

    # Iterate through product category folders (e.g., bottle, grid)
    for category in os.listdir(DATASET_PATH):
        category_path = os.path.join(DATASET_PATH, category)
        
        if os.path.isdir(category_path):
            dataset_summary[category] = {"test_samples": 0, "categories": []}
            test_path = os.path.join(category_path, "test")
            
            if os.path.exists(test_path):
                # Count sample defect images within categories
                for defect_type in os.listdir(test_path):
                    defect_folder = os.path.join(test_path, defect_type)
                    if os.path.isdir(defect_folder):
                        images = [f for f in os.listdir(defect_folder) if f.endswith(('.png', '.jpg', '.bmp'))]
                        dataset_summary[category]["test_samples"] += len(images)
                        dataset_summary[category]["categories"].append(defect_type)

    return dataset_summary
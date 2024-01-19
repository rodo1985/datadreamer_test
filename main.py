import subprocess

# Parameters
save_dir = "dataset"  # Path to save the dataset
class_names = ['dog', 'cat', 'bird']  # Class names for the dataset
prompts_number = 10  # Number of prompts/images to generate

# Options
task = "detection"  # options: 'detection' or 'classification'
prompt_generator = "simple"  # options: 'simple' or 'lm' (language model)
image_generator = "sdxl-turbo"  # Image generator, e.g., 'sdxl' or 'sdxl-turbo'
image_annotator = "owlv2"  # Image annotator, e.g., 'owlv2'
conf_threshold = "0.15"  # Confidence threshold for object detection
device = "cuda"  # options: 'cuda' or 'cpu'
seed = "42"  # Random seed for image and prompt generation

# Construct the command
command = [
    "datadreamer",
    "--save_dir", save_dir,
    "--class_names", *class_names,
    "--prompts_number", str(prompts_number),
    "--task", task,
    "--prompt_generator", prompt_generator,
    "--image_generator", image_generator,
    "--image_annotator", image_annotator,
    "--conf_threshold", conf_threshold,
    "--device", device,
    "--seed", seed
]

# Execute the command
subprocess.run(command)

# PRODIGY_GA_04
# Pix2Pix cGAN: Image-to-Image Translation

This project demonstrates the pix2pix framework - a conditional generative adversarial network (cGAN) for paired image-to-image translation tasks (e.g., edges to photo, maps to satellite).

## Features

- U-Net based generator & PatchGAN discriminator.
- Modular training workflow with sample visualization.
- Easily adapt to your own paired datasets (128x128 or 256x256 recommended).

## Project Structure

- `main.py`: Entry-point script for running training and inference.
- `generator.py`: U-Net generator implementation.
- `discriminator.py`: PatchGAN discriminator implementation.
- `train.py`: Training loop, loss functions, and checkpointing.
- `utils.py`: Data loading, image visualization, and preprocessing.
- `data/`: Folder for paired images dataset.
- `requirements.txt`: All dependencies listed for pip install.

## Installation


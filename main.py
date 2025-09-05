from generator import Generator
from discriminator import Discriminator
from train import train
from utils import load_data

if __name__ == "__main__":
    train_dataset, val_dataset = load_data("data/")
    gen = Generator()
    disc = Discriminator()
    train(gen, disc, train_dataset, val_dataset)

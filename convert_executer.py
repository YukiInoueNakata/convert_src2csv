import os
from glob import glob
from tqdm import tqdm
from src import Converter, Loader, TextChecker


def make_file_path(load_path):
    save_path = load_path.replace("raw","out")
    save_path = save_path.replace("srt","csv")
    save_dir = os.path.dirname(save_path)
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    return save_path

def main():
    src_files = glob("./data/raw/*/*.srt")
    import pdb; pdb.set_trace
    for load_path in tqdm(src_files):
        l=Loader.Loader(load_path)
        converter = Converter.Converter(l)
        save_path = make_file_path(load_path=load_path)
        converter.df_for_csv.to_csv(save_path)

if __name__ == "__main__":
    main()
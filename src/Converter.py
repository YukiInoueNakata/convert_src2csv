import pandas as pd
from src import TextChecker


def preprocessing_text(text):
    text = text.replace("\n", "")
    return text


class Converter:
    def __init__(self, loader):
        self.text_lists = loader.text_lists

    @property
    def converted_dictionary(self):
        converted_dict = {
            "number": [],
            "speaker_and_caption": [],
            "start_and_end_time": [],
        }
        for text in self.text_lists():
            text = preprocessing_text(text)
            if not text:
                continue
            else:
                category = TextChecker.teach_category(text)
                converted_dict[category].append(text)
        return converted_dict

    @property
    def df_for_csv(self):
        df = pd.DataFrame(self.converted_dictionary)
        speaker_caption = df["speaker_and_caption"].str.split("]: ", expand=True)
        speaker_caption.columns = ["speaker", "caption"]
        speaker_caption["speaker"] = speaker_caption["speaker"].str.replace("[", "")

        start_end = df["start_and_end_time"].str.split(" --> ", expand=True)
        start_end.columns = ["start", "end"]

        df_for_csv = pd.concat([df["number"], start_end, speaker_caption], axis=1)
        return df_for_csv

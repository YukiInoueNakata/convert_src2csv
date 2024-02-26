class Loader:
    def __init__(self, srt_path: str):
        self.srt_path = srt_path


    def text_lists(self):
        f = open(self.srt_path, "r", encoding="UTF-8_sig")
        try:
            text_lists = f.readlines()
            return text_lists
        finally:
            f.close()


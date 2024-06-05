class Validators:

    @staticmethod
    def nota_entry(text: str or int) -> bool:
        text = text.lower()
        if text in "---" or text == "" or text in "abandonado":
            return True
        try:
            value = float(text)
        except ValueError:
            return False
        return 0 <= value <= 10

    @staticmethod
    def posse_entry(text: str) -> bool:
        text = text.lower()
        if text in "sim" or text in "não":
            return True
        return False

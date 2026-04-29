class InputHelper:

    @staticmethod
    def get_player_input(prompt, min_val, max_val):
        while True:
            try:
                value = int(input(prompt))
                if value < min_val or value > max_val:
                    print(f"Bitte Zahl zwischen {min_val} und {max_val} eingeben.")
                    continue
                return value
            except ValueError as e:
                print("Ungültige Eingabe! Bitte Zahl eingeben", e)
import random
from colorama import Fore, Style, init

init()


class Deck:
    """Class representing a deck of cards."""
    def __init__(self):
        """Initializes the deck."""
        self.cards = self.generate_deck()

    def generate_deck(self):
        """Generates a standard deck of 52 cards.

               Returns:
                   list: A list of tuples representing cards, each tuple containing a value and a suit.
               """
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        suits = ['♠', '♦', '♥', '♣']
        deck = [(value, suit) for suit in suits for value in values]
        return deck

    def shuffle(self):
        """Shuffles the deck."""
        random.shuffle(self.cards)

    def get_card(self):
        """Gets a card from the deck.

               Returns:
                   tuple or str: A tuple representing a card (value, suit), or a string 'No cards left in the deck' if the deck is empty.
               """
        if len(self.cards) > 0:
            return self.cards.pop(0)
        else:
            return "Brak kart"


class Makao:
    """Represents the Makao card game."""
    def __init__(self):
        """Initializes the game."""
        self.number_of_players = 0
        self.players = {}
        self.deck = Deck()
        self.pipe = []
        self.additional_cards = 0

    def start_game(self):
        """Starts the game."""
        self.get_number_of_players()
        self.get_players_nicknames()
        self.deck.shuffle()
        self.deal_cards(5)
        self.play_game()

    def menu(self):
        """Displays the game menu."""
        while True:
            print(f"{Fore.LIGHTMAGENTA_EX}Witaj w grze Makao!\n{Style.RESET_ALL}")
            print(f"{Fore.MAGENTA}1. {Style.RESET_ALL}Wyświetl zasady gry.")
            print(f"{Fore.MAGENTA}2. {Style.RESET_ALL}Wyświetl ranking.")
            print(f"{Fore.MAGENTA}3. {Style.RESET_ALL}Zacznij nową grę.")
            print(f"{Fore.MAGENTA}4. {Style.RESET_ALL}Wyjdź.")

            choice = input(f"\n{Fore.YELLOW}Wybierz opcję (1-4): {Style.RESET_ALL}\n")

            if choice == '1':
                self.show_rules()
                break
            elif choice == '2':
                self.display_ranking()
            elif choice == '3':
                self.start_game()
            elif choice == '4':
                print(f"{Fore.CYAN}Dziękujemy za grę! Do zobaczenia!{Style.RESET_ALL}")
                break
            else:
                print("Nieprawidłowy wybór. Spróbuj ponownie.")

    def show_rules(self):
        """Displays the game rules."""
        print(f"{Fore.LIGHTGREEN_EX}\nZasady gry Makao:{Style.RESET_ALL}")
        print(f"\n{Fore.LIGHTGREEN_EX}1.{Style.RESET_ALL} Każdy gracz otrzymuje 5 kart na początku gry.")
        print(f"\n{Fore.LIGHTGREEN_EX}2.{Style.RESET_ALL} Celem gry jest pozbycie się wszystkich swoich kart.")
        print(f"\n{Fore.LIGHTGREEN_EX}3.{Style.RESET_ALL} Gracz wybiera karte, która pasuje wartością lub kolorem do karty na wierzchu stosu.")
        print(f"\n{Fore.LIGHTGREEN_EX}4.{Style.RESET_ALL} Karty funkcyjne w makao.")
        print("\n\tW grze występują karty funkcyjne: 2, 3, 4, Król kier, Król Jopek i As. "
              "\n\n\t2, 3 – karta z figurą 2 lub 3 zobowiązuje kolejną osobę w kolejce do pobrania dwóch lub trzech kart ze stosu."
              "\n\tWyjątkiem jest sytuacja, gdy kolejny gracz ma w swojej ręce odpowiednio kartę 2 lub 3."
              "\n\n\t4 – karta z figurą 4 to tak zwana karta stopu lub inaczej – pauzy. "
              "\n\tJeśli gracz ją wyrzuci, kolejna osoba w kolejce omija kolejkę. "
              "\n\tMożna jednak dorzucić kolejną 4, wtedy pauza przechodzi na kolejnego gracza. "
              "\n\n\tKróle – karta z figurą króla może być kartą wojenną lub nie. Król kier oraz pik to karty wojenne. "
              "\n\tWyrzucenie ich na stos skutkuje tym, że kolejna osoba w kolejce musi pobrać 5 kart ze stosu. \n"
              "\n\tAs- pozwala graczowi zażądać konkretnego koloru.\n"
              "\n\tJopek(Walet)- pozwala graczowi zażądać konkretnej wartości kart prostych.")
        print(f"\n{Fore.LIGHTGREEN_EX}5.{Style.RESET_ALL} Gracz, który nie może lub nie chce wyłożyć żadnej karty, musi pobrać jedną kartę ze stosu. Jeśli ta karta pasuje, gracz może ją wyłożyć od razu.")
        print(f"\n{Fore.LIGHTGREEN_EX}6.{Style.RESET_ALL} Przy wykładaniu przedostatniej karty należy po spacji wpisac slowo 'Makao', w przeciwnym wypadku gracz będzie zmuszony dobrać 5 kart.")
        go_back = input("\nWcisnij 'q' aby wrocic do menu głownego: ")
        if go_back == "q":
            self.menu()

    def get_number_of_players(self):
        """Prompts the user to input the number of players."""
        while True:
            try:
                self.number_of_players = int(input("Podaj liczbę graczy: \n"))
                if self.number_of_players <= 0:
                    print("Podaj liczbę graczy większą od zera.")
                elif self.number_of_players > 4:
                    print("Podaj liczbę graczy nie większą niż 4")
                else:
                    break
            except ValueError:
                print("Podaj liczbę całkowitą.")

    def get_players_nicknames(self):
        """Gets nicknames for each player.

               Iterates through the range of the number of players and prompts for a nickname for each player.
               """
        for player in range(1, self.number_of_players + 1):
            nickname = input(f"Podaj nickname dla gracza {player}: \n")
            self.players[nickname] = {"cards": {}}

    def deal_cards(self, number_of_cards):
        """Deals cards to each player.

                Args:
                    number_of_cards (int): The number of cards to deal to each player.
                """
        player_nicknames = list(self.players.keys())
        for player_nickname in player_nicknames:
            player_cards = {i: self.deck.get_card() for i in range(1, number_of_cards + 1)}
            self.players[player_nickname]["cards"] = player_cards

    def pick_cards(self, player, number):
        """Allows a player to pick additional cards.

                Args:
                    player (str): The nickname of the player picking cards.
                    number (int): The number of additional cards to pick.
                """
        decision = input("Wpisz 'w', aby wyświetlić dobrane karty lub enter, aby kontynuować: ")

        if decision == 'w':
            print("Dobrane karty: ")

        for _ in range(number):
            new_card = self.deck.get_card()
            new_card_key = max(self.players[player]["cards"].keys(), default=0) + 1

            if decision == 'w':
                new_card_value, new_card_suit = new_card
                if new_card_suit in ('♠', '♣'):
                    print(
                        f"{new_card_key}. {new_card_value} {Fore.WHITE}{Style.BRIGHT}{new_card_suit}{Style.RESET_ALL}")
                else:
                    print(f"{new_card_key}. {new_card_value} {Fore.RED}{Style.BRIGHT}{new_card_suit}{Style.RESET_ALL}")

            self.players[player]["cards"][new_card_key] = new_card
        self.additional_cards = 0

    def show_first_card(self):
        """Displays the first card on the stack."""
        top_card_value, top_card_suit = self.pipe[-1]

        if top_card_suit in ('♠', '♣'):
            print(
                f"\nPierwsza karta na stosie:\n{top_card_value} {Fore.WHITE}{Style.BRIGHT}{top_card_suit}{Style.RESET_ALL}")
        else:
            print(
                f"\nPierwsza karta na stosie:\n{top_card_value} {Fore.RED}{Style.BRIGHT}{top_card_suit}{Style.RESET_ALL}")

    def skip_players_turn(self, current_player, top_card_value):
        """Skips the turn of a player if they have a defensive card.

                Args:
                    current_player (str): The nickname of the current player.
                    top_card_value (str): The value of the top card on the stack.

                Returns:
                    bool: True if the player's turn is skipped, False otherwise.
                """
        has_defensive_card = any(value == top_card_value for value, suit in self.players[current_player]["cards"].values())
        if has_defensive_card:
            print(f"\nGracz {current_player}, {Fore.RED}Pauza na kolejkę lub możesz odbić odpowiednią kartą.{Style.RESET_ALL}")
            self.take_turn(current_player)
        else:
            print(f"\nGracz {current_player}, {Fore.RED}Pauza na kolejkę.{Style.RESET_ALL}")
            return True
        return False

    def show_players_cards(self, current_player):
        """Displays the cards of a player.

                Args:
                    current_player (str): The nickname of the player whose cards are to be displayed.
                """

        print(f"\nGracz {Fore.CYAN}{current_player}{Style.RESET_ALL}, twoje karty: ")

        for number, card in self.players[current_player]["cards"].items():
            card_value, card_suit = card
            if card_suit in ('♠', '♣'):
                print(f"{number}. {card_value} {Fore.WHITE}{Style.BRIGHT}{card_suit}{Style.RESET_ALL}")
            else:
                print(f"{number}. {card_value} {Fore.RED}{Style.BRIGHT}{card_suit}{Style.RESET_ALL}")

    def check_makao(self, current_player, makao):
        """Checks if the player needs to say 'Makao'.

                Args:
                    current_player (str): The nickname of the current player.
                    makao (bool): Flag indicating if 'Makao' has been said.
                """
        if len(self.players[current_player]["cards"]) == 1:
            if not makao:
                print(f"\n{Fore.RED}Nie powiedziałeś 'makao'! Musisz dobrać 5 dodatkowych kart.{Style.RESET_ALL}")
                self.pick_cards(current_player, 5)
            else:
                print(f"Gracz {current_player}, MAKAO!")

    def validate_card(self, top_card_value, top_card_suit, chosen_card_value, chosen_card_suit):
        """Validates if the chosen card can be played.

                Args:
                    top_card_value (str): The value of the top card on the stack.
                    top_card_suit (str): The suit of the top card on the stack.
                    chosen_card_value (str): The value of the chosen card.
                    chosen_card_suit (str): The suit of the chosen card.

                Returns:
                    bool: True if the chosen card can be played, False otherwise.
                """
        if chosen_card_value == 'Q' or top_card_value == 'Q':
            return True
        elif top_card_suit == chosen_card_suit:
            return True
        elif top_card_value == chosen_card_value:
            return True
        else:
            return False

    def take_turn(self, current_player):
        """Allows the current player to take their turn.

               Args:
                   current_player (str): The nickname of the current player.

               Returns:
                   tuple: A tuple containing the chosen card value, a boolean indicating if 'Makao' was said, and the suit of the chosen card.
               """
        makao = False

        while True:
            chosen_card_number = input(f"\n{Fore.YELLOW}Wybierz numer żądanej karty lub wpisz 'q' by dobrać nową:{Style.RESET_ALL}\n")
            if chosen_card_number == 'q':
                new_card = self.deck.get_card()
                new_card_key = max(self.players[current_player]["cards"].keys(), default=0) + 1
                self.players[current_player]["cards"][new_card_key] = new_card
                return None, False, None
            else:
                if 'makao' in chosen_card_number.lower():
                    chosen_card_parts = chosen_card_number.split()
                    chosen_card_number = int(chosen_card_parts[0])
                    makao = True
                chosen_card = self.players[current_player]["cards"].get(int(chosen_card_number))

            if not chosen_card:
                print("Nieprawidłowy wybór. Spróbuj ponownie.")
                continue

            chosen_card_value, chosen_card_suit = chosen_card

            if self.validate_card(self.pipe[-1][0], self.pipe[-1][1], chosen_card_value, chosen_card_suit):
                self.players[current_player]["cards"].pop(int(chosen_card_number))
                self.pipe.append((chosen_card_value, chosen_card_suit))

                return chosen_card_value, makao, chosen_card_suit

            else:
                print("Wybrana karta nie pasuje do karty na stosie. Spróbuj ponownie.")

    def process_special_card(self, additional_cards, chosen_card_value, chosen_card_suit):
        """Processes the effects of special cards.

                Args:
                    additional_cards (int): The number of additional cards to be drawn.
                    chosen_card_value (str): The value of the chosen card.
                    chosen_card_suit (str): The suit of the chosen card.

                Returns:
                    tuple: A tuple containing the updated number of additional cards and a boolean indicating
                    if the turn should be skipped.
                """
        skip_turn = False
        match chosen_card_value:
            case '2':
                additional_cards += 2
            case '3':
                additional_cards += 3
            case 'K':
                if chosen_card_suit in ('♠', '♥'):
                    additional_cards += 5
            case '4':
                skip_turn = True

        return additional_cards, skip_turn

    def save_ranking(self, ranking):
        """Saves the ranking of players to a file.

              Args:
                  ranking (list): A list of player nicknames representing the ranking.
              """
        with open("ranking.txt", "a") as file:
            round_number = sum(1 for line in open("ranking.txt")) // (self.number_of_players + 1) + 1
            file.write(f"Runda {round_number}:\n")
            for position, player in enumerate(ranking, 1):
                file.write(f"{position}. {player}\n")
            file.write("\n")

    def display_ranking(self):
        """Displays the ranking of players from a file."""
        try:
            with open("ranking.txt", "r") as file:
                print(file.read())
        except FileNotFoundError:
            print("Brak zapisanych rankingów.")

    def has_additional(self, top_card_value, current_player, additional_cards):
        """Checks if additional cards need to be drawn.

                Args:
                    top_card_value (str): The value of the top card on the stack.
                    current_player (str): The nickname of the current player.
                    additional_cards (int): The number of additional cards to be drawn.

                Returns:
                    int: The updated number of additional cards to be drawn.
                """
        has_defensive_card = any(value == top_card_value for value, suit in self.players[current_player]["cards"].values())
        has_king_of_hearts_or_spades = any(card[0] == 'K' and card[1] in ('♠', '♥') for card in self.players[current_player]["cards"].values())

        if (has_defensive_card and (has_king_of_hearts_or_spades and top_card_value == 'K')) or (has_defensive_card and not top_card_value == 'K'):
            if additional_cards in (2, 3, 4):
                print(
                    f"\nGraczu {Fore.CYAN}{current_player}{Style.RESET_ALL}, {Fore.RED}Musisz dobrać {additional_cards} karty lub możesz odbić odpowiednią kartą.{Style.RESET_ALL}")
            else:
                print(
                    f"\nGraczu {Fore.CYAN}{current_player}{Style.RESET_ALL}, {Fore.RED}Musisz dobrać {additional_cards} kart lub możesz odbić odpowiednią kartą.{Style.RESET_ALL}")
            return additional_cards
        else:
            if additional_cards in (2, 3, 4):
                print(
                    f"\nGraczu {Fore.CYAN}{current_player}{Style.RESET_ALL}, {Fore.RED}Musisz dobrać {additional_cards} karty.{Style.RESET_ALL}")
            else:
                print(
                    f"\nGraczu {Fore.CYAN}{current_player}{Style.RESET_ALL}, {Fore.RED}Musisz dobrać {additional_cards} kart.{Style.RESET_ALL}")
            self.pick_cards(current_player, additional_cards)
            additional_cards = 0
            return additional_cards

    def change_value(self, player):
        """Changes the value of the top card on the stack.

               Args:
                   player (str): The nickname of the player who is changing the value.
               """
        while True:
            new_value = input(f"\nGracz {player}, wybierz nową wartość karty (5-10): ").upper()
            if new_value in ['5', '6', '7', '8', '9', '10']:
                self.pipe[-1] = (new_value, self.pipe[-1][1])
                print(f"\nGracz {player} zmienił wartość na {new_value}.")
                break
            else:
                print("Nieprawidłowa wartość. Spróbuj ponownie.")

    def change_suit(self, player):
        """Changes the suit of the top card on the stack.

                Args:
                    player (str): The nickname of the player who is changing the suit.
                """
        while True:
            new_suit = input(f"\nGracz {player}, wybierz nowy kolor karty (♠, ♦, ♥, ♣): ")
            if new_suit in ['♠', '♦', '♥', '♣']:
                self.pipe[-1] = (self.pipe[-1][0], new_suit)
                print(f"\nGracz {player} zmienił kolor na {new_suit}.")
                break
            else:
                print("Nieprawidłowy kolor. Spróbuj ponownie.")

    def play_game(self):
        """Starts the game and manages player turns until the game is over."""
        players_list = list(self.players.keys())
        finished_players = set()
        current_index = 0
        self.pipe.append(self.deck.get_card())
        additional_cards = 0
        skip_turn = False

        while len(finished_players) < self.number_of_players:
            current_player = players_list[current_index]

            if current_player in finished_players:
                current_index = (current_index + 1) % len(players_list)
                continue

            top_card_value, top_card_suit = self.pipe[-1]
            self.show_first_card()
            self.show_players_cards(current_player)

            if additional_cards > 0:
                additional_cards = self.has_additional(top_card_value, current_player, additional_cards)

            if skip_turn:
                skipped = self.skip_players_turn(current_player, top_card_value)
                skip_turn = False
                if skipped:
                    current_index = (current_index + 1) % len(players_list)
                continue

            makao = False

            while True:
                chosen_card_number = input(f"\n{Fore.YELLOW}Wybierz numer żądanej karty lub wpisz 'q' by dobrać nową:{Style.RESET_ALL}\n")
                if chosen_card_number == 'q':
                    new_card = self.deck.get_card()
                    new_card_key = max(self.players[current_player]["cards"].keys(), default=0) + 1
                    self.players[current_player]["cards"][new_card_key] = new_card
                    break
                else:
                    if 'makao' in chosen_card_number.lower():
                        chosen_card_parts = chosen_card_number.split()
                        chosen_card_number = int(chosen_card_parts[0])
                        makao = True
                    chosen_card = self.players[current_player]["cards"].get(int(chosen_card_number))

                if not chosen_card:
                    print("Nieprawidłowy wybór. Spróbuj ponownie.")
                    continue

                chosen_card_value, chosen_card_suit = chosen_card

                if self.validate_card(top_card_value, top_card_suit, chosen_card_value, chosen_card_suit):
                    self.players[current_player]["cards"].pop(int(chosen_card_number))
                    self.pipe.append((chosen_card_value, chosen_card_suit))
                    additional_cards, skip_turn = self.process_special_card(additional_cards, chosen_card_value, chosen_card_suit)

                    if chosen_card_value == 'A':
                        self.change_suit(current_player)
                    if chosen_card_value == 'J':
                        self.change_value(current_player)
                    self.check_makao(current_player, makao)
                    makao = False
                    if len(self.players[current_player]["cards"]) == 0:
                        print(f"Po makale!!! Gracz {current_player} wygrał.")
                        finished_players.add(current_player)
                        if len(finished_players) == self.number_of_players - 1:
                            self.save_ranking(players_list)
                            print("Gra zakończona. Wszyscy gracze skończyli.")
                            return
                    break
                else:
                    print("Wybrana karta nie pasuje do karty na stosie. Spróbuj ponownie.")
                    makao = False

            current_index = (current_index + 1) % len(players_list)


makao_game = Makao()
makao_game.menu()


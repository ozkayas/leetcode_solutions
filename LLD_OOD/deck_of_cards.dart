enum Suit { club, diamond, heart, spade }

abstract class Card {
  Card({required this.faceValue, required this.suit});

  bool _isAvailable = true;
  final int faceValue;
  final Suit suit;

  bool get isAvailable => _isAvailable;
  void setAvailable() => _isAvailable = true;
  void setUnavailable() => _isAvailable = false;
}

class Deck<T extends Card> {
  List<T> cards = [];
  void setCards(List<T> cardsToAdd) {
    cards.addAll(cardsToAdd);
  }

  int dealtIndex = 0;

  int remainingDeckSize() {
    throw ("Unimplemented");
  }

  void shuffle() {
    throw ("Unimplemented");
  }

  List<T> dealHand(int number) {
    throw ("Unimplemented");
  }

  T dealCard() {
    throw ("Unimplemented");
  }
}

class Hand<T extends Card> {
    List<T> cards = [];
    
}

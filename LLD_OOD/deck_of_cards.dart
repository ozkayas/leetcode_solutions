
enum Suit { club, diamond, heart, spade }

abstract class Card {
  Card({required this.faceValue, required this.suit});

  bool _isAvailable = true;
  final int faceValue;
  final Suit suit;

  bool get isAvailable => _isAvailable;
  void setAvailable() => _isAvailable = true;
  void setUnavailable() => _isAvailable = false;

  int value();
}

class Deck<T extends Card> {
  List<T> cards = [];
  void setCards(List<T> cardsToAdd) {
    cards.addAll(cardsToAdd);
  }

    int get size => cards.length;

  int remainingDeckSize() {
    return size;
  }

  void shuffle() {
    cards.shuffle();
  }

  List<T> dealHand(int number) {

    List<T> toDealt = [];
    for(int i = 0; i < number; i++){
        toDealt.add(cards.removeLast());
    }
    return toDealt;
  }

  T dealCard() {
    return cards.removeLast();
  }
}

class Hand<T extends Card> {
    List<T> cards = [];

    int value(){
        int val = 0;
        for(T card in cards ){
            val += card.value();
        }
        return val;
    }

    void addCard(T card) => cards.add(card);

}

//// BlackJack Implementation
////

class BlackJackCard extends Card{
    BlackJackCard({required super.faceValue, required super.suit});

    bool get _isAce => faceValue == 1;

    int value(){
        int val = 0;

        if(_isAce){
            val = 1;
        } else if(faceValue >= 11 && faceValue <= 13){
            val = 10;
        } else {
            val = faceValue;
        }
        return val;
    }

    int minValue(){
        return _isAce ? 1 : value();
    }

        int maxValue(){
        return _isAce ? 11 : value();
    }

    bool get isFaceCard => (faceValue >= 11 && faceValue <= 13);
}

class BlackJackHand extends Hand<BlackJackCard>{
    int score(){
        throw UnimplementedError();
    }
}
% Facts
fruit(apple, red).
fruit(banana, yellow).
fruit(grape, purple).
fruit(orange, orange).
fruit(lemon, yellow).
fruit(strawberry, red).
fruit(blueberry, blue).
fruit(kiwi, green).

% Rule to find all fruits of a given color
fruit_of_color(Color, Fruit) :-
    fruit(Fruit, Color).

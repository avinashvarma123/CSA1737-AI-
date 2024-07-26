% Define the heuristic function for nodes
heuristic(a, 10).
heuristic(b, 5).
heuristic(c, 2).
heuristic(d, 1).
heuristic(e, 0).

% Define the graph with neighbors
edge(a, b).
edge(a, c).
edge(b, d).
edge(c, d).
edge(d, e).

% Best First Search algorithm
best_first_search(Start, Goal, Path) :-
    best_first_search_helper([Start], Goal, Path).

best_first_search_helper([Goal|Rest], Goal, [Goal|Rest]).
best_first_search_helper(OpenList, Goal, Path) :-
    OpenList = [Current|_],
    findall(Next, (edge(Current, Next), \+ member(Next, OpenList)), Neighbors),
    sort_by_heuristic(Neighbors, SortedNeighbors),
    append(SortedNeighbors, Rest, NewOpenList),
    best_first_search_helper(NewOpenList, Goal, Path).

% Sort neighbors by heuristic value (ascending)
sort_by_heuristic(Neighbors, Sorted) :-
    findall(Node-Heuristic, (member(Node, Neighbors), heuristic(Node, Heuristic)), Pairs),
    sort(2, @=<, Pairs, SortedPairs),
    pairs_keys(SortedPairs, Sorted).

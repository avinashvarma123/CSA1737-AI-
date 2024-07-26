% Facts
fact(has_sore_throat).
fact(has_cough).
fact(has_fever).

% Rules
rule(flu, [has_fever, has_cough, has_sore_throat]).
rule(cold, [has_cough]).
rule(allergy, [has_sneezing, has_itchy_eyes]).

% Backward chaining to determine if a goal can be satisfied
prove(Goal) :-
    fact(Goal).
prove(Goal) :-
    rule(Goal, Conditions),
    satisfy_conditions(Conditions).

satisfy_conditions([]).
satisfy_conditions([Condition|Rest]) :-
    prove(Condition),
    satisfy_conditions(Rest).


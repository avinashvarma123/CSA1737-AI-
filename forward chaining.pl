% Facts
fact(has_sore_throat).
fact(has_cough).
fact(has_fever).

% Rules
rule(flu, [has_fever, has_cough, has_sore_throat]).
rule(cold, [has_cough]).
rule(allergy, [has_sneezing, has_itchy_eyes]).

% Forward chaining to derive new facts
infer(Fact) :-
    rule(Disease, Conditions),
    all_conditions_met(Conditions),
    assertz(fact(Disease)).

all_conditions_met([]).
all_conditions_met([Condition|Rest]) :-
    fact(Condition),
    all_conditions_met(Rest).

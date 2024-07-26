% Facts: Define the symptoms associated with various diseases
symptom(flu, fever).
symptom(flu, cough).
symptom(flu, sore_throat).
symptom(cold, cough).
symptom(cold, runny_nose).
symptom(cold, sneezing).
symptom(allergy, itchy_eyes).
symptom(allergy, sneezing).
symptom(allergy, runny_nose).
symptom(covid, fever).
symptom(covid, cough).
symptom(covid, loss_of_taste).

% Rules: Infer the possible disease based on observed symptoms
diagnose(Disease, Symptoms) :-
    findall(S, (member(S, Symptoms), symptom(Disease, S)), MatchingSymptoms),
    length(MatchingSymptoms, NumMatching),
    NumMatching > 1.

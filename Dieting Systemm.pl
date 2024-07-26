% Facts
disease_diet(diabetes, diet(low_carb, high_fiber, low_sugar)).
disease_diet(hypertension, diet(low_sodium, high_potassium, low_fat)).
disease_diet(heart_disease, diet(low_fat, high_fiber, omega_3)).
disease_diet(anemia, diet(high_iron, vitamin_c, folic_acid)).
disease_diet(obesity, diet(low_calorie, high_protein, high_fiber)).
disease_diet(gastritis, diet(low_acid, low_spice, soft_foods)).

% Rules
diet_recommendation(Disease, Diet) :-
    disease_diet(Disease, Diet).


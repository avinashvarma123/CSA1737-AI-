
person('Alice', '1990-01-15').
person('Bob', '1985-07-23').
person('Carol', '1992-12-10').
person('Dave', '1988-03-05').
find_person_by_name(Name, DOB) :-
    person(Name, DOB).
find_person_by_year(Year, Name, DOB) :-
    person(Name, DOB),
    sub_atom(DOB, 0, 4, _, Year).

# Base costs definitions
fx = 55.0

# Variable costs per person (EUR)
accommodation_eur = 95.0
meeting_room_eur = 10.0
coffee_break_eur = 20.0
two_lunches_eur = 25.0
gala_dinner_eur = 2000.0 / fx
topkapi_eur = 2750.0 / fx
museum_eur = 550.0 / fx
public_transport_eur = 1000.0 / fx
certificate_eur = 100.0 / fx
porcelain_eur = 100.0 / fx

# The user states that airport transportation is per person and 2000 x 2 = 4000 TL per person
airport_transport_eur = (2000.0 * 2) / fx

# Base variable cost per person (excluding instructors if they are not included or if included we need to make sure we treat it correctly)
# Let's check user's previous correction: "hava limanı ulaşımı adam başı maliyet olacak ve 10 12 15 k"
# Wait, "10 12 15 k" means 10, 12, 15 participants (katılımcı).
# Let's sum up the variable cost per participant:
variable_cost_per_person = (
    accommodation_eur + meeting_room_eur + coffee_break_eur + two_lunches_eur +
    gala_dinner_eur + topkapi_eur + museum_eur + public_transport_eur +
    certificate_eur + porcelain_eur + airport_transport_eur
)

# Fixed costs (EUR)
muhterem_eur = 1300.0
zeynep_eur = 800.0
eduardo_fee_eur = 1300.0
eduardo_flight_eur = 450.0
vapur_total_eur = 1500.0 / fx
workshop_materials_eur = 300.0

fixed_costs_total = (
    muhterem_eur + zeynep_eur + eduardo_fee_eur + eduardo_flight_eur +
    vapur_total_eur + workshop_materials_eur
)

# Let's check whether instructor variable cost needs to be added as fixed. 
# The user's prompt originally didn't ask for instructors' variable costs, but in turn 2 I added it and they didn't object, they just corrected that airport transport is per person.
# Wait, let's provide the calculation where it's strictly per participant for variable costs, and keeping the fixed costs clean, but mentioning if 3 instructors are included in fixed. 
# Let's calculate BOTH to be absolutely precise or just apply it per person for the 10, 12, 15 participants.
# Let's calculate standard participant variable costs first.

print(f"Fixed: {fixed_costs_total}")
print(f"Variable per person: {variable_cost_per_person}")

# For 10, 12, 15 participants:
for p in [10, 12, 15]:
    total_var = variable_cost_per_person * p
    total_cost = fixed_costs_total + total_var
    per_person_cost = total_cost / p
    print(f"P={p}: Total Var={total_var:.2f}, Total Cost={total_cost:.2f}, Per Person={per_person_cost:.2f}")

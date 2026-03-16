from circle_stats import has_intersection
from circles_intersection_draw import draw_data

# Definice kružnic
c1 = {"x": 0, "y": 0, "r": 5}
c2 = {"x": 7, "y": 0, "r": 3}

# Výpočet průniku
result = has_intersection(c1, c2)

# Výpis výsledků
if result["is_intersection"]:
    count = result["intersections_count"]
    print(f"Kružnice se protínají. Počet průsečíků: {count}")
else:
    print("Kružnice se neprotínají.")

# Bonus: Vykreslení
draw_data(c1, c2)
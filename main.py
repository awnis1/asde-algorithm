def can_abhinayu_cross(p, enemies, skips, recharges):
    n = len(enemies)
    skips_used = 0
    recharges_used = 0
    regenerated_3 = False
    regenerated_7 = False
    
    for i in range(n):
        enemy_power = enemies[i]
        
        if p < enemy_power:
            if skips_used < skips:
                skips_used += 1
                continue
            elif recharges_used < recharges:
                recharges_used += 1
                p = max(p, enemy_power)
            else:
                return False
        
        p -= enemy_power
        
        if i == 2 and not regenerated_3:  # k3 regenerates
            p -= enemy_power // 2
            regenerated_3 = True
        elif i == 6 and not regenerated_7:  # k7 regenerates
            p -= enemy_power // 2
            regenerated_7 = True
        
        if p < 0:
            return False
    
    return True

# Test Cases
p1 = 100
enemies1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110]
skips1 = 3
recharges1 = 2

p2 = 50
enemies2 = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55]
skips2 = 2
recharges2 = 1

print(can_abhinayu_cross(p1, enemies1, skips1, recharges1))  # Expected output: True or False
print(can_abhinayu_cross(p2, enemies2, skips2, recharges2))  # Expected output: True or False

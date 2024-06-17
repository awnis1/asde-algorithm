# asde-algorithm



Algorithm:
1. Initialization:
  Input the initial power of Abhimanyu (p).
  Input the power of enemies in each circle (k1, k2, ..., k11).
  Input the number of skips (a).
  Input the number of recharges (b).
  
2. Iterate Through Each Circle:
  Initialize Abhimanyu's current power to p.
  Initialize counters for skips used and recharges used.
  Keep track of whether enemies in circle 3 and 7 have regenerated.

3. Battle Logic:
   For each circle i from 1 to 11:
    If skips are available and Abhimanyu's power is less than the enemy power, use a skip.
    If Abhimanyu's power is less than the enemy power and skips are not available, use a recharge if available.
    If Abhimanyu's power is less than the enemy power and no skips or recharges are available, Abhimanyu loses.
    If Abhimanyu's power is greater than or equal to the enemy power, proceed to battle:
      Reduce Abhimanyu's power by the enemy's power.
      Check if enemies in circle 3 or 7 have regenerated:
        If yes, reduce Abhimanyu's power by half the enemy's initial power again.
        Mark the enemy as no longer able to regenerate.
   
4. Check Completion:
  If Abhimanyu successfully battles through all circles, return success.
  If at any point Abhimanyu's power drops below the required level and no skips or recharges are available, return failure.


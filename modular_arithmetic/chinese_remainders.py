import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from lib.lib import chinese_remainders
### IF YOU KNOW xi modulo ni (ni are pairwise coprime) then you
### compute xi modulo N (where N=product(ni))

remainders  = [2,3,5]
moduli = [5,11,17]

print(chinese_remainders(remainders, moduli))
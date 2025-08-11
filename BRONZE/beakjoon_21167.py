import sys
import math

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    parts = line.split()
    R = float(parts[0])
    S = float(parts[1])
    V = math.sqrt((R * (S + 0.16)) / 0.067)
    # 양수이므로 int(V + 0.5)로 안전하게 반올림
    print(int(V + 0.5))
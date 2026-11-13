"""
def solution(a):
    # 1. Φιλτράρισμα: Κρατάμε μόνο τους θετικούς αριθμούς ( > 0 ) εξ αρχής
    a = [x for x in a if x > 0]
    
    # Αν η λίστα έμεινε άδεια (όλοι ήταν αρνητικοί ή μηδέν), το 1 λείπει σίγουρα
    if not a:
        return 1

    # 2. Ταξινόμηση (Bubble Sort με τη βελτιστοποίησή σου)
    for i in range(0, len(a) - 1): 
        for j in range(0, len(a) - 1 - i):
            if a[j] > a[j+1]:
                temp = a[j]
                a[j] = a[j+1]
                a[j+1] = temp
                
    print("Καθαρή & Ταξινομημένη λίστα:", a)

    # 3. Έλεγχος αν λείπει το 1 από την αρχή
    if a[0] != 1:
        return 1

    # 4. Έλεγχος για κενά ανάμεσα στα στοιχεία
    for i in range(0, len(a) - 1):
        if (a[i+1] - a[i] > 1):
            return a[i] + 1
            
    # 5. Αν όλα είναι συνεχόμενα, ο επόμενος είναι ο max + 1
    return a[-1] + 1

A = [-1, -3]
result = solution(A)
print("Αποτέλεσμα:", result)
"""

A = [1,2,3,3,3,4,6,4,5,6,7]

def solution2(a : list) -> int :
    a2 = set(i for i in a if i > 0)
    for i in range(1,len(a2) + 1):
        if (i) not in a2:
            return i, a2
    return len(a2) + 1, a2
        
res, a2 = solution2(A)
print(f"array is {a2} and smallest positive integer is {res} ")
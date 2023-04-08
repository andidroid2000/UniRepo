# Structuri_de_date
## Tema 1: algoritmi de sortare

Pentru tema numarul 1 de la laboratorul de SD, am implementat in Python urmatorii algoritmi de sortare:
1. Bubble_sort
2. Count_sort
3. Merge_sort
4. Quick_sort
5. Radix_sort

Link prezentare [PowerPoint](https://unibucro0-my.sharepoint.com/:p:/r/personal/andi_toader_s_unibuc_ro/Documents/SDA%20-%20Tema%201.pptx?d=wdda6482b3f064bd4a2ab6252d4ac38f7&csf=1&web=1&e=CuLbjA).

Pentru a determina eficienta acestora, am realizat un numar de 8 teste, cu numere generate aleator, avand urmatoarele caracteristici privind vectorii: [[Numar_elemente, Valoare maxima]], unde teste = teste = [[1000, 1000], [1000, 100000], [10000, 10000], [10000, 100000], [100000, 10000], [1000000, 100000], [10000000, 10000], [100000000, 30000]]. Pentru comparatie, am rulat si sort-ul nativ. Un ultim test a fost efectuat pe un input deja sortat. In urma acestor teste, am inregistrat urmatoarele date (acestea au fost validate la final):

TEST  1 [1000, 1000]
- Test 1 : BUBBLE SORT efectuat in 60 de milisecunde

- Test 1 : COUNT SORT efectuat in 1 de milisecunde

- Test 1 : MERGE SORT efectuat in 10 de milisecunde

- Test 1 : QUICK SORT efectuat in 2 de milisecunde

- Test 1 : RADIX SORT efectuat in 130 de milisecunde

- Test 1 : SORT NATIV efectuat in 0.1 de milisecunde

TEST 2 [1000, 100000]

- Test 2 : BUBBLE SORT efectuat in 59 de milisecunde

- Test 2 : COUNT SORT efectuat in 16 de milisecunde

- Test 2 : MERGE SORT efectuat in 10 de milisecunde

- Test 2 : QUICK SORT efectuat in 2 de milisecunde

- Test 2 : RADIX SORT efectuat in 127 de milisecunde

- Test 2 : SORT NATIV efectuat in 0.5 de milisecunde

TEST 3 [10000, 10000]

- Test 3 : BUBBLE SORT efectuat in 6740 de milisecunde

- Test 3 : COUNT SORT efectuat in 3 de milisecunde

- Test 3 : MERGE SORT efectuat in 1005 de milisecunde

- Test 3 : QUICK SORT efectuat in 25 de milisecunde

- Test 3 : RADIX SORT efectuat in 1380 de milisecunde

- Test 3 : SORT NATIV efectuat in 1 de milisecunde

TEST 4 [10000, 100000]

- Test 4 : BUBBLE SORT efectuat in 6782 de milisecunde

- Test 4 : COUNT SORT efectuat in 17 de milisecunde

- Test 4 : MERGE SORT efectuat in 903 de milisecunde

- Test 4 : QUICK SORT efectuat in 19 de milisecunde

- Test 4 : RADIX SORT efectuat in 1357 de milisecunde

- Test 4 : SORT NATIV efectuat in 1 de milisecunde

TEST  5 [100000, 10000]

- Test 5 : BUBBLE SORT efectuat in 609585 de milisecunde

- Test 5 : COUNT SORT efectuat in 17 de milisecunde

- Test 5 : MERGE SORT efectuat in 103128 de milisecunde

- Test 5 : QUICK SORT efectuat in 310 de milisecunde

- Test 5 : RADIX SORT efectuat in 13537 de milisecunde

- Test 5 : SORT NATIV efectuat in 15 de milisecunde

TEST  6 [1000000, 100000]

- Test 6 : BUBBLE SORT nu a putut efectua sortarea intr-un timp rezonabil!

- Test 6 : COUNT SORT efectuat in 183 de milisecunde

- Test 6 : MERGE SORT nu a putut efectua sortarea intr-un timp rezonabil!

- Test 6 : QUICK SORT efectuat in 3500 de milisecunde

- Test 6 : RADIX SORT efectuat in 185938 de milisecunde

- Test 6 : SORT NATIV efectuat in 218 de milisecunde

TEST  7 [10000000, 10000]

- Test 7 : BUBBLE SORT nu a putut efectua sortarea intr-un timp rezonabil!

- Test 7 : COUNT SORT efectuat in 1623 de milisecunde

- Test 7 : MERGE SORT nu a putut efectua sortarea intr-un timp rezonabil!

- Test 7 : QUICK SORT efectuat in 224016 de milisecunde

- Test 7 : RADIX SORT nu a putut efectua sortarea intr-un timp rezonabil!

- Test 7 : SORT NATIV efectuat in 2386 de milisecunde

TEST  8 [100000000, 30000]

- Test 8 : BUBBLE SORT nu a putut efectua sortarea intr-un timp rezonabil!

- Test 8 : COUNT SORT efectuat in 18434 de milisecunde

- Test 8 : MERGE SORT nu a putut efectua sortarea intr-un timp rezonabil!

- Test 8 : QUICK SORT nu a putut efectua sortarea intr-un timp rezonabil!

- Test 8 : RADIX SORT nu a putut efectua sortarea intr-un timp rezonabil!

- Test 8 : SORT NATIV efectuat in 24573 de milisecunde

SORTAT

- Sortat : BUBBLE SORT efectuat in 1 de milisecunde

- Sortat : COUNT SORT efectuat in 8 de milisecunde

- Sortat : MERGE SORT efectuat in 1004 de milisecunde

- Sortat : QUICK SORT efectuat in 17 de milisecunde

- Sortat : RADIX SORT efectuat in 1244 de milisecunde

- Sortat : SORT NATIV efectuat in 0.1 de milisecunde

# Gaussian-elimination
Gaussian elimination with pivoting strategy + some tests with results writing to .csv file 

## Polish Description
Częściowy opis w języku angielskim zawarty jest w komentarzu w pliku gaussian_elimination.py 
(A partial description in English is included in the comment in the file gaussian_elimination.py)

### Opis plików
- Plik gaussian_elimination.py zawiera jedną z metod rozwiązywania układów równań liniowych - metodę eliminacji Gaussa. Szczegółowy opis tej metody, wraz z wykorzystaniem wyboru elementu podstawowego (pivot), znajduje się pod linkiem: https://rperlinski.pl/strona/files/mn/d03_UkladyRownanLiniowychI.pdf w rozdziale 4.3,
- Plik gaussian_elimination_tests.py zawiera 4 testy jednostkowe jednej instancji wraz z funkcją zapisującą wyniki uzyskane powyższą metodą (funkcja: write_to_file) do pliku .csv. 
### Uzyskane wyniki

Wyniki uzyskane z wykorzystaniem powyższej metody nie są w każdym przypadku rozwiązaniami idealnymi. Nawet wybór elementu podstawowego, zarówno pod kątem minimalizacji zjawiska występowania zer na diagonali oraz mniejszych liczb niż poza nią, nie rozwiązuje w pełni problemu. W przypadku wyników, nie będących rozwiązaniami idealnymi, rozwiązania te, są często badzo bliskie tym prawdziwym (ich błąd bezwzględny jest niewielki). Problemem tej metody numerycznej, rozwiązywania układów równań liniowych, może być: wspomniany wyżej problem wyboru elementu podstawowego, skończona dokładność obliczeń wykonywanych przez komputer oraz zapisu liczb czy złe uwarunkowanie macierzy.





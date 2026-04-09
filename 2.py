#Dmytro Stefko WCY23KY3S1
#Protokol rzutu moneta przy zastosowaniu potegowania modulo p

#kody zaimplementowanych funkcji:
#krok 1:uzgodnienie p
def uzg_p(b=60):
    while True:
        k = randrange(2^(b-1), 2^b)
        p = next_prime(k)
        if p.nbits() == b:
            r = factor(p - 1)
            return p, r

#krok 2: B wybiera h i t
def wyb_gen(p):
    F = GF(p)
    h = F.multiplicative_generator()
    while True:
        t = F.random_element()
        if t != h and t.multiplicative_order() == p - 1:
            return F, h, t

#krok 3: A losuje x i wysyla y
def wyslij(F, h, t, p):
    while True:
        x = randint(2, p - 2)
        if gcd(x, p - 1) == 1:
            break
    w = choice(['h', 't'])  # wybor A: h lub t
    y = power_mod(h, x, p) if w == 'h' else power_mod(t, x, p)
    return x, w, y

#krok 4: B zgaduje h lub t
def zgadnij():
    return choice(['h', 't'])

#krok 5: wynik rzutu
def wynik(w_A, w_B):
    return w_A == w_B

#krok 6: B sprawdza
def sprawdz(x, y, h, t, p):
    if power_mod(h, x, p) == y:
        return 'h'
    elif power_mod(t, x, p) == y:
        return 't'
    else:
        return 'ERR'

#sekwencje wywolan funkcji realizujacych kroki protokolu:

#uzgadnianie p
p, r = uzg_p()
print("p =", p)
print("rozklad p-1 =", r)

#generatory od B
F, h, t = wyb_gen(p)
print("h =", h)
print("t =", t)

#A losuje x i wysyla y
x, w_A, y = wyslij(F, h, t, p)
print("A wysyla y =", y)

#B zgaduje
w_B = zgadnij()
print("B zgaduje:", w_B)

#wynik
ok = wynik(w_A, w_B)
res = "Reszka – B zgadl" if ok else "Orzel – B nie zgadl"
print("Wynik rzutu:", res)

#A ujawnia x
print("A ujawnia x =", x)

#B weryfikuje
act = sprawdz(x, y, h, t, p)
if act == 'ERR':
    print("B: blad, y nie pasuje")
else:
    final = "Reszka" if act == w_B else "Orzel"
    print("B: to bylo", act, "->", final)

#_______________________________________________________________________________________________________
#Output:
#p = 1055544902999821271
#rozklad p-1 = 2 * 5 * 17 * 1429 * 4345057847939
#h = 7
#t = 191372646975736299
#A wysyla y = 447200612697409108
#B zgaduje: t
#Wynik rzutu: Orzel – B nie zgadl
#A ujawnia x = 276002289612725267
#B: to bylo h -> Orzel




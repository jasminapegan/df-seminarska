# reviews - povzetek

- [ ] dodati sliko/boljši opis Bloomove funkcije
- [ ] preimenovati izraze da bojo konsistentni (npr. ocena dela datoteke = zgostitvena ocena = ocena pomembnosti?)
- [x] ključne besede v SLO
- [ ] graf večji tekst na oseh
- [ ] opis strukture članka brisat? (js bi pustila)
- [x] link do repota? (nardim repo javen? Lahko samo mogoce prej popravimo par stvari)
- [ ] članek --> raziskava/delo/avtorji v [x] navajajo
- [ ] označit enačbe? (oštevilčit)
- [ ] naslove poštimat: 1.1, 3.4.2
- [ ] **očitno članek nima napake? (utež je med 0 in 1)** to predvidevam da je review od brodnika 90% (glede na slog pisanja, napake in ker je ene stvari iz reviewja spraseval) Jaz sem se vedno mnenja da je v clanku napaka, saj se avtorji zgledujejo po tf idf shemi ki je drugacna. Poleg tega je ocitno da ta sledi ni res in ga ne razumem. Sem pa mnenja da bi bilo dobro ce ta del mogoce malo boljse opisemo oz argumentiramo zakaj tako mislimo
	n: veliko praštevilo, večje od chf_ch^D;  <-- tle smo napisali da je n število vseh datotek ...
	chf_ch^D < n (število pojavitev zloga ch v datoteki h
	sledi: 0 < (chf__ch^D)/n < 1 => 0 < log_10((chf__ch^D)/n) < 1 => 0 < 1 - log_10((chf__ch^D)/n) < 1
- [ ] bolje opisat slike (kaj so stolpci in kaj je črta)
- [ ] Uteži bi lahko raziskali bolje, saj se v članku pojavi napaka pri računanju uteži, ki jo opišejo avtorji algoritma FbHash.
- [ ] Vredno bi bilo preiskusiti tudi z naključni šum, saj pokažejo, da pomankanje uteži prinese slabše rezultate, medtem ko uporaba različnih uteži ne prikaže bistvenih razlik pri rezultatih.
- [x] pobrisat naše IDje -- zamenjat z imenom fakultete
- [ ] funkcije, ki jih enačbe uporabljajo kot osnovo, niso podrobno obrazložene
- [ ] popravek zaporedja člankov (knjiga ima prednost pred spletno stranjo) <-- a to je sploh možno če se samo generira?
- [ ] maybe diagram, ki povzame algoritem?
- [ ] V uvodu: ssdeep in sdhash lahko preslepi aktivni napadalec, FbHash algoritma pa ne. Menim da te informacije ne spadajo v uvod, temveč pod opise posameznih algoritmov in zaključek.
- [ ] Uvod: podati naše ugotovitve (ne samo od članka)
- Sebastian: napaka v kosinusni podobnosti in metodi FbHash-s ker drugace deluje

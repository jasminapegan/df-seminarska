# reviews - povzetek

TODO
- [ ] preimenovati izraze da bojo konsistentni (npr. ocena dela datoteke = zgostitvena ocena = ocena pomembnosti?)
- [x] Vredno bi bilo preiskusiti tudi z naključni šum, saj pokažejo, da pomankanje uteži prinese slabše rezultate, medtem ko uporaba različnih uteži ne prikaže bistvenih razlik pri rezultatih.
- [ ] funkcije, ki jih enačbe uporabljajo kot osnovo, niso podrobno obrazložene

MAYBE DONE
- [ ] opis strukture članka brisat? (js bi pustila + 1)
- [ ] V uvodu: ssdeep in sdhash lahko preslepi aktivni napadalec, FbHash algoritma pa ne. premaknit iz uvoda v opise algoritmov in zaključek. (meni je ok, pustimo tko?)
- [x] link do repota? (nardim repo javen? Lahko samo mogoce prej popravimo par stvari) <-- sm dala da je javen, moramo še kje citirat?
- [ ] **(mogoce popravljeno)** Uteži bi lahko raziskali bolje, saj se v članku pojavi napaka pri računanju uteži, ki jo opišejo avtorji algoritma FbHash.
- [ ] **(mogoce popravljeno)** **očitno članek nima napake? (utež je med 0 in 1)** to predvidevam da je review od brodnika 90% (glede na slog pisanja, napake in ker je ene stvari iz reviewja spraseval) Jaz sem se vedno mnenja da je v clanku napaka, saj se avtorji zgledujejo po tf idf shemi ki je drugacna. Poleg tega je ocitno da ta sledi ni res in ga ne razumem. Sem pa mnenja da bi bilo dobro ce ta del mogoce malo boljse opisemo oz argumentiramo zakaj tako mislimo
	n: veliko praštevilo, večje od chf_ch^D;  <-- tle smo napisali da je n število vseh datotek ...
	chf_ch^D < n (število pojavitev zloga ch v datoteki h
	sledi: 0 < (chf__ch^D)/n < 1 => 0 < log_10((chf__ch^D)/n) < 1 => 0 < 1 - log_10((chf__ch^D)/n) < 1
- [ ] označit enačbe? (oštevilčit, meni se zdi nepotrebno ker jih nikjer ne referenciramo +1)
- [x] **(mogoce je ze ali pa je misljeno v nasih ugotovitvah)** bolje opisat slike (kaj so stolpci in kaj je črta)

DONE
- [x ] članek --> raziskava/delo/avtorji v [x] navajajo
- [x] dodati sliko/boljši opis Bloomove funkcije
- [x] ključne besede v SLO
- [x] graf večji tekst na oseh
- [x] naslove poštimat: 1.1, 3.4.2
- [x] pobrisat naše IDje -- zamenjat z imenom fakultete
- [x] popravek zaporedja člankov (knjiga ima prednost pred spletno stranjo) <-- a to je sploh možno če se samo generira?
- [x] Uvod: podati naše ugotovitve (ne samo od članka)
- [x] Sebastian: napaka v kosinusni podobnosti in metodi FbHash-s ker drugace deluje
- [x] maybe diagram, ki povzame algoritem?

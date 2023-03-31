## Boston Housing Dataset. 
Uppgiften för denna datauppsättning är att förutsäga medianvärdet för ägarbostäder i olika förorter till Boston, 
baserat på 13 funktioner relaterade till bostadsmarknaden, demografi och tillgänglighet. 

Specifikt är målvariabeln i denna datamängd mediankostnaden för egna hus (i tusentals dollar) för varje förort, 
och de 13 indatavariablerna inkluderar:

CRIM: brottslighet per capita per stad
ZN: andel av bostadsmark som är zonplanerad för tomter över 25 000 kvm.
INDUS: andel tunnland icke-detaljhandel per stad
CHAS: Charles River dummyvariabel (1 om området avgränsar floden; 0 annars)
NOX: kväveoxidkoncentration (delar per 10 miljoner)
RM: genomsnittligt antal rum per bostad
AGE: andelen ägarbostäder byggda före 1940
DIS: vägda avstånd till fem arbetsförmedlingar i Boston
RAD: index för tillgänglighet till radiella motorvägar
TAX: fastighetsskattesats för fullt värde per 10 000 USD
PTRATIO: förhållande mellan elever och lärare per stad
B: 1000(Bk - 0,63)^2 där Bk är andelen "blacks" per stad
LSTAT: % lägre status för befolkningen 

När vi räknar dessa inputdetaljer  är uppgiften att bygga en regressionsmodell som kan förutsäga medianvärdet 
för ägarbostäder för nya förorter i Boston-området. Detta problem kan lösas med hjälp av olika regressionsalgoritmer, 
inklusive linjär regression, beslutsträd, slumpmässiga beslutskogar och neurala nätverk. 

Boston Housing Dataset Regression Model med FastAPI
Det här är ett projekt som visar hur man tränar en regressionsmodell på Boston Housing dataset och använder den 
som ett webb-API med FastAPI. Modellen tränas med den linjära regressionsalgoritmen från scikit-learn, 
och API:n implementeras med FastAPI. 

För att använda API:t, skickas en POST-begäran till /predict-endpoint med en JSON-nyttolast som innehåller 
värden för de 13 ingångsparametrarna i Boston Housing Dataset. Här är ett exempel på JSON-data:
{
     "CRIM": 0,03,
     "ZN": 0,0,
     "INDUS": 5,19,
     "CHAS": 0,
     "NOX": 0,5,
     "RM": 6,0,
     "ÅLDER": 48,5,
     "DIS": 5.0,
     "RAD": 5,
     "SKATT": 224,0,
     "PTRATIO": 20.2,
     "B": 395,43,
     "LSTAT": 8.13
}

Denna JSON-data motsvarar inmatningsdata för en datapunkt i Boston Housing Dataset. När du skickar den här 
JSON-nyttolasten till /predict-slutpunkten för API:t, kommer den tränade regressionsmodellen att använda 
ingångsfunktionerna för att förutsäga medianvärdet för egna hem (i tusentals dollar) för den givna förorten. 

Här är ett exempel på utdata du kan förvänta dig från API:n:

{
     "förutsägelse": 29,77718689149256
}
Denna JSON-utdata innehåller det förutsagda medianvärdet för egna hus för de givna ingångsfunktionerna, vilket i 
det här fallet är cirka 29,8 tusen dollar. 

I fastighetsprisprediktionsproblemet används linjär regression för att bestämma hur olika faktorer påverkar priset 
på en bostad.
När det gäller Boston Housing Dataset beror målvariabeln (huspris) på flera prediktorer som antal rum, brottsfrekvens, 
avstånd till centrum och så vidare. Med hjälp av linjär regression kan du modellera ett linjärt samband mellan dessa 
prediktorer och priset på ett hus.

Dessutom är linjär regression väl lämpad för att modellera linjära samband mellan prediktorer och målvariabeln som 
finns i Boston Housing Dataset. Antalet rum och bostadsyta kan till exempel vara direkt proportionell mot priset 
på ett hus, och brottsligheten kan vara omvänt proportionell mot priset. Linjär regression kan fånga dessa linjära 
samband och förutsäga priset på ett hus baserat på prediktorerna.
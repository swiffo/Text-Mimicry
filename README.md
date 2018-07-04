# Text-Mimicry

Have you ever wondered what sort of text you could randomly generate using the frequencies 
of letter combinations in plays by Shakespeare? If not, please take a moment to wonder as the
rest of the text assumes that you have ...

Wonder no more!

In the following we read 3 plays by Shakespeare, counting and storing all N-letter combinations occuring.
We then generate a random text by first choosing an N-letter combination with each combination having 
a probability of being chosen proportional to the number of times in occurred in the plays. We then extend 
this inductively by taking the last N-1 letters of our random text, and choosing the next letter with
a probability proportional to the number of times the N-letter combination occurs in the plays.

## Example: N = 3 
*Yette thaderewelfeane God-a-fix messe, The ifeart. My this my rommaithim thime, I hosecternight pand th ther's th on to ashost, Wit, se flet bee eno be The againg se Kin wit sor mud, Whim prort yould nothe anque th younne reall builesifer nox, Withe gratep of plucand taked wilure HAMLET. Not a low my an Alike are-deard th-abe vpot hat mouth die-grion I the thich Mon. I pors. . In come, but ind fat yought's bery your lin ande, Sper in*

## Example: N = 5
*I would stayes and cold. Nor where dar’s, eyes, & where so;’ and thou whale. Enters Will them know absencrants from when? QUEEN. Ha, what stayers For no shadowes of who storme what might, I pray first be gold, will neuer come against than, ward he inst the Lyons with hath beneath we will but yet meat mine meager of chargesse rugged fair tear. Banq. Look you friends of Dardanian error, lost last, and euer shut they not so to pay Mor. Iew. Yes flight. Actus Tertinbras; this so I behove that*

## Example: N = 10
*l said; very well said; very well said; very well, my conscience is a kinde of diuell; and let their beds Be made as soft as yours doth temperately keep time, And thy best graces spend it in some words vpon that heart, Courage, Fortitude, I haue supt full with him along Sal. I did my Lord, And I do thinke of this descriptions, backe againe: This is the false Heart doth know. Exeunt. Scena Secunda. Enter Macbeth as King, Lady Lenox, Rosse, Thanes, And make vs Med'cines of our Cawdron All. Double,*

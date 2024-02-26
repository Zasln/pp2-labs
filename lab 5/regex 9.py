import re
txt = """Introduction

Usually, prejudice is realized through fear, hatred, or even the threat of a shared enemy. It entails biases perpetuated with the intention of helping people assume consolidated power within the society, for them to achieve individual interests that are in most cases quite unconstructive. Past evidence indicates that prejudice and the resulting discrimination have far-reaching effects on the lives of society members. Such affects are apparent in the play The Merchant of Venice, where hatred between different groups of individuals negatively affects healthy co-existence. One of the key foundations of this prejudice is religious differences. The play illustrates how forms of religious bias have distorted relationships and interactions between characters.
Body

Religious prejudice in the play is presented through biased beliefs about the morals and values held by the Jews. It is clear that Christians view Jewish morals and values as compromised, particularly when it comes to lending of money. The Jews are considered shrewd, mean, and heartless. This view is evident when Antonio says to Bassanio “I pray you, think you question with the Jew? …You may as well do anything most hard, as seek to soften that-than which what’s harder? – his Jewish heart.” This illustrates of how lowly Christians thought of the Jewish morals and values were. In the quest to challenge and change these morals and values, Christian characters in the play conspire to expose Shylock with the intention of forcing him to convert to Christianity.  In this, religious biases on conventional moral and values causes major conflicts and co-existence problems.  

As well, religious prejudice is exhibited through beliefs on the type of foods that should be consumed. In the play, Shylock detests Christians for their cuisine choices as expressed by his response to dinner invitation by Bassanio. Following the invitation he says, “Yes, to smell pork; to eat of the habitation which your prophet the Nazarite conjured the devil into.”  In another incident, Shylock made it clear to Yachnin and Patricia that he could buy with them, sell with them, walk with them and so following; but would never eat, drink, or pray with them. The Jewish beliefs that are the basis of Shylock’s bias against foods such as pork and those who consume them creates distrust and strenuous relationships between Jews and Christians. This makes cuisine a major cause of religious prejudice in the play."""

for x in txt:
    a=re.search("[A-Z]", x)
    if a:
        print(" "+x, end="")
    else:
        print(x.lower(), end="")
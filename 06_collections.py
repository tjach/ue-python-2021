# Create a list. Append the names of your colleagues and friends to it. Has the id of the
# list changed? Sort the list. What is the first item in the list? What is the second item in
# the list?

# 2. Create a tuple with your first name, last name, and age. Create a list, people, and
# append your tuple to it. Make more tuples with the corresponding information from
# your friends and append them to the list. Sort the list.

# 4. Go to Project Gutenberg11 and find a page of text from Shakespeare. Paste it into a
# triple-quoted string. Create another string with a paragraph of text from Ralph Waldo
# Emerson. Use the string’s .split method to get a list of words from each. Using set
# operations find the common words and words unique to both authors. Find out all words starting with `w`.

# 5. Tuples and lists are similar but have different behavior. Use set operations to find the
# attributes of a list object that are not in a tuple object.

lista = ["Tomek", "Marcin", "Michał", "Paweł", "Piotr", "Joanna", "Anna", "Dariusz"]

#
# other_list = list()
#
# for elem in lista:
#     if elem.startswith("M"):
#         other_list.append(elem)
# print(other_list)


# other_list = [ elem.upper() for elem in lista if elem.startswith("M") ]

# print(other_list)

# print(lista[::-1])

# tup = ("ala", "ola")

# def fun():
#     print("Inner function")
#     return "ala", 1, None
#
# _, _, v3 = fun()
#
# print(v3)
# print(type(v3))

# print(tup)
# print(type(tup))


shs = '''

As You Like It
Shakespeare homepage | As You Like It | Act 2, Scene 5
Previous scene | Next scene
SCENE V. The Forest.
Enter AMIENS, JAQUES, and others
SONG.
AMIENS
Under the greenwood tree
Who loves to lie with me,
And turn his merry note
Unto the sweet bird's throat,
Come hither, come hither, come hither:
Here shall he see No enemy
But winter and rough weather.
JAQUES
More, more, I prithee, more.
AMIENS
It will make you melancholy, Monsieur Jaques.
JAQUES
I thank it. More, I prithee, more. I can suck
melancholy out of a song, as a weasel sucks eggs.
More, I prithee, more.
AMIENS
My voice is ragged: I know I cannot please you.
JAQUES
I do not desire you to please me; I do desire you to
sing. Come, more; another stanzo: call you 'em stanzos?
AMIENS
What you will, Monsieur Jaques.
JAQUES
Nay, I care not for their names; they owe me
nothing. Will you sing?
AMIENS
More at your request than to please myself.
JAQUES
Well then, if ever I thank any man, I'll thank you;
but that they call compliment is like the encounter
of two dog-apes, and when a man thanks me heartily,
methinks I have given him a penny and he renders me
the beggarly thanks. Come, sing; and you that will
not, hold your tongues.
AMIENS
Well, I'll end the song. Sirs, cover the while; the
duke will drink under this tree. He hath been all
this day to look you.
JAQUES
And I have been all this day to avoid him. He is
too disputable for my company: I think of as many
matters as he, but I give heaven thanks and make no
boast of them. Come, warble, come.
SONG.
Who doth ambition shun
All together here

And loves to live i' the sun,
Seeking the food he eats
And pleased with what he gets,
Come hither, come hither, come hither:
Here shall he see No enemy
But winter and rough weather.
JAQUES
I'll give you a verse to this note that I made
yesterday in despite of my invention.
AMIENS
And I'll sing it.
JAQUES
Thus it goes:--
If it do come to pass
That any man turn ass,
Leaving his wealth and ease,
A stubborn will to please,
Ducdame, ducdame, ducdame:
Here shall he see
Gross fools as he,
An if he will come to me.
AMIENS
What's that 'ducdame'?
JAQUES
'Tis a Greek invocation, to call fools into a
circle. I'll go sleep, if I can; if I cannot, I'll
rail against all the first-born of Egypt.
AMIENS
And I'll go seek the duke: his banquet is prepared.
Exeunt severally

Shakespeare homepage | As You Like It | Act 2, Scene 5
Previous scene | Next scene

'''
emers = '''
1. We have a great deal more kindness than is ever spoken. Barring all the selfishness that chills like east winds the world, the whole human family is bathed with an element of love like a fine ether. How many persons we meet in houses, whom we scarcely speak to, whom yet we honor, and who honor us! How many we see in the street, or sit with in church, whom, though silently, we warmly rejoice to be with! Read the language of these wandering eyebeams. The heart knoweth.

2. The effect of the indulgence of this human affection is a certain cordial exhilaration. In poetry, and in common speech, the emotions of benevolence and complacency which are felt toward others, are likened to the material effects of fire; so swift, or much more swift, more active, more cheering are these fine inward irradiations. From the highest degree of passionate love, to the lowest degree of good will, they make the sweetness of life.

3. Our intellectual and active powers increase with our affection. The scholar sits down to write, and all his years of meditation do not furnish him with one good thought or happy expression; but it is necessary to write a letter to a friend, and, [118]forthwith, troops of gentle thoughts invest themselves, on every hand, with chosen words. See in any house where virtue and self-respect abide, the palpitation which the approach of a stranger causes. A commended stranger is expected and announced, and an uneasiness between pleasure and pain invades all the hearts of a household. His arrival almost brings fear to the good hearts that would welcome him. The house is dusted, all things fly into their places, the old coat is exchanged for the new, and they must get up a dinner if they can. Of a commended stranger, only the good report is told by others, only the good and new is heard by us. He stands to us for humanity. He is, what we wish. Having imagined and invested him, we ask how we should stand related in conversation and action with such a man, and are uneasy with fear. The same idea exalts conversation with him. We talk better than we are wont. We have the nimblest fancy, a richer memory, and our dumb devil has taken leave for the time. For long hours we can continue a series of sincere, graceful, rich communications, drawn from the oldest, secretest experience, so that they who sit by, of our own kinsfolk and acquaintance, shall feel a lively surprise at our unusual powers. But as soon as the stranger begins to intrude his partialities, his definitions, his defects, into the conversation, it is all over. He has heard the first, the last and best, he will ever hear from us. He is no stranger now. Vulgarity, ignorance, misapprehension, are old [119]acquaintances. Now, when he comes, he may get the order, the dress, and the dinner, but the throbbing of the heart, and the communications of the soul, no more.

4. What is so pleasant as these jets of affection which relume[279] a young world for me again? What is so delicious as a just and firm encounter of two, in a thought, in a feeling? How beautiful, on their approach to this beating heart, the steps and forms of the gifted and the true! The moment we indulge our affections, the earth is metamorphosed; there is no winter, and no night; all tragedies, all ennuis vanish; all duties even; nothing fills the proceeding eternity but the forms all radiant of beloved persons. Let the soul be assured that somewhere in the universe it should rejoin its friend, and it would be content and cheerful alone for a thousand years.

5. I awoke this morning with devout thanksgiving for my friends, the old and the new. Shall I not call God, the Beautiful, who daily showeth himself so to me in his gifts? I chide society, I embrace solitude, and yet I am not so ungrateful as not to see the wise, the lovely, and the noble-minded, as from time to time they pass my gate.[280] Who hears me, who understands me, becomes mine,—a possession for all time. Nor is nature so poor, but she gives me this joy several times, and thus we weave social threads of our own, a new web of relations; and, as many thoughts in succession substantiate themselves, we shall by-and-by stand in a new world of our own creation, [120]and no longer strangers and pilgrims is a traditionary globe. My friends have come[281] to me unsought. The great God gave them to me. By oldest right, by the divine affinity of virtue with itself, I find them, or rather, not I, but the Deity in me and in them, both deride and cancel the thick walls of individual character, relation, age, sex and circumstance, at which he usually connives, and now makes many one. High thanks I owe you, excellent lovers, who carry out the world for me to new and noble depths, and enlarge the meaning of all my thoughts. These are new poetry of the first Bard[282]—poetry without stop—hymn, ode and epic,[283] poetry still flowing, Apollo[284] and the Muses[285] chanting still. Will these two separate themselves from me again, or some of them? I know not, but I fear it not; for my relation to them is so pure, that we hold by simple affinity, and the Genius[286] of my life being thus social, the same affinity will exert its energy on whomsoever is as noble as these men and women, wherever I may be.
'''

# 4. Go to Project Gutenberg11 and find a page of text from Shakespeare. Paste it into a
# triple-quoted string. Create another string with a paragraph of text from Ralph Waldo
# Emerson. Use the string’s .split method to get a list of words from each. Using set
# operations find the common words and words unique to both authors. Find out all words starting with `w`.

print(len(shs.split()))
print(len(emers.split()))

shs_words = shs.split()
emers_words = emers.split()
# print(shs_words)
# print(emers_words)

return_tab = list()
# for word in shs_words:
#     if word in emers_words:
#         return_tab.append(word)

shs_words_set = set( [e.lower() for e in shs_words] )
emers_words_set = set([e.lower() for e in emers_words])

common_words = shs_words_set.intersection(emers_words_set)
print(common_words)

unique_words_shs = shs_words_set.difference(emers_words_set)
unique_words_emers = emers_words_set.difference(shs_words_set)

print(unique_words_shs)
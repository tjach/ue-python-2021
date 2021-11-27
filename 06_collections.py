# Create a list. Append the names of your colleagues and friends to it. Has the id of the
# list changed? Sort the list. What is the first item in the list? What is the second item in
# the list?

# 2. Create a tuple with your first name, last name, and age. Create a list, people, and
# append your tuple to it. Make more tuples with the corresponding information from
# your friends and append them to the list. Sort the list.

# 4. Go to Project Gutenberg11 and find a page of text from Shakespeare. Paste it into a
# triple-quoted string. Create another string with a paragraph of text from Ralph Waldo
# Emerson. Use the string’s .split method to get a list of words from each. Using set
# operations find the common words and words unique to both authors.


# 5. Tuples and lists are similar but have different behavior. Use set operations to find the
# attributes of a list object that are not in a tuple object.

# attednace_list = list()
# attednace_list.append("Artur")
# attednace_list.append("Alicja")
# attednace_list.append("Denis")
# attednace_list.append("Piotr")
# attednace_list.append("Marcin")
# attednace_list.append("Laura")
#
# # attednace_list.sort(reverse=True)
# # print(attednace_list[-1])
#
# print(attednace_list[::-1])

# tuplee = (1, 2, 3, 4, "ala", None, True)
#
#
# def foo() -> tuple:
#     return 42, "ala"
#
#
# res_from_foo1, _ = foo()
#
# print(res_from_foo1)
# print(type(res_from_foo1))

shs = '''
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
'''

emerson = '''
This society, composed of the first twenty-five men in each class graduating from college, has annual meetings which have called forth the best efforts of many distinguished scholars and thinkers. Emerson's address was listened to with the most profound interest. It declared a sort of intellectual independence for America. Henceforth we were to be emancipated from clogging foreign influences, and a national literature was to expand under the fostering care of the Republic.

These two discourses, Nature and The American Scholar, strike the keynote of Emerson's philosophical, poetical, and moral teachings. In fact he had, as every great teacher has, only a limited number of principles and theories to teach. These principles of life can all be enumerated in twenty words—self-reliance, culture, intellectual and moral independence, the divinity of nature and man, the necessity of labor, and high ideals.

[8]
Emerson spent the latter part of his life in lecturing and in literary work. His son, Dr. Edward Emerson, gave an interesting account of how these lectures were constructed. "All through his life he kept a journal. This book, he said, was his 'Savings Bank.' The thoughts thus received and garnered in his journals were indexed, and a great many of them appeared in his published works. They were religiously set down just as they came, in no order except chronological, but later they were grouped, enlarged or pruned, illustrated, worked into a lecture or discourse, and, after having in this capacity undergone repeated testing and rearranging, were finally carefully sifted and more rigidly pruned, and were printed as essays."

Besides his essays and lectures Emerson left some poetry in which is embodied those thoughts which were to him too deep for prose expression. Oliver Wendell Holmes in speaking of this says: "Emerson wrote occasionally in verse from his school-days until he had reached the age which used to be known as the grand climacteric, sixty-three.... His poems are not and hardly can become popular; they are not meant to be liked by the many, but to be dearly loved and cherished by the few.... His occasional lawlessness in technical construction, his somewhat fantastic expressions, his enigmatic obscurities hardly detract from the pleasant surprise his verses so often bring with them.... The poetic license which we allow in the verse of Emerson is more than excused by the noble spirit which makes us forget its occasional blemishes, sometimes to be pleased with them as characteristic of the writer."

Emerson was always a striking figure in the intellectual life of America. H
'''

# 4. Go to Project Gutenberg11 and find a page of text from Shakespeare. Paste it into a
# triple-quoted string. Create another string with a paragraph of text from Ralph Waldo
# Emerson. Use the string’s .split method to get a list of words from each. Using set
# operations find the common words and words unique to both authors.

shs_as_words = shs.split()
# emerson_as_words = emerson.split()
#
# shs_as_set = set(shs_as_words)
# emesron_as_set = set(emerson_as_words)
#
# print(emesron_as_set)
#
#
# common_words = shs_as_set.intersection(emesron_as_set)
# unique_words_shs = shs_as_set.difference(emesron_as_set)
#
# print(common_words)

# common_words = list()
# for shs_word in shs_as_words:
#     if shs_word in emerson_as_words:
#             common_words.append(shs_word)
#
# print(common_words)

print(shs_as_words)
#
# all_small_letters = list()
# for word in shs_as_words:
#     all_small_letters.append(word.lower())

all_small_letters = [ word.lower() for word in shs_as_words if word.startswith('a') ]

print(all_small_letters)
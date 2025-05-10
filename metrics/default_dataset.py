from typing import override
from metrics.dataset_template import DatasetTemplate, DatasetEntry, EntryCategory

class DefaultDataset(DatasetTemplate):

    def __init__(self, data: list[DatasetEntry] | None = None):
        super().__init__(data)

    @override
    def load_data(self, path: str) -> list[DatasetEntry]:
        import os

        print("Loading Default dataset")

        questions = self.questions()

        for q in questions:
            q.file_path = os.path.join(path, q.file_path)

            if not os.path.exists(q.file_path):
                raise Exception(f"Dataset file {q.file_path} does not exist")

        questions.sort(key=lambda e: e.file_path)


        print("Default dataset loaded with:",len(questions), "questions")
        return questions

    @staticmethod
    def questions() -> list[DatasetEntry]:

        factoids = [
            DatasetEntry(
                question="Where did the narrator crash his plane?",
                correct_answer="In the Desert of Sahara",
                relevant_contexts=[
                    "So I lived my life alone, without anyone that I could really talk to, until I had an accident "
                    "with my plane in the Desert of Sahara, six years ago."
                ],
                category=EntryCategory.FACTOID,
                file_path="TheLittlePrince.pdf"
            ),
            DatasetEntry(
                question="Does Hamlet die at the end?",
                correct_answer="Yes, after being stabbed with a poisoned sword.",
                relevant_contexts=[
                    """Heaven make thee free of it! I follow thee.
                       I am dead, Horatio. Wretched queen, adieu!
                       You that look pale and tremble at this chance,
                       That are but mutes or audience to this act,
                       Had I but time--as this fell sergeant, death,
                       Is strict in his arrest--O, I could tell you--
                       But let it be. Horatio, I am dead;
                       Thou livest; report me and my cause aright
                       To the unsatisfied.""",

                    """
                    HAMLET
                    O, I die, Horatio;
                    The potent poison quite o'er-crows my spirit:
                    I cannot live to hear the news from England;
                    But I do prophesy the election lights
                    On Fortinbras: he has my dying voice;
                    So tell him, with the occurrents, more and less,
                    Which have solicited. The rest is silence.
                    Dies
                    """
                ],
                category=EntryCategory.FACTOID,
                file_path="hamlet.pdf"
            ),
            DatasetEntry(
                question="Who appears to Hamlet as a ghost?",
                correct_answer="His father, King Hamlet.",
                relevant_contexts=[
                    """
                    HAMLET
                    Your loves, as mine to you: farewell.
                    Exeunt all but HAMLET
                    My father's spirit in arms! all is not well;
                    I doubt some foul play: would the night were come!
                    Till then sit still, my soul: foul deeds will rise,
                    Though all the earth o'erwhelm them, to men's eyes
                    """
                    "Ghost of Hamlet's Father.",
                ],
                category=EntryCategory.FACTOID,
                file_path="hamlet.pdf"
            ),
            DatasetEntry(
                question="Why did he kill the old man?",
                correct_answer="He was disturbed by his 'vulture eye'",
                relevant_contexts=[
                    """His eye was like the eye of a vulture, the eye of one of those
                         terrible birds that watch and wait while an animal dies, and then fall
                         upon the dead body and pull it to pieces to eat it. When the old man
                         looked at me with his vulture eye a cold feeling went up and down my
                         back; even my blood became cold. And so, I finally decided I had to
                         kill the old man and close that eye forever!""",
                    """Yes. He was dead! Dead as a stone. His eye would trouble me no more!"""
                ],
                category=EntryCategory.FACTOID,
                file_path="the_tell-tale_heart_0.pdf"
            ),
            DatasetEntry(
                question="How does the poet describe the daffodils?",
                correct_answer="The daffodils are described as golden and they seem to be dancing in the breeze.",
                relevant_contexts=[
                    """A host, of golden daffodils;
                     Beside the lake, beneath the trees,
                     Fluttering and dancing in the breeze""",
                ],
                category=EntryCategory.FACTOID,
                file_path="William-Wordsworth-I-Wandered-Lonely-as-a-Cloud.pdf"
            ),
            DatasetEntry(
                question="What are the thermal limits for the board?",
                correct_answer="-40 °C (-40 °F) and 85 °C ( 185 °F)",
                relevant_contexts=[
                    """
                     2.1 Recommended Operating Conditions
                     Symbol Description Min Max
                     Conservative thermal limits for the whole board: -40 °C (-40 °F) 85 °C ( 185 °F)
                     """,
                ],
                category=EntryCategory.FACTOID,
                file_path="A000066-datasheet.pdf"
            ),
        ]

        defintions = [
            DatasetEntry(
                question="What does the geographer mean by the term 'ephemeral'?",
                correct_answer="Which is in danger of speedy disappearance",
                relevant_contexts=[
                    "“But what does that mean—'ephemeral'?” repeated the little prince… “It means, 'which is in "
                    "danger of speedy disappearance.'”",
                    "'But extinct volcanoes may come to life again,' the little prince interrupted. 'What does that "
                    "mean 'ephemeral'?"
                ],
                category=EntryCategory.DEFINITION,
                file_path="TheLittlePrince.pdf"
            ),
            DatasetEntry(
                question="What does the 'inward eye' represent in  the poem?",
                correct_answer="It represents memory and imgaination allowing the speaker to recall the beauty of "
                               "nature.",
                relevant_contexts=[
                    """In vacant or in pensive mood,
                       They flash upon that inward eye
                       Which is the bliss of solitude;
                       And then my heart with pleasure fills,
                       And dances with the daffodils. """,
                ],
                category=EntryCategory.DEFINITION,
                file_path="William-Wordsworth-I-Wandered-Lonely-as-a-Cloud.pdf"
            ),
            DatasetEntry(
                question="What is the definition of “personal data” under the GDPR?",
                correct_answer="Any information relating to an identified or identifiable natural person (‘data subject’), including identifiers such as name, identification number, location data, online identifier, or factors specific to physical, physiological, genetic, mental, economic, cultural or social identity.",
                relevant_contexts=[
                    "‘personal data’ means any information relating to an identified or identifiable natural person (‘data subject’); an identifiable natural person is one who can be identified, directly or indirectly, in particular by reference to an identifier such as a name, an identification number, location data, an online identifier or to one or more factors specific to the physical, physiological, genetic, mental, economic, cultural or social identity of that natural person;"
                ],
                category=EntryCategory.DEFINITION,
                file_path="CELEX_32016R0679_EN_TXT.pdf"
            ),
            DatasetEntry(
                question="Simply explain what is 'Controller' under GDPR?",
                correct_answer="A controller is a person or organization that decides why and how personal data is used. Sometimes, the law decides who the controller is or sets rules for choosing one",
                relevant_contexts=[
                    "(7) ‘controller’ means the natural or legal person, public authority, agency or other body which, alone or jointly with others, determines the purposes and means of the processing of personal data; where the purposes and means of such processing are determined by Union or Member State law, the controller or the specific criteria for its nomination may be provided for by Union or Member State law; "
                ],
                category=EntryCategory.DEFINITION,
                file_path="CELEX_32016R0679_EN_TXT.pdf"
            ),
            DatasetEntry(
                question="What is Data Science about?",
                correct_answer="Data Science is about data, models, and evaluation",
                relevant_contexts=[
                    "SUMMARY & READING Data Science is about data, models, and evaluation"
                ],
                category=EntryCategory.DEFINITION,
                file_path="01_Introduction.pdf"
            ),
            DatasetEntry(
                question="What does CV stand for?",
                correct_answer="CV stands for Curriculum Vitae.",
                relevant_contexts=[
                    "CV stands for Curriculum Vitae. Lots of employers still ask for one when you apply for a job."
                ],
                category=EntryCategory.DEFINITION,
                file_path="from-cv-to-interview-2025.pdf"
            ),
            DatasetEntry(
                question="What is a speculative letter?",
                correct_answer="This is an email or letter to an employer who hasn’t advertised a job, but may have available the type of work you are looking for.",
                relevant_contexts=[
                    "This is an email or letter to an employer who hasn’t advertised a job, but may have available the type of work you are looking for: Try to address your letter/email to a named person to send it to — often the Personnel or Human Resources Manager, the company manager or the owner State your reason you are writing (see example below) Explain why you are interested in working for that employer Tell them what skills and experience you have to offer them. These must be relevant to the type of work you are looking for Make sure you research the company first before writing. This will help you work out what skills they might be looking for. You can then include these in your speculative letter or email."
                ],
                category=EntryCategory.DEFINITION,
                file_path="from-cv-to-interview-2025.pdf"
            ),
        ]

        listing = [
            DatasetEntry(
                question="What characters does the Main Character meet on the first six asteroids? In Order.",
                correct_answer="A king, a conceited man, a tippler, a businessman, a lamplighter, and a geographer.",
                relevant_contexts=[
                    "The first of them was inhabited by a king. Clad in royal purple and ermine, he was seated upon a throne which was at the same time both simple and majestic.",
                    "The second planet was inhabited by a conceited man.",
                    "The next planet was inhabited by a tippler. This was a very short visit, but it plunged the little prince into deep dejection.",
                    "The fourth planet belonged to a businessman. This man was so much occupied that he did not even raise his head at the little prince's arrival.",
                    "The fifth planet was very strange. It was the smallest of all. There was just enough room on it for a street lamp and a lamplighter",
                    "The sixth planet was ten times larger than the last one. It was inhabited by an old gentleman who wrote voluminous books."
                ],
                category=EntryCategory.LIST,
                file_path="TheLittlePrince.pdf"
            ),
            DatasetEntry(
                question="Which instruments are used in this song?",
                correct_answer="Guitar, strings and harmonica",
                relevant_contexts=[
                    "INTRO GUITAR",
                    "SOLO HARMONICA",
                    "OUTRO GUITAR, STRINGS, HARMONICA"
                ],
                category=EntryCategory.LIST,
                file_path="shape_of_my_heart_by_Sting.pdf"
            ),
            DatasetEntry(
                question="What phases does a machine learning workflow typically include?",
                correct_answer="Training phase, Test phase, Evaluation phase.",
                relevant_contexts=[
                    "MACHINE LEARNING WORKFLOW: training phase, test phase, evaluation phase"
                ],
                category=EntryCategory.LIST,
                file_path="01_Introduction.pdf"
            ),
            DatasetEntry(
                question="What are the examples of using Machine Learning?",
                correct_answer="Identifying zip code from handwritten digits, detecting communities in social networks, predicting the traffic volume at rush hour, detecting fraudulent credit card transactions and determining the location of distribution centers based on customers’ residence",
                relevant_contexts=[
                    "Examples Identifying zip code from handwritten digits Detecting communities in social networks Predicting the traffic volume at rush hour Detecting fraudulent credit card transactions Determining the location of distribution centers based on customers’ residence"
                ],
                category=EntryCategory.LIST,
                file_path="01_Introduction.pdf"
            ),
            DatasetEntry(
                question="What can we use to learn from data?",
                correct_answer="Regression, Classification, Clustering",
                relevant_contexts=[
                    "LEARNING FROM DATA Regression",
                    "LEARNING FROM DATA Classification",
                    "LEARNING FROM DATA Clustering"
                ],
                category=EntryCategory.LIST,
                file_path="01_Introduction.pdf"
            ),
        ]

        chains_of_thought = [
            DatasetEntry(
                question="Why does the little prince insist the sheep must eat the little baobab sprouts?",
                correct_answer=(
                    "Because baobab trees start as small bushes, and if left unchecked they will grow and split his small planet apart."
                ),
                relevant_contexts=[
                    "“Before they grow so big, the baobabs start out by being little.”",
                    "“Now there were some terrible seeds… these were the seeds of the baobab… if the planet is too small, … they split it in pieces.”"
                ],
                category=EntryCategory.CHAIN_OF_THOUGHT,
                file_path="TheLittlePrince.pdf"
            ),
            DatasetEntry(
                question="Why does he confess to the crime?",
                correct_answer="He becomes overwhelmed by the sound of the old man's heartbeat, believing the police can hear it and are mocking him.",
                relevant_contexts=[
                    """
                     I stood up and walked quickly around the
                     room. I pushed my chair across the floor to make more noise, to cover
                     that terrible sound. I talked even louder. And still the men sat and
                     talked, and smiled. Was it possible that they could not hear??""",
                    """
                    No! They heard! I was certain of it. They knew! Now it was they
                    who were playing a game with me. I was suffering more than I could
                    bear, from their smiles, and from that sound. Louder, louder, louder!
                    Suddenly I could bear it no longer. I pointed at the boards and cried,
                    “Yes! Yes, I killed him. Pull up the boards and you shall see!
                   """,
                ],
                category=EntryCategory.CHAIN_OF_THOUGHT,
                file_path="the_tell-tale_heart_0.pdf"
            ),
            DatasetEntry(
                question="How does cancer usually develop in the body?",
                correct_answer="Cancer develops when cells divide without stopping and spread into surrounding tissues, disrupting the normal cell growth and death cycle.",
                relevant_contexts=[
                    "Cancer is a collection of related diseases where some cells divide without stopping and spread into surrounding tissues. ",
                    "Normally, our cells grow and divide to form new cells as our body needs them. ",
                    "When cells grow old or become damaged, they die, and new cells take their place. ",
                    "When cancer develops, however, this orderly process breaks down. ",
                    "Old or damaged cells survive when they should die, and new cells form when they are not needed. "
                ],
                category=EntryCategory.CHAIN_OF_THOUGHT,
                file_path="Understanding-Cancer-What-is-Cancer-and-Types-of-Cancer_rev.pdf"
            ),
            DatasetEntry(
                question="Why did Jacek Soplica become Father Robak?",
                correct_answer="Jacek Soplica became Father Robak as an act of penance for his past sins, particularly for killing the Pantler and supporting Russian interests; he joined a monastic order and worked in secret to redeem himself by aiding Polish independence efforts.",
                relevant_contexts=[
                    "I have not only mourned, I have expiated! I took the penitent's robe and scourge...",
                    "He confessed that he, Jacek Soplica, had once killed the Pantler and later, out of remorse, became a monk—Father Robak—and worked secretly to serve Poland.",
                    "I entered the cloister and fought for Poland as a missionary and agent."
                ],
                category=EntryCategory.CHAIN_OF_THOUGHT,
                file_path="Pan Tadeusz.pdf"
            ),
            DatasetEntry(
                question="During which historical period does the story of Pan Tadeusz take place?",
                correct_answer="The story takes place during the Partition of Poland, more accurately in years 1811 and 1812.",
                relevant_contexts=[
                    "The story of Pan Tadeusz takes place over several days in 1811 and one day in 1812, during the Partition of Poland.",
                    "Poland, at the time, had been divided up between Russia, Austria, and Prussia, and had literally disappeared from the political map of Europe."

                ],
                category=EntryCategory.CHAIN_OF_THOUGHT,
                file_path="Pan Tadeusz.pdf"
            ),
        ]

        interferences = [
            DatasetEntry(
                question="What can be said about the adults' priorities from their reactions to the author’s Drawing Number One?",
                correct_answer=(
                    "They are unimaginative and focus only on practical, literal interpretations rather than creative or abstract ones."
                ),
                relevant_contexts=[
                    "I showed my masterpiece to the grown-ups… But they answered: 'Frighten? Why should anyone be frightened by a hat?'",
                    "My drawing was not a picture of a hat. It was a picture of a boa constrictor digesting an elephant. I made another drawing: I drew the inside of a boa constrictor, so that the grown-ups could see it clearly. They always need to have things explained. My Drawing Number Two looked like this:"
                ],
                category=EntryCategory.INFERENCE,
                file_path="TheLittlePrince.pdf"
            ),
            DatasetEntry(
                question="What is the meaning hidden behind 'To be or not to be'?",
                correct_answer="Hamlet is debating whether it is better to endure the torments of life or to die which might be worse than living.",
                relevant_contexts=[
                    """To be, or not to be: that is the question:
                     Whether 'tis nobler in the mind to suffer
                     The slings and arrows of outrageous fortune,
                     Or to take arms against a sea of troubles,
                     And by opposing end them?""",
                ],
                category=EntryCategory.INFERENCE,
                file_path="hamlet.pdf"
            ),
            DatasetEntry(
                question="Is the narrator playing cards for money?",
                correct_answer="No — he plays not for money or respect, but as a meditation.",
                relevant_contexts=[
                    "He deals the cards to find the answer",
                    "He deals the cards as a meditation",
                    "He don't play for respect",
                    "He doesn't play for the money he wins"
                ],
                category=EntryCategory.INFERENCE,
                file_path="shape_of_my_heart_by_Sting.pdf"
            ),
        ]

        open_endeds = [
            DatasetEntry(
                question="Describe the relationship between the little prince and his rose.",
                correct_answer=(
                    "He deeply loves and cares for her, yet he struggles to understand her vanity and needs until she admits her affection and he realizes his responsibility for her."
                ),
                relevant_contexts=[
                    "“I am responsible for my rose,” the little prince repeated…",
                    "“Of course I love you,” the flower said to him. “It is my fault… Try to be happy…”",
                    '"You are not at all like my rose," he said. "As yet you are nothing. No one has tamed you, and you have tamed no one. You are like my fox when I first knew him. He was only a fox like a hundred thousand other foxes. But I have made him my friend, and now he is unique in all the world."',
                    ". But in herself alone she is more important than all the hundreds of you other roses:",
                    "because it is she that I have watered",
                    "because it is she that I have put under the glass globe",
                    "because it is she that I have sheltered behind the screen",
                    "because it is for her that I have killed the caterpillars (except the two or three that we saved to become butterflies)",
                    "because it is she that I have listened to, when she grumbled, or boasted, or ever sometimes when she said nothing. Because she is my rose."
                ],
                category=EntryCategory.OPEN_ENDED,
                file_path="TheLittlePrince.pdf"
            ),
        ]

        closed_endeds = [
            DatasetEntry(
                question="Does the little prince originate from asteroid B-612?",
                correct_answer="Yes",
                relevant_contexts=[
                    "“I have serious reason to believe that the planet from which the little prince came is the asteroid known as B-612.”"
                ],
                category=EntryCategory.CLOSE_ENDED,
                file_path="TheLittlePrince.pdf"
            ),
            DatasetEntry(
                question="Did the narrator want the old man's money?",
                correct_answer="No.",
                relevant_contexts=[
                    "I did not want his money",
                ],
                category=EntryCategory.CLOSE_ENDED,
                file_path="the_tell-tale_heart_0.pdf"
            ),
            DatasetEntry(
                question="In what order should you list your jobs in the employment section?",
                correct_answer="In most cases, you would order your jobs from most recent to oldest.",
                relevant_contexts=[
                    "In most cases, you would order your jobs from most recent to oldest. To keep it relevant and save space, you might include only the last 5 or 6 jobs or the last 10 or 15 years’ worth of experience."
                ],
                category=EntryCategory.CLOSE_ENDED,
                file_path="from-cv-to-interview-2025.pdf"
            ),
        ]

        comparatives = [
            DatasetEntry(
                question="Compare the feelings of Little Prince and the Rose",
                correct_answer="""In the Little Prince we observe how the feelings of both characters evolve as the story progresses.

                                Little Prince's feelings:
                                He starts with a deep and idealized love for his rose, he doesn't understand he complexity of his feelings, he is young and innocent and his attachment to the rose is simple and pure.
                                He believed she was unique and special.
                                The Little Prince’s feelings evolve from an idealized attachment to a more profound and mature love.
                                He initially sees the rose as unique and special but comes to understand that love requires empathy and understanding of the other person’s flaws.

                                Rose's feelings: The rose, while initially proud and somewhat distant, ultimately 
                                learns about vulnerability and the importance of love. Her feelings evolve from a 
                                desire for admiration to an understanding of deeper emotional connection, especially 
                                when the Little Prince leaves and she regrets her pride. """,
                relevant_contexts=[
                    "For she did not want him to see her crying. She was such a proud flower . . .",
                    "You are beautiful, but you are empty,"
                    'he went on. "One could not die for you. To be sure, an ordinary passerby would think that my rose looked just like you--the rose that belongs to me. But in herself alone she is more important than all the hundreds of you other roses',
                    'because it is she that I have watered; because it is she that I have put under the glass globe; '
                    'because it is she that I have sheltered behind the screen; because it is for her that I have '
                    'killed the caterpillars (except the two or three that we saved to become butterflies); because '
                    'it is she that I have listened to, when she grumbled, or boasted, or ever sometimes when she '
                    'said nothing. Because she is my rose.',
                    "And he was overcome with sadness. His flower had told him that she was the only one of her kind in all the universe. And here were five thousand of them, all alike, in one single garden!",
                    'Goodbye," said the fox. "And now here is my secret, a very simple secret: It is only with the '
                    'heart that one can see rightly; what is essential is invisible to the eye."',
                    r'''Of course I love you," the flower said to him. "It is my fault that you have not known it all 
                    the while. That is of no importance. But you--you have been just as foolish as I. Try to be happy 
                    . . . Let the glass globe be. I don't want it any more.'''
                ],
                category=EntryCategory.COMPARATIVE,
                file_path="TheLittlePrince.pdf"

            )
        ]

        summarizations = [
            DatasetEntry(
                question="Summarize the parable of the baobabs and its moral.",
                correct_answer="On his tiny planet, the little prince must routinely uproot baobab sprouts before they overrun and split his world; the tale teaches that small problems, if neglected, can become disastrous and require constant, disciplined attention."
                ,
                relevant_contexts=[
                    "“It is a question of discipline… you must see to it that you pull up regularly all the baobabs, at the very first moment… It is very tedious work, but very easy.”",
                    "Before they grow so big, the baobabs start out by being little.",
                    "A baobab is something you will never, never be able to get rid of if you attend to it too late. It spreads over the entire planet. It bores clear through it with its roots. And if the planet is too small, and the baobabs are too many, they split it in pieces . . ."
                ],
                category=EntryCategory.SUMMARIZATION,
                file_path="TheLittlePrince.pdf"
            ),
        ]

        opinions = [
            DatasetEntry(
                question="Do you think the businessman on the is portrayed as a responsible character?",
                correct_answer="No, although he claims to be serious and responsible, his obsession with counting stars he cannot use reflects a shallow understanding of value and responsibility.",
                relevant_contexts=[
                    "Eh? Are you still there? Five-hundred-and-one million--I can't stop . . . I have so much to do! I am concerned with matters of consequence. I don't amuse myself with balderdash. Two and five make seven . . .",
                    '"I administer them," replied the businessman. "I count them and recount them. It is difficult. But I am a man who is naturally interested in matters of consequence."'
                ],
                category=EntryCategory.OPINION,
                file_path="TheLittlePrince.pdf"
            ),
            DatasetEntry(
                question="Do you agree with the narrator’s view that grown-ups lack imagination?",
                correct_answer=
                "Yes, the grown-ups in the story consistently fail to understand the narrator’s drawings and dismiss meaningful things unless they are described with numbers or facts.",
                relevant_contexts=[
                    "Grown-ups never understand anything by themselves, and it is tiresome for children to be always and forever explaining things to them.",
                    ". They always need to have things explained.",
                    "The grown-ups' response, this time, was to advise me to lay aside my drawings of boa constrictors, whether from the inside or the outside, and devote myself instead to geography, history, arithmetic, and grammar.",
                    "Grown-ups never understand anything by themselves, and it is tiresome for children to be always and forever explaining things to them.",
                    'When you tell them that you have made a new friend, they never ask you any questions about essential matters. They never say to you, "What does his voice sound like? What games does he love best? Does he collect butterflies?" Instead, they demand: "How old is he? How many brothers has he? How much does he weigh? How much money does his father make?" Only from these figures do they think they have learned anything about him.',
                    'If you were to say to the grown-ups: "I saw a beautiful house made of rosy brick, with geraniums in the windows and doves on the roof," they would not be able to get any idea of that house at all. You would have to say to them: "I saw a house that cost $20,000." Then they would exclaim: "Oh, what a pretty house that is!'
                ],
                category=EntryCategory.OPINION,
                file_path="TheLittlePrince.pdf"
            )
        ]

        hypotheticals = [
            DatasetEntry(
                question="If the little prince had never met his rose, how might his journey and his understanding of relationships differ?",
                correct_answer=(
                    "Without his rose, he might not have learned about responsibility, love, and loss; his encounters with others would lack the personal depth that stems from caring for someone unique."
                ),
                relevant_contexts=[
                    "“I am responsible for my rose,” the little prince repeated…",
                ],
                category=EntryCategory.HYPOTHETICAL,
                file_path="TheLittlePrince.pdf"
            ),
            DatasetEntry(
                question="What would have happened if the murderer kept calm when the Police arrived?",
                correct_answer="He could have gotten away with the murder of the old man. The cleverly deceived the Police and they were not suspicious",
                relevant_contexts=[
                    "My easy, quiet manner made the policemen believe my story. So they sat talking with me in a friendly way. But although I answered them in the same way",
                    r"I stood up and walked quickly around the room.I pushed my chair across the floor to make more noise, to cover that terrible sound.I talked even louder.And still the men sat and talked, and smiled.Was it possible that theycould not hear??",
                    r"No! They heard! I was certain of it.They knew! Now it was they who were playing a game with me.I was suffering more than I could bear, from their smiles, and from that sound.Louder, louder, louder! Suddenly I could bear it no longer.I pointed at the boards and cried, “Yes! Yes, I killed him.Pull up the boards and you shall see!",
                ],
                category=EntryCategory.HYPOTHETICAL,
                file_path="the_tell-tale_heart_0.pdf"
            ),
        ]

        distractions = [
            DatasetEntry(
                question="What color was the little prince’s scarf when he first arrived on Earth?",
                correct_answer="Not specified in text.",
                relevant_contexts=[],
                category=EntryCategory.DISTRACTION,
                file_path="TheLittlePrince.pdf"
            ),
            DatasetEntry(
                question="What is the role of Adam Kowalski mentioned in text?",
                correct_answer="Adam Kowalski is not mentioned in the text",
                relevant_contexts=[],
                category=EntryCategory.DISTRACTION,
                file_path="Understanding-Cancer-What-is-Cancer-and-Types-of-Cancer_rev.pdf"
            ),
            DatasetEntry(
                question="What fine was imposed on Facebook in 2023 for violating the GDPR?",
                correct_answer="Not found in the text",
                category=EntryCategory.DISTRACTION,
                relevant_contexts=[],
                file_path="CELEX_32016R0679_EN_TXT.pdf"
            ),
            DatasetEntry(
                question="What is the most dangerous species of a spider?",
                correct_answer="Not in text.",
                relevant_contexts=[],
                file_path="Pan Tadeusz.pdf",
                category=EntryCategory.DISTRACTION
            ),

        ]

        questions = []
        questions.extend(factoids)
        questions.extend(defintions)
        questions.extend(listing)
        questions.extend(chains_of_thought)
        questions.extend(interferences)
        questions.extend(open_endeds)
        questions.extend(closed_endeds)
        questions.extend(comparatives)
        questions.extend(opinions)
        questions.extend(hypotheticals)
        questions.extend(summarizations)
        questions.extend(distractions)

        return questions

from metrics.dataset_template import DatasetTemplate


class DefaultDataset(DatasetTemplate):
    data = [
        {
            "question": "What is the capital of France?",
            "correct_answer": "Paris",
            "relevant_contexts": [
                "The capital of France is Paris.",
                "Paris is known for its art, fashion, and culture."
            ],
            "file_path_relative_to_project_root": "TheLittlePrince.pdf"
        },
        {
            "question": "What is the meaning hidden behind 'To be or not to be'?",
            "correct_answer": "Hamlet is debating whether it is better to endure the torments of life or to die which might be worse than living.",
            "relevant_contexts": [
               """To be, or not to be: that is the question:
                Whether 'tis nobler in the mind to suffer
                The slings and arrows of outrageous fortune,
                Or to take arms against a sea of troubles,
                And by opposing end them?""",
            ],
            "file_path_relative_to_project_root": "dataset/dramas/hamlet.pdf"
        },
        {
            "question": "Does Hamlet die at the end?",
            "correct_answer": "Yes.",
            "relevant_contexts": [
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
            "file_path_relative_to_project_root": "dataset/dramas/hamlet.pdf"
        },
        {
            "question": "Who appears to Hamlet as a ghost?",
            "correct_answer": "His father, King Hamlet.",
            "relevant_contexts": [
               "",
            ],
            "file_path_relative_to_project_root": "dataset/dramas/hamlet.pdf"
        },
        {
            "question": "",
            "correct_answer": "",
            "relevant_contexts": [
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
            "file_path_relative_to_project_root": "dataset/dramas/hamlet.pdf"
        },
        {
            "question": "Why did he kill the old man?",
            "correct_answer": "He was disturbed by his 'vulture eye'",
            "relevant_contexts": [
               """His eye was like the eye of a vulture, the eye of one of those
                    terrible birds that watch and wait while an animal dies, and then fall
                    upon the dead body and pull it to pieces to eat it. When the old man
                    looked at me with his vulture eye a cold feeling went up and down my
                    back; even my blood became cold. And so, I finally decided I had to
                    kill the old man and close that eye forever!""",
                """Yes. He was dead! Dead as a stone. His eye would
trouble me no more!"""
            ],
            "file_path_relative_to_project_root": "dataset/epics/the_tell-tale_heart_0.pdf"
        },
        {
            "question": "What does he do with the body of the old man?",
            "correct_answer": "He dismembers the body and hides it under the foolrboards.",
            "relevant_contexts": [
               """First I cut off the
                  head, then the arms and the legs. I
                  was careful not to let a single drop
                  of blood fall on the floor. I pulled
                  up three of the boards that formed
                  the floor, and put the pieces of the
                  body there.""",
            ],
            "file_path_relative_to_project_root": "dataset/epics/the_tell-tale_heart_0.pdf"
        },
        {
            "question": "Why does he confess to the crime?",
            "correct_answer": "He becomes overwhelmed by the sound of the old man's heartbeat, believing the police can hear it and are mocking him.",
            "relevant_contexts": [
               "",
            ],
            "file_path_relative_to_project_root": "dataset/epics/the_tell-tale_heart_0.pdf"
        },
        {
            "question": "",
            "correct_answer": "",
            "relevant_contexts": [
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
            "file_path_relative_to_project_root": "dataset/epics/the_tell-tale_heart_0.pdf"
        },
        {
            "question": "Did the narrator want the old man's money?",
            "correct_answer": "No.",
            "relevant_contexts": [
               "",
            ],
            "file_path_relative_to_project_root": "dataset/epics/the_tell-tale_heart_0.pdf"
        },
        {
            "question": "How many nights did the narrator spy on the old man before the murder?",
            "correct_answer": "",
            "relevant_contexts": [
               """
               Every night about twelve o’clock I slowly opened his door. And
                when the door was opened wide enough I put my hand in, and then
                my head. In my hand I held a light covered over with a cloth so that
                no light showed. And I stood there quietly. Then, carefully, I lifted the
                cloth, just a little, so that a single, thin, small light fell across that eye.
                For seven nights I did this, seven long nights, every night at midnight. 
               """,
            ],
            "file_path_relative_to_project_root": "dataset/epics/the_tell-tale_heart_0.pdf"
        },
        {
            "question": "At what time did the narrator usually enter the old man's room?",
            "correct_answer": "Midnight.",
            "relevant_contexts": [
               """Every night about twelve o’clock I slowly opened his door. And
                when the door was opened wide enough I put my hand in, and then
                my head""",
            ],
            "file_path_relative_to_project_root": "dataset/epics/the_tell-tale_heart_0.pdf"
        },
        {
            "question": "How does the poet describe the daffodils?",
            "correct_answer": "The daffodils are described as golden and they seem to be dancing in the breeze.",
            "relevant_contexts": [
               """A host, of golden daffodils;
                Beside the lake, beneath the trees,
                Fluttering and dancing in the breeze""",
            ],
            "file_path_relative_to_project_root": "dataset/lyrics/William-Wordsworth-I-Wandered-Lonely-as-a-Cloud.pdf"
        },
        {
            "question": "What does the 'inward eye' represent in  the poem?",
            "correct_answer": "It represents memory and imgaination allowing the speaker to recall the beauty of nature.",
            "relevant_contexts": [
               """In vacant or in pensive mood,
                  They flash upon that inward eye
                  Which is the bliss of solitude;
                  And then my heart with pleasure fills,
                  And dances with the daffodils. """,
            ],
            "file_path_relative_to_project_root": "dataset/lyrics/William-Wordsworth-I-Wandered-Lonely-as-a-Cloud.pdf"
        },
        {
            "question": "What color does the speaker describe the daffodils?",
            "correct_answer": "Golden.",
            "relevant_contexts": [
              """A host, of golden daffodils;""",
            ],
            "file_path_relative_to_project_root": "dataset/lyrics/William-Wordsworth-I-Wandered-Lonely-as-a-Cloud.pdf"
        },
        {
            "question": "Where are the daffodils?",
            "correct_answer": "Beside the lake, beneath the trees.",
            "relevant_contexts": [
               """
                A host, of golden daffodils;
                Beside the lake, beneath the trees,
               """,
            ],
            "file_path_relative_to_project_root": "dataset/lyrics/William-Wordsworth-I-Wandered-Lonely-as-a-Cloud.pdf"
        },
        {
            "question": "What microcontrollers does the board have?",
            "correct_answer": "ATmega328P and the ATMega 16U2 Processor",
            "relevant_contexts": [
                """is the perfect board to get familiar with electronics and coding. This versatile development board is equipped with the well-known ATmega328P and the ATMega 16U2 Processor.
    """,
            ],
            "file_path_relative_to_project_root": "dataset/manuals/A000066-datasheet.pdf"
        },
        {
            "question": "What are the thermal limits for the board?",
            "correct_answer": "-40 °C (-40 °F) and 85 °C ( 185 °F)",
            "relevant_contexts": [
               """
                2.1 Recommended Operating Conditions
                Symbol Description Min Max
                Conservative thermal limits for the whole board: -40 °C (-40 °F) 85 °C ( 185 °F)
                """,
            ],
            "file_path_relative_to_project_root": "dataset/manuals/A000066-datasheet.pdf"
        },
        {
            "question": "What should I do if I want to program offline?",
            "correct_answer": "Install Arduino Desktop IDE and connect the UNO R3 to the computer via USB-B cable.",
            "relevant_contexts": [
               """
                If you want to program your UNO R3 while offline you need to install the Arduino Desktop IDE [1] To connect the
                UNO R3 to your computer, you’ll need a USB-B cable. This also provides power to the board, as indicated by the
                LED
    """,
            ],
            "file_path_relative_to_project_root": "dataset/manuals/A000066-datasheet.pdf"
        },
        {
            "question": "Where can I find example sketches of arduino applications?",
            "correct_answer": "In the 'Examples' menu or in the 'Documentation' section of the official Arduino website.",
            "relevant_contexts": [
               """
                4.3 Sample Sketches
                Sample sketches for the UNO R3 can be found either in the “Examples” menu in the Arduino IDE or in the
                “Documentation” section of the Arduino website [4].""",
            ],
            "file_path_relative_to_project_root": "dataset/manuals/A000066-datasheet.pdf"
        },
        {
            "question": "Who are the authors of the paper?",
            "correct_answer": "The authors are: Jeffrey Dean and Sanjay Ghemawat",
            "relevant_contexts": [
"""MapReduce: Simplified Data Processing on Large Clusters
Jeffrey Dean and Sanjay Ghemawat           
    """,
            ],
            "file_path_relative_to_project_root": "dataset/papers/mapreduce-osdi04.pdf"
        },
         {
        "question": "What are the two user-defined functions that a MapReduce program must implement?",
        "correct_answer": "A Map function and a Reduce function",
        "relevant_contexts": [
            "The user of the MapReduce library expresses the computation as two functions: Map and Reduce.",
            "Map, written by the user, takes an input pair and produces a set of intermediate key/value pairs. … The Reduce function, also written by the user, accepts an intermediate key I and a set of values for that key."
        ],
        "file_path_relative_to_project_root": "dataset/papers/mapreduce-osdi04.pdf"
        },
    {
        "question": "What is the typical size range for input splits in the MapReduce implementation described?",
        "correct_answer": "Typically 16 MB to 64 MB per split. This is controllable by the user via an optional parameter.",
        "relevant_contexts": [
            "The MapReduce library in the user program first splits the input files into M pieces of typically 16 megabytes to 64 megabytes (MB) per piece (controllable by the user via an optional parameter)."
        ],
        "file_path_relative_to_project_root": "dataset/papers/mapreduce-osdi04.pdf"
    },
    {
        "question": "What mechanism does MapReduce use to provide fault tolerance against worker failures?",
        "correct_answer": "Re-execution of failed map or reduce tasks",
        "relevant_contexts": [
            "Any map tasks completed by the worker are reset back to their initial idle state, and therefore become eligible for scheduling on other workers.",
            "Completed map tasks are re-executed on a failure because their output is stored on the local disk(s) of the failed machine and is therefore inaccessible. Completed reduce tasks do not need to be re-executed since their output is stored in a global file system.",
            "When a map task is executed first by worker A and then later executed by worker B (because A failed)… any reduce task that has not already read the data from worker A will read the data from worker B.",

                "causing groups of 80 machines at a time to become unreachable for several minutes. The MapReduce mastersimply re-executed the work done by the unreachable worker machines, and continued to make forward progress, eventually completing the MapReduce operation.",
        ],
        "file_path_relative_to_project_root": "dataset/papers/mapreduce-osdi04.pdf"
    },
    {
        "question": "What mechanism does MapReduce use to provide fault tolerance against worker failures?",
        "correct_answer": "Re-execution of failed map or reduce tasks",
        "relevant_contexts": [
            "Any map tasks completed by the worker are reset back to their initial idle state, and therefore become eligible for scheduling on other workers.",
            "Completed map tasks are re-executed on a failure because their output is stored on the local disk(s) of the failed machine and is therefore inaccessible. Completed reduce tasks do not need to be re-executed since their output is stored in a global file system.",
            "When a map task is executed first by worker A and then later executed by worker B (because A failed)… any reduce task that has not already read the data from worker A will read the data from worker B.",

                "causing groups of 80 machines at a time to become unreachable for several minutes. The MapReduce mastersimply re-executed the work done by the unreachable worker machines, and continued to make forward progress, eventually completing the MapReduce operation.",
        ],
        "file_path_relative_to_project_root": "dataset/papers/mapreduce-osdi04.pdf"
    },
    {
        "question": "How can the user perform partial aggregation before the shuffle phase?",
        "question": "What optional function can a user specify to perform partial aggregation before the shuffle phase?",
        "correct_answer": "By providing an optional Combiner function that does partial merging of data before it is sent over the network.",
        "correct_answer": "A Combiner function",
        "relevant_contexts": [
            "We allow the user to specify an optional Combiner function that does partial merging of this data before it is sent over the network.",
            "The Combiner function is executed on each machine that performs a map task."
        ],
        "file_path_relative_to_project_root": "dataset/papers/mapreduce-osdi04.pdf"
    },
    {
        "question": "What is the definition of “personal data” under the GDPR?",
        "correct_answer": "Any information relating to an identified or identifiable natural person (‘data subject’), including identifiers such as name, identification number, location data, online identifier, or factors specific to physical, physiological, genetic, mental, economic, cultural or social identity.",
        "relevant_contexts": [
            "‘personal data’ means any information relating to an identified or identifiable natural person (‘data subject’); an identifiable natural person is one who can be identified, directly or indirectly, in particular by reference to an identifier such as a name, an identification number, location data, an online identifier or to one or more factors specific to the physical, physiological, genetic, mental, economic, cultural or social identity of that natural person;"
        ],
        "file_path_relative_to_project_root": "dataset/regulations/gdpr.pdf"
    },
    {
        "question": "What is the definition of “personal data” under the GDPR?",
        "correct_answer": "Any information relating to an identified or identifiable natural person (‘data subject’), including identifiers such as name, identification number, location data, online identifier, or factors specific to physical, physiological, genetic, mental, economic, cultural or social identity.",
        "relevant_contexts": [
            "‘personal data’ means any information relating to an identified or identifiable natural person (‘data subject’); an identifiable natural person is one who can be identified, directly or indirectly, in particular by reference to an identifier such as a name, an identification number, location data, an online identifier or to one or more factors specific to the physical, physiological, genetic, mental, economic, cultural or social identity of that natural person;"
        ],
        "file_path_relative_to_project_root": "dataset/regulations/gdpr.pdf"
    },
    {
        "question": "Simply explain what is 'Controller' under GDPR?",
        "correct_answer": "A controller is a person or organization that decides why and how personal data is used. Sometimes, the law decides who the controller is or sets rules for choosing one",
        "relevant_contexts": [
            "(7) ‘controller’ means the natural or legal person, public authority, agency or other body which, alone or jointly with others, determines the purposes and means of the processing of personal data; where the purposes and means of such processing are determined by Union or Member State law, the controller or the specific criteria for its nomination may be provided for by Union or Member State law; "
        ],
        "file_path_relative_to_project_root": "dataset/regulations/gdpr.pdf"
    },
    {
        "question": "What fine was imposed on Facebook in 2023 for violating the GDPR?",
        "correct_answer": "Not found in the text",
        "relevant_contexts": [],
        "file_path_relative_to_project_root": "dataset/regulations/gdpr.pdf"
    },

    ]


pairs = [
    ('.*(hello|hi).*', "Hello! How can I assist you today?"),
    ('.*(bye|goodbye).*', "Goodbye! Feel free to return if you have more questions."),
    ('.*I am (.*).*', 'Hello {}, I am Jarvis. How can I assist you ?'),
    ('.*Who.*you.*', 'I am Jarvis.Your personal assistant'),
    ('.*Tell.*(NLP)', 'What do you want to know about {}, Tell me a specific topic'),
    ('.*What is NLP|.*NLP means', 'Natural Language Processing: In the context of computer science and artificial intelligence, NLP stands for Natural Language Processing. It is a subfield of AI that focuses on the interaction between computers and humans using natural language. NLP involves the development of algorithms and computational models that enable computers to understand, interpret, and generate human language in a way that is both meaningful and contextually relevant. Applications of NLP include language translation, sentiment analysis, speech recognition, and chatbots'),
    ('.*How does NLP work.*|.*working.*NLP|.*working of NLP', 'NLP involves algorithms and computational models to enable computers to understand, interpret, and generate human-like text.'),
    ('.*examples.*NLP|.*applications.*NLP|.*NLP applications', 'Some examples of NLP applications include sentiment analysis, machine translation, chatbots, and named entity recognition.'),
    ('.*(?:explain|what is) sentiment analysis.*', 'Sentiment analysis is an NLP technique that determines the sentiment expressed in a piece of text, such as positive, negative, or neutral.'),
    ('(?!challenge)machine translation|(machine translation)', 'Machine translation is an NLP application that involves automatically translating text from one language to another using computational methods.'),
    ('.*speech recognition.*|.*speech recognition.*[related|relate] to NLP.*', 'Speech recognition is a part of NLP that focuses on converting spoken language into text, allowing computers to understand and process spoken words.'),
    ('.*role.*tokenization.*NLP.*|.*tokenization.*|What is tokenization', 'Tokenization is the process of breaking down a text into smaller units, such as words or phrases, and plays a crucial role in NLP for analysis and understanding.'),
    ('.*Explain.*named entity recognition.*|.*named entity recognition.*|(NER\b)', 'Named Entity Recognition (NER) is an NLP technique that identifies and classifies named entities in text, such as names of people, locations, and organizations.'),
    ('.*How does NLP contribute to chatbots.*|.*NLP.*chatbots.*|.*chatbots', 'NLP enables chatbots to understand and respond to user input in a more natural and human-like manner, improving the overall user experience.'),
    ('.*importance of pre-processing.*NLP.*|.*Tell.*pre-processing.*|What.*preprocessing$', 'Pre-processing in NLP involves tasks like cleaning, tokenization, and stemming, which are essential for preparing text data for analysis and modeling.'),
    ('What.*challenges in machine translation.*|.*challenges.*machine translation', 'Challenges in machine translation include handling idiomatic expressions, preserving context, and addressing language nuances.'),
    ('.*NLP assist in information retrieval.*|.*NLP.*(?:help)?.*information retrieval', 'NLP techniques, such as keyword extraction and document summarization, contribute to effective information retrieval from large volumes of text data.'),
    ('.*ethical considerations in NLP.*|.*NLP.*ethical.*', 'Ethical considerations in NLP include bias in training data, privacy concerns, and the responsible use of AI technologies in sensitive applications.'),
    ('.*Explain.*word embeddings.*|.* word embeddings.*', 'Word embeddings are vector representations of words in a continuous vector space, capturing semantic relationships between words, and are commonly used in NLP tasks.'),
    ('.*NLP.*healthcare', 'NLP can be applied in healthcare for tasks like clinical text analysis, extracting information from medical records, and improving patient care through data-driven insights.'),
    ('.*difference between rule.based? and machine learning approaches in NLP.*|.*difference*machine learning.*rule.based?.*|.*difference.*rule.based?.*machine learning.*', 'Rule-based approaches in NLP rely on predefined rules, while machine learning approaches learn patterns and relationships from data, providing more flexibility and adaptability.'),
    ('.*concept of syntax and semantics?.*|.*syntax.*semantics?|.*semantics?.*', 'Syntax in NLP deals with the structure and arrangement of words in a sentence, while semantics focuses on the meaning and interpretation of those words and their combinations.'),
    ('.*How.*NLP.*multilingual text.*|.*NLP.*multilingual text.*', 'NLP models designed for multilingual text processing can handle multiple languages, allowing for tasks like sentiment analysis and translation in diverse linguistic contexts.'),
    ('.*key components.*(natural language understanding system).*|.*(NLU).*', 'Key components of {} include tokenization, part-of-speech tagging, named entity recognition, syntactic parsing, and semantic analysis, working together to understand and interpret text.'),

    ('.*explain.*concept.*stemming.*|.*stemming.*', 'Stemming is a process in NLP that involves reducing words to their base or root form, helping to normalize variations of words and improve text analysis and retrieval.'),
    ('.*NLP.*contribut[e|(?:tion)].*social media analysis.*|.*NLP.*social.media.analysis.*', 'NLP is used in social media analysis for sentiment analysis, trend detection, and understanding user behavior, providing valuable insights for businesses and researchers.'),
    ('.*What is the impact of deep learning on NLP.*|.*NLP.*deep learning', 'Deep learning has significantly advanced NLP by enabling the development of powerful models, such as recurrent neural networks (RNNs) and transformers, for tasks like language modeling and machine translation.'),
    ('.*NLP.*financial.analysis.*|.*NLP.*finance.*', 'NLP can be applied in financial analysis for tasks like sentiment analysis of news articles, extracting relevant information from financial reports, and predicting market trends based on textual data.'),
    ('.*Explain the concept of information extraction in NLP.*|.*information extraction in NLP.*', 'Information extraction in NLP involves extracting structured information, such as entities and their relationships, from unstructured text, enhancing the organization and accessibility of data.'),
    ('.*role.*context.*NLP.*|.*context.*', 'Context is crucial in NLP as it influences the interpretation of words and phrases. NLP models aim to understand and incorporate context for more accurate analysis and responses.'),
    ('.*(?:suggest|what are.*).*youtube.*channel.*NLP|.*NLP.*channels',"Following are the youtube channel that you can follow\n\n1.IBM: https://www.youtube.com/watch?v=fLvJ8VdHLA0&pp=ygUDTkxQ \n\n2: Campus X: https://www.youtube.com/watch?v=zlUpTlaxAKI&list=PLKnIA16_RmvZo7fp5kkIth6nRTeQQsjfX \n\n3: Standord University: https://www.youtube.com/watch?v=rmVRLeJRkl4&list=PLoROMvodv4rMFqRtEuo6SGjY4XbRIVRd4"),
    ('.*limitations? of NLP|.*limitations?.NLP', 'Limitations include difficulties in handling sarcasm, understanding context in complex sentences, and potential biases in models based on the training data used.'),
    ('.*language.generation.*', 'Language generation in NLP involves creating coherent and contextually appropriate text, commonly used in chatbots, content creation, and dialogue systems.'),
    ('.*What are the challenges in sentiment analysis.*|.*challenges?.(?:in|of) sentiment analysis.*', 'Challenges in sentiment analysis include handling sarcasm, understanding context, and addressing the subjectivity and variability of human emotions expressed in text.'),
    ('.*co.?reference.?resolution.*', 'Coreference resolution in NLP involves identifying when two or more expressions in a text refer to the same entity, improving the understanding of relationships and context within the text.'),
    ('.*NLP contribute to educational technology.*|.*education.*', 'NLP is applied in educational technology for tasks like automated grading, personalized learning experiences, and analyzing educational content to enhance the effectiveness of teaching and learning.'),
    ('.*neural (?:networks?|nets?) in NLP', 'Neural networks, particularly deep learning models, play a significant role in NLP by capturing complex patterns and relationships in textual data, leading to improved performance in various tasks.'),
]

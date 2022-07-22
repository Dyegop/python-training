"""
Function to split a long text into chunks of n size
"""

def get_chunks(text: str, max_length: int) -> str:
    start = 0
    end = 0
    while start + max_length < len(text) and end != -1:
        end = text.rfind(" ", start, start + max_length + 1)
        yield text[start:end]
        start = end + 1
    yield text[start:]



sample = "Well, Prince, so Genoa and Lucca are now just family estates of the Buonapartes. But I warn you, " \
         "if you don’t tell me that this means war, if you still try to defend the infamies and horrors perpetrated " \
         "by that Antichrist—I really believe he is Antichrist—I will have nothing more to do with you and you are " \
         "no longer my friend, no longer my ‘faithful slave,’ as you call yourself! But how do you do? I see I have " \
         "frightened you—sit down and tell me all the news. "

chunks = get_chunks(sample, 25)

# Make list with line lengths:
chunks_list = [(n, len(n)) for n in chunks]

print(chunks_list)



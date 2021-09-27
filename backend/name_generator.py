import difflib

def get_overlap(s1, s2):
    s = difflib.SequenceMatcher(None, s1, s2)
    pos_a, pos_b, size = s.find_longest_match(0, len(s1), 0, len(s2)) 
    return (pos_a, pos_b, size)

default_bigrams = {}

def generate_name(bigrams, starts_with="", ends_with="", contains=""):
    start, end = starts_with, ends_with
    interior = contains

    # try to stitch together
    print(get_overlap(start,interior), get_overlap(interior,end))

    # weave new stuff

    return ""

if __name__ == "__main__":
    generate_name(default_bigrams, starts_with="Aura", ends_with="zune", contains="aszu")
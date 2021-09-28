import difflib
import random
from typing import Literal

def get_overlap(s1, s2):
    s = difflib.SequenceMatcher(None, s1, s2)
    pos_a, pos_b, size = s.find_longest_match(0, len(s1), 0, len(s2)) 
    return (pos_a, pos_b, size)

default_bigrams = "auraszunelgettiusabrina"

def generate_name(bigrams, starts_with="", ends_with="", contains=""):
    convergence = 0.5
    bigrams = [(x,y) for x,y in zip(bigrams, bigrams[1:])]

    start, end = starts_with.lower(), ends_with.lower()
    interior = contains.lower()

    def stitchable(left, right):
        for l in range(len(left), 0, -1):
            subseq = left[len(left)-l:]
            if right.startswith(subseq):
                return len(left)-l, len(left), l
        return None

    def weave(s, end: Literal["START", "END"]):
        if end == "START":
            acceptable_bis = [ab for ab in bigrams if ab[1] == s[0]]
            return random.choice(acceptable_bis)[0] + s
        elif end == "END":
            acceptable_bis = [ab for ab in bigrams if ab[0] == s[-1]]
            return s + random.choice(acceptable_bis)[1]

    # create start
    while len(start):
        a, b, s = 0, 0, 0
        out = stitchable(start, interior)
        if out != None: a,b,s = out
        if s>0 and random.uniform(0,1)<convergence:
            interior = start + interior[s:]
            break
        interior = weave(interior, "START")

    while len(end):
        a, b, s = 0, 0, 0
        out = stitchable(interior, end)
        if out != None: a,b,s = out
        if s>0 and random.uniform(0,1)<convergence:
            interior = interior + end[s:]
            break
        interior = weave(interior, "END")
    return interior

if __name__ == "__main__":
    for i in range(10):
        name = generate_name(default_bigrams, starts_with="Aura", contains="sz", ends_with="")
        print(name)
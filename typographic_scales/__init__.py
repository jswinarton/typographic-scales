import math


class Scale:
    def __init__(self, ratio, tones, fundamental_freq):
        self.ratio = ratio
        self.tones = tones
        self.fundamental_freq = fundamental_freq

    def tone(self, tone):
        return self.fundamental_freq * math.pow(self.ratio, (tone / self.tones))

    def tone_by_octave(self, octave, tone):
        if tone > self.tones:
            raise ScaleError("tone out of range")
        tone = octave * self.tones + tone
        return self.tone(tone)




class ScaleError(Exception):
    pass


# s = Scale(2, 5, 16)
# s.tone(0, 0)
# > 16
# s.tone(10)
# > 32
# s.tone(1, 1)

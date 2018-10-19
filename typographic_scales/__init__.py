"""
For more general info, see http://spencermortensen.com/articles/typographic-scale/
"""
import functools
import math


class Scale:
    def __init__(self, base, ratio, steps, intervals=None, sig_figs=0):
        self.ratio = ratio
        self.steps = steps
        self.base = base
        self.sig_figs = sig_figs

        if intervals is None:
            self.intervals = range(steps)
        else:
            self.intervals = intervals

    def tone(self, tone):
        step = self._tone_to_step(tone)
        tone_value = self.base * math.pow(self.ratio, (step / self.steps))
        return self._round(tone_value)

    def _tone_to_step(self, tone):
        num_intervals = len(self.intervals)

        octave = math.floor(tone / num_intervals)
        remainder = tone % num_intervals

        return octave * self.steps + self.intervals[remainder]

    def _round(self, value):
        return round(value, self.sig_figs)


class ScaleError(Exception):
    pass



MajorScale = functools.partial(Scale, ratio=2, steps=12, intervals=[0,4,7])

MinorScale = functools.partial(Scale, ratio=2, steps=12, intervals=[0,3,7])

PentatonicScale = functools.partial(Scale, ratio=2, steps=5)

classical_scale = PentatonicScale(base=12)

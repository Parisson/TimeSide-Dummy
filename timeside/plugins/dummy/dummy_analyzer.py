# -*- coding: utf-8 -*-
#
# Copyright (c) 2007-2009 Guillaume Pellerin <yomguy@parisson.com>

# This file is part of TimeSide.

# TimeSide is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# (at your option) any later version.

# TimeSide is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with TimeSide.  If not, see <http://www.gnu.org/licenses/>.

# Author: Guillaume Pellerin <yomguy@parisson.com>

from timeside.core import implements, interfacedoc
from timeside.core.analyzer import Analyzer
from timeside.core.api import IValueAnalyzer
import numpy


class DummyAnalyzer(Analyzer):

    """A dummy analyzer returning random sample value from audio streaming"""
    implements(IValueAnalyzer)

    @interfacedoc
    def setup(self, channels=None,
              samplerate=None,
              blocksize=None,
              totalframes=None):
        super(MeanDCShift, self).setup(
            channels, samplerate, blocksize, totalframes)
        self.values = numpy.array([0])

    @staticmethod
    @interfacedoc
    def id():
        return "dummy_analyzer"

    @staticmethod
    @interfacedoc
    def name():
        return "Dummy analyzer"

    @staticmethod
    @interfacedoc
    def unit():
        return "No unit"

    def process(self, frames, eod=False):
        size = frames.size
        if size:
            index = numpy.random.randint(0, size, 1)
            self.values = numpy.append(self.values, frames[index])
        return frames, eod

    def post_process(self):
        result = self.new_result(data_mode='value', time_mode='global')
        result.data_object.value = self.values
        self.add_result(result)
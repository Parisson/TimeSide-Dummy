import pytest

@pytest.fixture
def wav_file():
    from timeside.core.tools.test_samples import samples
    return samples['C4_scale.wav']


def test_dummy(wav_file):

    import timeside.core
    decoder = timeside.core.get_processor('file_decoder')(wav_file)
    dummy_analyzer = timeside.core.get_processor('dummy')()
    pipe = (decoder | dummy_analyzer)
    pipe.run()

    assert dummy_analyzer.results.keys() == ['dummy']

from codebreaker_wrapper import codebreaker_wrapper

class TestCodebreakerWrapper(object):
    def test_generate_secret(self):
        w = codebreaker_wrapper()
        w.randrange = lambda x: 2

        assert w.generate_secret() == "3456"

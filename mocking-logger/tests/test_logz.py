import unittest
import logz.logz as logz


class TestLogz(unittest.TestCase):

    def test_info(self):
        # "When used without logger and level arguments, it catches all logging (suppresses existing handlers).
        # You can later access recorded entries from the context manager's records attribute."
        # source: https://stackoverflow.com/a/48196174/1185293
        with self.assertLogs(level='INFO') as log:
            logz.info()
            self.assertEqual(len(log.output), 1)
            self.assertEqual(len(log.records), 1)
            self.assertIn('info', log.output[0])

    def test_debug(self):
        with self.assertLogs(level='DEBUG') as log:
            logz.debug()
            self.assertEqual(len(log.output), 1)
            self.assertEqual(len(log.records), 1)
            self.assertIn('debug', log.output[0])


if __name__ == '__main__':
    unittest.main()

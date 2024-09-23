from runner import Runner
import unittest

class RunnerTest(unittest.TestCase):

    def test_walk(self):
        runner = Runner("John")
        for _ in range(70):
            runner.walk()
        self.assertEqual(runner.distance, 490)

    def test_run(self):
        runner = Runner("Jane")
        for _ in range(70):
            runner.run()
        self.assertEqual(runner.distance, 7350)

    def test_challenge(self):
        runner1 = Runner("Nina")
        runner2 = Runner("Bob")

        for _ in range(10):
            runner1.run()
            runner2.walk()

        self.assertNotEqual(runner1.distance, runner2.distance)


if __name__ == '__main__':
    unittest.main()
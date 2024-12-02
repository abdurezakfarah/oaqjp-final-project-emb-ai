from EmotionDetection import emotion_detector as ed
import unittest

class TestEmotionDetection(unittest.TestCase):
    def testEmotionDetector(self):
        r1 = ed("I am glad this happened")
        self.assertEqual(r1["dominant_emotion"], "joy")

        r1 = ed("I am really mad about this")
        self.assertEqual(r1["dominant_emotion"], "anger")

        r1 = ed("I feel disgusted just hearing about this")
        self.assertEqual(r1["dominant_emotion"], "disgust")

        r1 = ed("I am so sad about this")
        self.assertEqual(r1["dominant_emotion"], "sadness")

        r1 = ed("I am really afraid that this will happen")
        self.assertEqual(r1["dominant_emotion"], "fear")


unittest.main()
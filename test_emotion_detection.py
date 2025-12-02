from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetector(unittest.TestCase):

    def test_joy(self):
        dominant_emotion = emotion_detector("I am glad this happened")
        self.assertEqual(dominant_emotion["dominant_emotion"], "joy")

    def test_anger(self):
        dominant_emotion = emotion_detector("I am really mad about this")
        self.assertEqual(dominant_emotion["dominant_emotion"], "anger")

    def test_disgust(self):
        dominant_emotion = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(dominant_emotion["dominant_emotion"], "disgust")

    def test_sadness(self):
        dominant_emotion = emotion_detector("I am so sad about this")
        self.assertEqual(dominant_emotion["dominant_emotion"], "sadness")

    def test_fear(self):
        dominant_emotion = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(dominant_emotion["dominant_emotion"], "fear")


if __name__ == "__main__":
    unittest.main()
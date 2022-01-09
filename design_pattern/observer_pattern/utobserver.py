import unittest
import observer
import subjects

class UtVisitor(unittest.TestCase):

    def test_observer(self):
        # Create observers
        pbx = observer.PrivateBranchExchange()
        ms  = observer.MailServer()
            
        # Create subject
        subject = subjects.Subject()
        subject.attach(pbx)
        subject.attach(ms)

        # Notify when JB is leave of absence
        subject.notify("JB", "Hachi")
            
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
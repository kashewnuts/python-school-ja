class A(object):

    @classmethod
    def name(cls, msg):
        print "Greetings from classmethod."
        cls.hello(msg)

class B(A):

    @staticmethod
    def hello(msg):
        print "Hello", msg, "on Class-B"

class C(A):

    @staticmethod
    def hello(msg):
        print "Hello", msg, "on Class-C"


B.name("Alice")
C.name("Bob")
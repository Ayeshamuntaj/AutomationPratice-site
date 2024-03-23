import random
import string

class Randomemailgenerator:
    def random_email_generator(size=7,chars=string.ascii_lowercase+string.digits):
        return ''.join(random.choice(chars) for x in range(size))
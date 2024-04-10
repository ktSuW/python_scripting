import re
import hashlib

class PasswordValidator:
    def __init__(self, min_length=8, special_chars="~!@#$%^&*()_+-={}|[]\\:;'<>,.?/"):
        self.min_length = min_length
        self.special_chars = special_chars
        self.criteria = []
    def _check_min_length(self,password):
        pass 
    
    def _check_uppercase(self, password):
        pass
    
    def _check_lowercase(self, password):
        pass 
    
    def _check_digit(self, password):
        pass 
    
    def _check_special_chars(self,password):
        pass 
    
    def validate(self, password):
        pass 
    
    @staticmethod
    def hash_password(password):
        # Use SHA-256 algorithm
        return hashlib.sha256(password.encode()).hexdigest()




"""
hashlib => This module implements a common interface to many different secure hash and message digest algorithms. Included are the FIPS secure hash algorithms SHA1, SHA224, SHA256, SHA384, SHA512, (defined in the FIPS 180-4 standard), the SHA-3 series (defined in the FIPS 202 standard) as well as RSA’s MD5 algorithm (defined in internet RFC 1321). The terms “secure hash” and “message digest” are interchangeable. Older algorithms were called message digests. The modern term is secure hash.
        
single underscore _ => In general, you should use a single leading underscore only when you need to indicate that a variable, class, method, function, or module is intended for internal use within the containing module, class, or package. Again, this is just a well-established naming convention. It's not a strict rule that Python enforces.  


staticmethod => A static method in Python is a method that belongs to a class, not its instances. It does not require an instance of the class to be called, nor does it have access to an instance. Static methods in Python are declared using the @staticmethod decorator. This decorator tells the Python interpreter that the method is static and should be called on the class, not on an instance of the class.

Thus, static methods in Python can be used to perform operations that do not require access to the class instance or its attributes, meaning that they are essentially helper functions.
  
https://hostman.com/tutorials/python-static-method/   
"""

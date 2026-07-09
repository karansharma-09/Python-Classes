"""Problem Statement: 

Design a ‘book’ class with title, author, publisher, price, and author’s royalty as instance variables. Provide getter and setter properties for all variables. Also, define a method royalty() to calculate royalty amount author can expect to receive the following royalties:10%  of the retail price on the first 500 copies; 12.5% for the next 1,000 copies sold, then 15% for all further copies sold. 

Then design a new ‘ebook’ class inherited from the ‘book’ class. Add ebook format (EPUB, PDF,  MOBI, etc) as an additional instance variable in the inherited class.                                                                                                                                    Override royalty() method to deduct GST @12% on ebooks."""

class book:
    def __init__(self,title,author,publisher,price):
        self.author=author
        self.title=title
        self.price=price
        self.publisher=publisher
        self.author_royality=0.0
    #getter and setter methods 
    @property
    def title(self):
        return self._title
    @title.setter
    def title(self,value):
        self._title=value
    
    @property
    def author(self):
        return self._author
    @author.setter
    def author(self,value):
        self._author=value
    @property
    def publisher(self):
        return self._publisher
    @publisher.setter
    def publisher(self,value):
        self._publisher=value
    @property
    def price(self):
        return self._price
    @price.setter
    def price(self,value):
        if value<0:
            raise ValueError("Price cannot be negative.")
        self._price=value
    @property
    def author_royality(self):
        return self._author_royality
    @author_royality.setter
    def author_royality(self,value):
        self._author_royality=value
    
    # Royality calculator
    def royality(self,cp_sold):
        royality_amt=0.0
        if cp_sold<=500:
            royality_amt=cp_sold*self.price*0.1
        elif cp_sold<=1500:
            first_tier=500*self.price*0.10
            second_tier=(cp_sold-500)*self.price*0.125
            royality_amt=first_tier+second_tier
        else:
            first_tier=500*self.price*0.1
            second_tier=1000*self.price*0.125
            third_tier=(cp_sold-1500)*self.price*0.15
            royality_amt=first_tier+second_tier+third_tier
        self.author_royality=royality_amt
        return royality_amt

class ebook(book):
    def __init__(self,title,author,publisher,price,format):
        super().__init__(title,author,publisher,price)
        self.ebook_format=format

        #getter and setter method for ebook format
    @property
    def ebook_format(self):
        return self._ebook_format
    @ebook_format.setter
    def ebook_format(self,value):
        self._ebook_format=value
    
    #overriding
    def royality(self,cp_sold):
        base_royality=super().royality(cp_sold)

        gst_ded=base_royality*0.12 

        final_royality=base_royality-gst_ded

        self.author_royality=final_royality
        return final_royality

    






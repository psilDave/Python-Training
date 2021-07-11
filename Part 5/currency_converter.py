import re


class URLExtractor():

    """ Class responsive for extracting parameters from a valid URL."""

    def __init__(self, url):
        self.url = self.sanitize_url(url)
        self.validate_url()

    @staticmethod
    def sanitize_url(url):
        if type(url) == str:
            return url.strip()
        else:
            return ""

    def validate_url(self):
        if not self.url:
            raise ValueError("The URL is empty.")

        url_pattern = re.compile("(http(s)?://)?(www.)?bytebank.com(.br)?/cambio")
        if not url_pattern.match(self.url):
            raise ValueError("The URL is invalid.")

    def get_url_base(self):
        return self.url[:self.url.find("?")]

    def get_url_parameters(self):
        return self.url[(self.url.find("?") + 1):]

    def get_parameter_value(self, parameter_name):
        ind_parameter = self.get_url_parameters().find(parameter_name)
        ind_value = ind_parameter + len(parameter_name) + 1
        ind_e = self.get_url_parameters().find("&", ind_value)

        if ind_e == -1:
            return self.get_url_parameters()[ind_value:]
        else:
            return self.get_url_parameters()[ind_value:ind_e]

    def __len__(self):
        return len(self.url)

    def __str__(self):
        return self.url + "\n" + "Parameters: " + self.get_url_parameters() + "\n" + "URL base: " + self.get_url_base()

    def __eq__(self, other):
        return self.url == other.url


class CurrencyConversion:

    """ Class responsible for converting from one monetary amount to another. For the class to work correctly,
    consider the conversion ratio of one unit of the current currency to the currency that you want convert.

    - For example: USD to BRL

        USD           BRL
        1             5.23
        x             y

        y = x*5.23

        from_coin: USD
        value_coin: x
        to_coin: BRL
        conversion_rate = 5.23


    """

    def __init__(self, from_coin, value_coin, to_coin, conversion_rate):
        self.from_coin = from_coin
        self.value_coin = value_coin
        self.to_coin = to_coin
        self.conversion_rate = conversion_rate

    def conversion(self):
        return float(self.value_coin) * self.conversion_rate

    def __str__(self):
        return ("Considering the current " + self.from_coin + " to " + self.to_coin +  " currency quote of " + str(self.conversion_rate) +  "," + "\n"
                "the value of " + str(self.value_coin)+ " " + self.from_coin + " converted to " + self.to_coin + " is given by: " + str(self.conversion())+ " " + self.to_coin + "."                                                                                                                                          
                "\n"
                )


bank_url = URLExtractor("bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar")
converter = CurrencyConversion("BRL", bank_url.get_parameter_value("quantidade"), "USD", 0.19)
print(converter)

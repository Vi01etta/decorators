import json
from dec import logger, param_logger


class Country:

    @logger
    def __iter__(self):
        with open("countries.json", 'r', encoding='utf-8') as f:
            text = json.load(f)
            self.countries = set(txt['name']['common'] for txt in text)
            return self


    @param_logger('logs')
    def __next__(self):
        if not self.countries:
            raise StopIteration
        name = self.countries.pop()
        return name


if __name__ == '__main__':
    output_file = open('countries_with_links.txt', 'w', encoding='utf-8')
    for country in Country():
        output_file.write(country + ' - ' + 'https://en.wikipedia.org/wiki/' + country.replace(' ', '_') + '\n')
    output_file.close()
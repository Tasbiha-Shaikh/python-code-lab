letter = '''Dear <|name|> , 
            you are selected!
             <|date|>'''

print(letter.replace("<|name|>", "harry").replace("<|date|>", "24 july 2025"))

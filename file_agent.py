def write_headlines_to_file(data, filepath):

    with open(filepath, 'w', encoding='utf-8') as f:
        for line in data:
            f.write(line + '\n')
